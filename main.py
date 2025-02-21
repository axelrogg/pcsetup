from utils import exec
import os
from pathlib import Path


HOME_PATH = Path.home()
CPU_COUNT = os.cpu_count()


def gitClone(repo: str, saveTo: Path):
    clone_result = exec(f"git clone {repo} {str(saveTo)}")
    return clone_result.returncode == 0


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
