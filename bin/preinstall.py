#!/usr/bin/python3

import sys
import os

# Get the project root (one level up from the 'bin' directory)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


from src.utils import CPU_COUNT, HOME_PATH, exec, gitclone


def exec_in_neovim_path(cmd: str):
    return exec(cmd, cwd=HOME_PATH.joinpath("apps/neovim"))


def install_neovim():
    cloned = gitclone(
        "https://github.com/neovim/neovim",
        HOME_PATH.joinpath("apps/neovim")
    )

    if not cloned:
        return False
    exec_in_neovim_path("git checkout stable")
    exec_in_neovim_path(f"make -j {CPU_COUNT} CMAKE_BUILD_TYPE=RelWithDebInfo")
    exec_in_neovim_path("cd build && cpack -G DEB && dpkg -i nvim-linux64.deb")
    return True


def main():
    install_neovim()

if __name__ == "__main__":
    main()
