import os, shlex, subprocess
from pathlib import Path

HOME_PATH = Path.home()


def exec(cmd: str, capture_output: bool = True) -> subprocess.CompletedProcess:
    return subprocess.run(shlex.split(cmd), capture_output=capture_output)


def gitClone(repo: str, saveTo: Path):
    print(f"Cloning repo {repo} to {str(saveTo)}")
    clone_result = exec(f"git clone {repo} {str(saveTo)}")

    if clone_result.returncode == 0:
        print(f"Successfully cloned to {str(saveTo)}")
        return True

    print(f"Error while cloning repo: {clone_result.stderr.decode('utf-8')}")
    return False


def add_apt_packages():
    pkgs = [
        "build-essential",
        "calibre",
        "curl",
        "git",
        "htop",
        "libfuse2",
        "mmv",
        "nodejs",
        "npm",
        "thunderbird",
        "tmux",
        "tree",
        "valgrind",
        "vlc",
    ]
    print("Installing apt packages")
    result = exec("apt-get install -y " + " ".join(pkgs))
    if result.returncode == 0:
        print("Installed apt packages")
        return True
    print(f"Error installing apt packages: {result.stderr.decode('utf-8')}")
    return False


def install_neovim():

    os.mkdir(HOME_PATH.joinpath("apps"))
    repo_is_cloned = gitClone("https://github.com/neovim/neovim", HOME_PATH.joinpath("apps/neovim"))
    if not repo_is_cloned:
        print("Could not install neovim")
        return False
    print("Neovim was installed")
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
set -g status-fg white"""

    with open(HOME_PATH.joinpath(".tmux.conf"), "w", encoding="utf-8") as tmux_file:
        tmux_file.write(content)


def main():
    add_apt_packages()
    install_neovim()


if __name__ == "__main__":
    main()
