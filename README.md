# rosch (RO's Ssh Config Helper) version 0.0.1

## ABOUT:

rosch is a simple script that adds ssh pub files to the .ssh/authorized_keys folder of a host, and adds an ssh config to your ssh folder. the result is that the process of sshing onto a host is simplified from


  `ssh tocaadmin@123.456.789.000 -p 2222 -> {enter password}`

to

  `ssh mytocahost`

with no password required.

please note that i wrote rosch mostly in my spare time and it has not been extensively tested, so it may have some bugs. i (ro) am the sole maintainer of this script so if you find any bugs please come directly to me (rowan.amber@toca.io and/or roarch@proton.me)

## HOW TO USE: 
there are two rosch modes in which rosch can configure ssh hosts - csv and individual.

### csv mode:
1. in main.py, set use_csv to True.
2. in main.py, set config_path your ssh config file (by default it is set to $HOME/.ssh/config). this is the file that rosch will append to.
3. in main.py, set pem_path and pub_path to the public/private key pair you wish to use. the pem will be added to the host's authorized_keys file, and the pub will be added to your ssh config entry for each host as the Identityfile.
4. create a csv file. the top row should be a list of ssh options for each column. for example:

| Host         |   Hostname    | Port |
|--------------|:-------------:|-----:|
| kiera        | 123.456.789.0 | 2222 |
| johnny       | 456.789.102.3 | 2222 |

for a list of possible options, see <https://www.man7.org/linux/man-pages/man5/ssh_config.5.html>

**host** and **hostname** are ***required*** options.

5. by default, rosch looks for csv files in the script's own directory. place the csv file in the script's directory, or edit the csv_dir directory to be the exact path where your csv is located.
6. run main.py. you will be periodically prompted for the passwords of hosts you are adding public keys to. rosch does not store any of these passwords.

### individual mode:
1. in main.py, set use_csv to False.
2. in main.py, set config_path your ssh config file (by default it is set to $HOME/.ssh/config). this is the file that rosch will append to.
3. in main.py, set pem_path and pub_path to the public/private key pair you wish to use. the pem will be added to the host's authorized_keys file, and the pub will be added to your ssh config entry for each host as the Identityfile.
4. run main.py. the script will prompt you for:
- Host (alias of the host)
- Hostname (ip address or hostname)
- Port (leave blank for 22)
- User (leave blank for root)
5. you will be prompted for the ssh password of the server you are adding a public key to.
6. run the script again for each host you wish to add your ssh key to.
