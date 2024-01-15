#!/usr/bin/python3
from host import Host


print("Welcome to Ro's SSH Config Helper!")
# print("Checking configuration file for environment variables...")
# TODO: read configuration file

path_to_pem = "/home/ro/.ssh/roarch.pem"
path_to_config = "/home/ro/.sh/config"
path_to_pub = "/home/ro/.ssh/roarch.pem.pub"
bro = Host(:
)
print("Initialising list of hosts...")
# TODO: Initialise list of host objects from the csv file.
test_host = Host("testdel", "0.0.0.0")  # test host
print(test_host.path_to_pub)
host_list = []
host_list.append(test_host)
print(f"Opening SSH config file located at {Host.path_to_config}")
try:
    with open(Host.path_to_config, "a") as ssh_config:
        for host in host_list:
            print(
                f"Appending {host.hostname}:{host.port} to SSH config with the alias {host.alias}"
            )
            host.add_alias_to_ssh_config(ssh_config)
            host.copy_publickey_to_server()

except FileNotFoundError:
    print(
        "ERROR: Unable to access the ssh config file. Perhaps you do not have permissions or the parent directories do not exist?"
    )
# test host list for debugging
print("Copying public keys to each host in the host list...")
# expected output is "{host.user}@{host.hostname}'s password"
# in order to input passwords automatically, sshpass is required - optional dependency
# TODO Append aliases to the ssh config
