#!/usr/bin/python
import subprocess
import shlex
from host import Host


print("Welcome to Ro's SSH Config Helper!")
print("Checking configuration file for environment variables...")
# TODO: read configuration file

# Following is temp code which should eventually be moved to the config file?
pem_path = "/home/ro/.ssh/roarch.pem"
ssh_path = "/home/ro/.ssh/config"

print("Initialising list of hosts...")
# TODO: Initialise list of host objects from the class file.
host_list = []

# test host list for debugging
test_host = Host("141.147.86.138")
test_host.set_user("ro")
test_host.set_port("22")
host_list.append(test_host)
print("Copying public keys to each host in the host list...")
for host in host_list:
    print(
        "Adding SSH key to %s@%s on port %s..." % (host.user, host.hostname, host.port)
    )

    args = shlex.split(
        f"ssh-copy-id -i {pem_path} -p {host.port} {host.user}@{host.hostname}"
    )
    proc = subprocess.run(args)
# expected output is "{host.user}@{host.hostname}'s password"
# in order to input passwords automatically, sshpass is required - optional dependency
# TODO Append aliases to the ssh config
print("Appending new server configs to ssh config...")
