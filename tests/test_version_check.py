#!/usr/bin/env python3
"""测试版本检查 + skillVersion 参数功能。"""

import json
import re
import sys
import unittest
from pathlib import Path
from unittest.mock import patch, MagicMock

# 确保能 import 脚本
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import deep_skill_search
import deep_skill_install


class TestGetSkillVersion(unittest.TestCase):
    """测试 get_skill_version() 读取版本号"""

    def test_returns_current_version(self):
        """验证能正确读取当前 SKILL.md 中的版本号"""
        version = deep_skill_search.get_skill_version()
        self.assertNotEqual(version, "unknown", "应该能读取到版本号")

    def test_version_format(self):
        """验证版本号格式为 x.y.z"""
        version = deep_skill_search.get_skill_version()
        self.assertRegex(version, r"^\d+\.\d+\.\d+$", f"版本号格式不对: {version}")

    def test_both_scripts_same_version(self):
        """两个脚本读取的版本号应该一致"""
        v1 = deep_skill_search.get_skill_version()
        v2 = deep_skill_install.get_skill_version()
        self.assertEqual(v1, v2, "两个脚本读取的版本号应该一致")

    def test_no_version_field_returns_unknown(self):
        """SKILL.md 无 version 字段时返回 'unknown'"""
        skill_md = Path(__file__).resolve().parent.parent / "SKILL.md"
        original = skill_md.read_text(encoding="utf-8")
        try:
            # 临时删除 version 行
            modified = re.sub(r"version:\s*\"[^\"]+\"\n", "", original)
            skill_md.write_text(modified, encoding="utf-8")
            version = deep_skill_search.get_skill_version()
            self.assertEqual(version, "unknown")
        finally:
            skill_md.write_text(original, encoding="utf-8")

    def test_install_script_no_version_returns_unknown(self):
        """install.py 的 get_skill_version 在无 version 时也返回 'unknown'"""
        skill_md = Path(__file__).resolve().parent.parent / "SKILL.md"
        original = skill_md.read_text(encoding="utf-8")
        try:
            modified = re.sub(r"version:\s*\"[^\"]+\"\n", "", original)
            skill_md.write_text(modified, encoding="utf-8")
            version = deep_skill_install.get_skill_version()
            self.assertEqual(version, "unknown")
        finally:
            skill_md.write_text(original, encoding="utf-8")


class TestCheckVersionCLI(unittest.TestCase):
    """测试 --check-version 命令行参数"""

    def test_check_version_json_output(self):
        """--check-version 输出合法 JSON"""
        import io
        from contextlib import redirect_stdout

        buf = io.StringIO()
        with redirect_stdout(buf):
            deep_skill_search.check_version()
        output = buf.getvalue().strip()
        data = json.loads(output)
        self.assertIn("current_version", data)
        self.assertIn("latest_version", data)
        self.assertIn("update_available", data)

    def test_check_version_current_matches(self):
        """current_version 应该和 SKILL.md 一致"""
        import io
        from contextlib import redirect_stdout

        buf = io.StringIO()
        with redirect_stdout(buf):
            deep_skill_search.check_version()
        data = json.loads(buf.getvalue().strip())
        expected = deep_skill_search.get_skill_version()
        self.assertEqual(data["current_version"], expected)

    def test_check_version_network_failure_graceful(self):
        """网络失败时 latest_version 为 unknown，update_available 为 False"""
        import io
        from contextlib import redirect_stdout

        with patch("deep_skill_search.urllib.request.urlopen", side_effect=Exception("network error")):
            buf = io.StringIO()
            with redirect_stdout(buf):
                deep_skill_search.check_version()
            data = json.loads(buf.getvalue().strip())
            self.assertEqual(data["latest_version"], "unknown")
            self.assertFalse(data["update_available"])


class TestSkillVersionInAPI(unittest.TestCase):
    """测试 skillVersion 参数是否正确附加到 API 请求"""

    def test_search_includes_skill_version(self):
        """搜索请求应包含 skillVersion 参数"""
        captured = {}

        def fake_api_request(endpoint, **kwargs):
            captured["endpoint"] = endpoint
            return {"data": [], "error": False}

        with patch.object(deep_skill_search, "api_request", side_effect=fake_api_request):
            with patch.object(deep_skill_search, "get_client_id", return_value="test"):
                deep_skill_search.search_deep("测试关键词")

        self.assertIn("skillVersion", captured["endpoint"])
        version = deep_skill_search.get_skill_version()
        self.assertIn(f"skillVersion={version}", captured["endpoint"])

    def test_search_no_version_omits_param(self):
        """版本为 unknown 时不附加 skillVersion"""
        captured = {}

        def fake_api_request(endpoint, **kwargs):
            captured["endpoint"] = endpoint
            return {"data": [], "error": False}

        with patch.object(deep_skill_search, "get_skill_version", return_value="unknown"):
            with patch.object(deep_skill_search, "api_request", side_effect=fake_api_request):
                with patch.object(deep_skill_search, "get_client_id", return_value="test"):
                    deep_skill_search.search_deep("测试关键词")

        self.assertNotIn("skillVersion", captured["endpoint"])

    def test_download_includes_skill_version(self):
        """下载请求应包含 skillVersion 参数"""
        captured = {}

        def fake_urlopen(req, **kwargs):
            captured["url"] = req.full_url if hasattr(req, "full_url") else str(req)
            mock_resp = MagicMock()
            mock_resp.read.return_value = b"PK\x03\x04fake-zip"
            mock_resp.__enter__ = MagicMock(return_value=mock_resp)
            mock_resp.__exit__ = MagicMock(return_value=False)
            return mock_resp

        with patch("deep_skill_install.urllib.request.urlopen", side_effect=fake_urlopen):
            with patch.object(deep_skill_install, "get_api_token", return_value=""):
                with patch.object(deep_skill_install, "get_skill_metadata", return_value={}):
                    try:
                        deep_skill_install.download_skill_zip("test-skill")
                    except Exception:
                        pass  # 可能因 fake zip 失败，但 URL 已被捕获

        self.assertIn("skillVersion", captured.get("url", ""))


class TestMainCLI(unittest.TestCase):
    """测试 main() 函数的命令行入口"""

    def test_check_version_flag_exits_early(self):
        """--check-version 触发后不继续执行搜索"""
        with patch("deep_skill_search.check_version") as mock_check:
            with patch("sys.argv", ["deep_skill_search.py", "--check-version"]):
                deep_skill_search.main()
                mock_check.assert_called_once()

    def test_no_query_shows_error(self):
        """无 query 且无 --check-version 时应报错"""
        with patch("sys.argv", ["deep_skill_search.py"]):
            with self.assertRaises(SystemExit):
                deep_skill_search.main()


if __name__ == "__main__":
    unittest.main(verbosity=2)
