from pathlib import Path
import subprocess
import sys

def test_cli_dry_run(tmp_path: Path):
    repo = Path.cwd()
    cmd = [sys.executable, "-m", "src.cli", "--repo", str(repo), "--template", "minimal", "--dry-run"]
    out = subprocess.run(cmd, capture_output=True, text=True, check=True)
    assert "# " in out.stdout

