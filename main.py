import os, shlex, subprocess
from pathlib import Path

HOME_PATH = Path.home()


def exec(cmd: str, capture_output: bool = True) -> subprocess.CompletedProcess:
    return subprocess.run(shlex.split(cmd), capture_output=capture_output)

def append_to_profile():
    screen = """#Added for my very old slot machine monitor
xrandr --newmode "1920x1080_60.00"  172.80  1920 2040 2248 2576  1080 1081 1084 1118  -HSync +Vsync
xrandr --addmode DP-1 "1920x1080_60.00"
xrandr --addmode eDP-1 "1920x1080_60.00"
"""


def gitClone(repo: str, saveTo: Path):
    print(f"Cloning repo {repo} to {str(saveTo)}")
    clone_result = exec(f"git clone {repo} {str(saveTo)}")

    if clone_result.returncode == 0:
        print(f"Successfully cloned to {str(saveTo)}")
        return True

    print(f"Error while cloning repo: {clone_result.stderr.decode('utf-8')}")
    return False

def add_apt_repos():
    repos = [
        "sudo apt-add-repository ppa:fish-shell/release-3 -y",
    ]
    for repo in repos:
        result = exec(repo)
        if result.returncode != 0:
            print(result)
            return False


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
    return exec("sudo apt-get install -y " + " ".join(pkgs))


def install_neovim():
    repo_is_cloned = gitClone("https://github.com/neovim/neovim", HOME_PATH.joinpath("apps/neovim"))
    if not repo_is_cloned:
        return False
    exec("cd neovim && git checkout stable && make CMAKE_BUILD_TYPE=RelWithDebInfo")
    result = exec("sudo make install")
    print(result)
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
    print("Installing apt packages")
    result = add_apt_packages()
    print(result)
    if result.returncode == 0:
        print("All apt packages were installed")
    else:
        print(result)

    print("Installing Neovim")
    install_neovim()


if __name__ == "__main__":
    main()
