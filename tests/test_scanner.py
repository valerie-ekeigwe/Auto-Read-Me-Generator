from pathlib import Path
from src.scanner import scan_project

def test_scanner_detects_python(tmp_path: Path):
    (tmp_path / "requirements.txt").write_text("jinja2\n", encoding="utf-8")
    (tmp_path / "example.py").write_text("print('ok')", encoding="utf-8")
    result = scan_project(tmp_path)
    assert "Python" in result["tech_stack"]

