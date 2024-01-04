import subprocess
import shlex
from pathlib import Path


class Host:
    path_to_pem = ""
    path_to_pub = ""
    path_to_config = f"{Path.home()}/.ssh/config"

    def __init__(self, alias, hostname, port="22", user="root"):
        self.hostname = hostname
        self.alias = alias
        self.port = port
        self.user = user

    def add_alias_to_ssh_config(self, ssh_config):
        print(
            "Appending new server config to ssh config..."
        )  # It may be better to do this in the main function because this will continuously open and close the config
        print(f"Checking if alias {self.alias} exists in {Host.path_to_config}...")
        print(
            f"Appending SSH alias {self.alias} for {self.hostname} to local SSH config..."
        )
        ssh_config.write(
            f"""Host {self.alias}
    Hostname {self.hostname}
    Port {self.port}
    User {self.user}
    Identityfile {Host.path_to_pub}"""
        )

    def copy_publickey_to_server(self):
        print(
            f"Adding SSH public key {Host.path_to_pub} to {self.user}@{self.hostname} on port {self.port}"
        )

        args = shlex.split(
            f"ssh-copy-id -i {Host.path_to_pub} -p {self.port} {self.user}@{self.hostname}"
        )
        subprocess.run(args)
