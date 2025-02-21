import os, shlex, subprocess
from pathlib import Path


HOME_PATH = Path.home()
CPU_COUNT = os.cpu_count()


def exec(cmd: str, capture_output: bool = True, cwd: Path | None = None) -> subprocess.CompletedProcess:
    if cwd:
        return subprocess.run(shlex.split(cmd), capture_output=capture_output, text=True, cwd=cwd)
    return subprocess.run(shlex.split(cmd), capture_output=capture_output, text=True)


def gitclone(repo: str, saveTo: Path):
    clone_result = exec(f"git clone {repo} {str(saveTo)}")
    return clone_result.returncode == 0

