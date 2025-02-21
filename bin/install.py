#!/usr/bin/python3

import sys
import os

# Get the project root (one level up from the 'bin' directory)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


from src.utils import exec


def install_docker():
    result = exec("install -m 0755 -d /etc/apt/keyrings")
    print(result)
    result = exec("curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc")
    print(result)
    result = exec("chmod a+r /etc/apt/keyrings/docker.asc")
    print(result)
    result = exec('echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null')
    print(result)
    result = exec("apt apt-update -y")
    print(result)
    result = exec("apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin -y")
    print(result)
    result = exec("groupadd docker")
    print(result)
    result = exec("usermod -aG docker $USER")
    print(result)


def main():
    install_docker()


if __name__ == "__main__":
    main()
