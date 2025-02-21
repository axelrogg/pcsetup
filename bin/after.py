#!/usr/bin/python3

import sys
import os

# Get the project root (one level up from the 'bin' directory)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


from src.utils import HOME_PATH

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
    create_tmux_conf()

if __name__ == "__main__":
    main()
