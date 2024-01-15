#!/usr/bin/python3
import shlex
import subprocess


class Host:
    def __init__(self, csv_dictionary: dict, path_to_pem=""):
        self.dictionary = {"User": "root"}
        self.dictionary.update({"Identityfile": path_to_pem, "Port": "22"})
        self.dictionary.update(csv_dictionary)

    def check_required_keys(self):
        if "Host" not in self.dictionary or self.dictionary["Host"] == "":
            raise KeyError(
                """You have not included a Host (address) for one of your
                hosts. Please make sure that there is a Host column and that
                every row is filled."""
            )
        if "Hostname" not in self.dictionary or self.dictionary["Hostname"] == "":
            raise KeyError(
                """You have not included a Hostname (alias) for one of your 
                hosts. Please make sure there is a Hostname column and every
                row is filled."""
            )

    def add_alias_to_ssh_config(self, ssh_config, tab="  "):
        print("Appending new server config to ssh config...")
        # TODO: Add checking for if an alias already exists in the ssh config
        print(f"Checking if alias {self.dictionary["Host"]} exists in SSH config...")
        if self.dictionary["Host"] in ssh_config.read():
            raise ValueError(
                f"""Host {self.dictionary["Host"]} is already present in your
                SSH config file. Please either choose a different alias for
                the host you are trying to add or delete/rename the entry in
                your SSH config."""
            )
        ssh_config.write(f"Host {self.dictionary["Host"]}")
        for key, value in self.dictionary.items():
            if key != "Host":
                ssh_config.write(f"{tab}{key} {value}")

    def copy_publickey_to_server(self, public_key):
        print(
            f"Adding SSH public key {public_key} to {self.dictionary["User"]}@{self.dictionary["Hostname"]} on port {self.dictionary["Port"]}"
        )

        args = shlex.split(
            f"ssh-copy-id -i {self.dictionary["Identityfile"]} -p {self.dictionary["Port"]} {self.dictionary["User"]}@{self.dictionary["Hostname"]}"
        )
        subprocess.run(args)
