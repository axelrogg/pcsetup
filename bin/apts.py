#!/usr/bin/python3

import sys
import os

# Get the project root (one level up from the 'bin' directory)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


from src.utils import exec


def add_apt_repos():
    repos = [
        "ppa:fish-shell/release-3",
    ]
    for repo in repos:
        result = exec(f"apt-add-repository {repo} -y")
        if result.returncode != 0:
            if "must run as root" in result.stdout:
                print("To add a ppa you must run the script as root.")
            else:
                print(result)
            return False
    return True


def add_apt_packages():
    pkgs = [
        "build-essential",
        "ca-certificates",
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
    exec(f"apt-get install -y {' '.join(pkgs)}")


def main():
    add_apt_repos()
    add_apt_packages()


if __name__ == "__main__":
    main()
