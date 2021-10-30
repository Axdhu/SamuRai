#!/usr/bin/env bash
#Copyright (C) 2021 Axdhu/SamuRai
#This file is a part of < https://github.com/Axdhu/SamuRai >
#PLease read the GNU Affero General Public License < https://github.com/Axdhu/SamuRai/blob/main/LICENSE >

clear


while [ $sec -gt 0 ]; do
    echo -ne "\e[33m ${spinner[sec]} Starting dependency installation in $sec seconds...\r"
    sleep 1
    sec=$(($sec - 1))
done
echo -e "\e[1;32mInstalling Dependencies ---------------------------\e[0m\n" # Don't Remove Dashes / Fix it
apt-get update
apt-get upgrade -y
pkg upgrade -y
pkg install python wget -y
wget https://gist.githubusercontent.com/Axdhu/6aec7e5e0e8193e40dbeb586f32e8c7f/raw/bdeb27e542728f546a92e9890c491056eb2f0dc7/ssgen.py
pip install telethon
clear
python3 ssgen.py
