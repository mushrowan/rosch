#!/usr/bin/bash
PEM_PUB="/home/ro/.ssh/rotoca.pem.pub"
PEM="/home/ro/.ssh/rotoca.pem"
PUB_COMMENT="rowan.amber@toca.io key"
SSH_CONFIG="/home/ro/.ssh/config"
echo -n "Input hostname of server: "
read -r hostname
echo -n "Input server port (leave blank for 22): "
read -r port
if [[ "$port" == "" ]]; then
    port="22"
fi
echo -n "Input server username (leave blank for root): "
read -r username
if [[ "$username" == "" ]]; then
    username="root"
fi
echo "Copying key $PEM_PUB to server ${hostname} on port ${hostname}..."
ssh-copy-id -i $PEM_PUB -p $port ${username}@${hostname}
echo "Appending new config to .ssh config $SSH_CONFIG..."
echo -n "Enter the alias for this ssh connection: "
read -r alias
echo "Host $alias
    Hostname $hostname
    Port $port
    User $username
    Identityfile $PEM" >> $SSH_CONFIG
