import os
import shlex, subprocess
from pathlib import Path


HOME_PATH = Path.home()
CPU_COUNT = os.cpu_count()


def exec(cmd: str, capture_output: bool = True, cwd: Path | None = None) -> subprocess.CompletedProcess:
    if cwd:
        return subprocess.run(shlex.split(cmd), capture_output=capture_output, text=True, cwd=cwd)
    return subprocess.run(shlex.split(cmd), capture_output=capture_output, text=True)


def append_to_profile():
    screen = """#Added for my very old slot machine monitor
xrandr --newmode "1920x1080_60.00"  172.80  1920 2040 2248 2576  1080 1081 1084 1118  -HSync +Vsync
xrandr --addmode DP-1 "1920x1080_60.00"
xrandr --addmode eDP-1 "1920x1080_60.00"
"""


def gitClone(repo: str, saveTo: Path):
    clone_result = exec(f"git clone {repo} {str(saveTo)}")
    if clone_result.returncode == 0:
        return True
    return False


def add_apt_repos():
    repos = [
        "ppa:fish-shell/release-3",
    ]
    for repo in repos:
        print(f"info: adding repository {repo}")
        result = exec(f"sudo apt-add-repository {repo} -y")
        if result.returncode != 0:
            print(result)
            return False
    return True


def add_apt_packages():
    pkgs = [
        "build-essential",
        "calibre",
        "cmake",
        "curl",
        "gettext",
        "htop",
        "libfuse2",
        "mmv",
        "ninja-build",
        "nodejs",
        "npm",
        "postgresql",
        "thunderbird",
        "tmux",
        "tree",
        "unzip",
        "valgrind",
        "vlc",
    ]
    for pkg in pkgs:
        print(f"info: installing {pkg}")
        exec(f"sudo apt-get install -y {pkg}")


def install_neovim():
    def exec_in_neovim_path(cmd: str):
        return exec(cmd, cwd=HOME_PATH.joinpath("apps/neovim"))

    print(
        f"info: cloning github.com/neovim/neovim to \
        {HOME_PATH.joinpath('apps/neovim')}"
    )
    repo_is_cloned = gitClone(
        "https://github.com/neovim/neovim",
        HOME_PATH.joinpath("apps/neovim")
    )

    if not repo_is_cloned:
        return False
    exec_in_neovim_path(
        f"git checkout stable && make -j {CPU_COUNT} \
        CMAKE_BUILD_TYPE=RelWithDebInfo"
    )
    exec_in_neovim_path("git checkout stable")
    exec_in_neovim_path("sudo make install")
    return True


def create_tmux_conf():
    content = """# remap prefix from 'C-b' to 'C-a'
unbind C-b
set-option -g prefix C-a
bind-key C-a send-prefix

# Enable mouse navigation
set -g mouse on

# Increase the history buffer
set-option -g history-limit 5000

# Change status bar color
set -g default-terminal "screen-256color"
set -g status-bg black
set -g status-fg white
"""

    with open(HOME_PATH.joinpath(".tmux.conf"), "w", encoding="utf-8") as file:
        file.write(content)


def main():
    install_neovim()

if __name__ == "__main__":
    main()
