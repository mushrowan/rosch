import subprocess
import shlex


class Host:
    def __init__(self, alias, hostname, path_to_pem, path_to_pub, port=22, user="root"):
        self.hostname = hostname
        self.alias = alias
        self.port = port
        self.user = user
        self.path_to_pem = path_to_pem  # This will be shared between all hosts so maybe class attribute
        self.path_to_pub = path_to_pub  # This will be shared between all hosts so maybe class attribute

    def addAliasToSSHConfig(self, path_to_config="$HOME/.ssh/config"):
        print(
            "Appending new server config to ssh config..."
        )  # It may be better to do this in the main function because this will continuously open and close the config
        with open(path_to_config, "a") as ssh_config:
            print(f"Checking if alias {self.alias} exists in {path_to_config}...")
            print(
                f"Appending SSH alias {self.alias} for {self.hostname} to local SSH config..."
            )
            ssh_config.write(
                f"""Host {self.alias}
            Hostname {self.hostname}
            Port {self.port}
            User {self.user}
            Identityfile {self.path_to_pub}"""
            )
            # except FileNotFoundError: # Should we do this in the main function?
            print("fuck")

    def copyIDToServer(self):
        print(
            f"Adding SSH public key {self.path_to_pub} to {self.user}@{self.hostname} on port {self.port}"
        )

        args = shlex.split(
            f"ssh-copy-id -i {self.path_to_pub} -p {self.port} {self.user}@{self.hostname}"
        )
        subprocess.run(args)
