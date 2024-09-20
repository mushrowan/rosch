#!/usr/bin/env python3
from SSHost import SSHost
from hostcsv import HostCsv
from pathlib import Path
from subprocess import CalledProcessError


# print("Checking configuration file for environment variables...")
# TODO: read configuration file

use_csv = False
pem_path = Path("/home/rowan/.ssh/rotoca.pem")
config_path = Path("/home/rowan/.ssh/config")
pub_path = Path("/home/rowan/.ssh/rotoca.pem.pub")
csv_dir = list(Path(".").glob("*.csv"))
if len(csv_dir) > 0:
    print(
        """rosch has detected csv files in the current directory.\n
If these csv files are formatted in the correct way, they can be used to configure SSH hosts in bulk.
"""
    )
    print("The following csvs were detected:")
    [print(path) for path in csv_dir]


def main():
    print("Welcome to Ro's SSH Config Helper!")
    host_list = []
    with open(config_path, "a+", encoding="utf-8") as config:
        config.write("\n######### Ro's SSH Config Helper Start ########\n")
        if use_csv is True:
            for csv_path in csv_dir:
                host_csv = HostCsv(csv_path).write_csv()
                host_count = 0
                for dictionary in host_csv:
                    host_list.append(SSHost(dictionary, str(pem_path)))
                    host_count += 1
                print(f"Detected {str(host_count)} in {csv_path}.")
            for host in host_list:
                host.check_required_keys()
                host.copy_publickey_to_server(str(pub_path))
                try:
                    host.add_alias_to_ssh_config(config)
                except ValueError:
                    print(f"{host.dictionary['Host']} is already in the Config file.")
                    print("Skipping...")
        else:
            print("Reading Host information from user input.")
            userhost_dict = dict()
            userhost_dict.update({"Host": input("Input host alias: ")})
            userhost_dict.update({"Hostname": input("Input Hostname: ")})
            userhost_dict.update(
                {"User": input("Input username (leave blank for root)")}
            )
            userhost_dict.update({"Port": input("Input port (leave blank for 22): ")})
            if userhost_dict["Port"] == "":
                userhost_dict["Port"] = "22"
            if userhost_dict["User"] == "":
                userhost_dict["User"] = "root"
            userhost = SSHost(userhost_dict, str(pem_path))
            try:
                userhost.copy_publickey_to_server(str(pub_path))
                userhost.add_alias_to_ssh_config(config)
            except CalledProcessError:
                print(
                    "Something went wrong with copying the public key to the server. Skipping..."
                )

        config.write("\n######### Ro's SSH Config Helper End ########\n")


main()
