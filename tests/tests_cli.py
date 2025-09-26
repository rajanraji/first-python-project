import subprocess
import sys

def test_cli_hello_runs():
    result = subprocess.run([sys.executable, "-m", "fpp.cli", "hello"], capture_output=True, text=True)
    assert result.returncode == 0
    assert "scaffold is working" in result.stdout or "scaffold is working" in result.stderr
