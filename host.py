import subprocess
import shlex


class Host:
    def __init__(self, alias, hostname, path_to_pem, port=22, user="root"):
        self.hostname = hostname
        self.alias = alias
        self.port = port
        self.user = user
        self.path_to_pem = path_to_pem

    def copyIDToServer(self, path_to_pem):
        print(
            f"Adding SSH key {path_to_pem} to {self.user}@{self.hostname} on port {self.port}"
        )

        args = shlex.split(
            f"ssh-copy-id -i {path_to_pem} -p {self.port} {self.user}@{self.hostname}"
        )
        subprocess.run(args)

    def addAliasToSSHConfig(self, path_to_config="$HOME/.ssh/config"):
        print("Appending new server configs to ssh config...")
        with open(path_to_config, "a") as ssh_config:
            for host in host_list:
                print(
                    f"Appending SSH alias {host.alias} for {host.hostname} to local SSH config..."
                )
                ssh_config.write(
                    f"""Host {host.alias}
            Hostname {host.hostname}
            Port {host.port}
            User {host.user}
            Identityfile {pem_path}"""
                )
