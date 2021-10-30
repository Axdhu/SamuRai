#!/usr/bin/env bash
#Copyright (C) 2021 Axdhu/SamuRai
#This file is a part of < https://github.com/Axdhu/SamuRai >
#PLease read the GNU Affero General Public License < https://github.com/Axdhu/SamuRai/blob/main/LICENSE >

clear
echo -e "\e[1m"
echo "                                     _  "
echo "                                    (_) "
echo "  ___  __ _ _ __ ___  _   _ _ __ __ _ _ "
echo " / __|/ _` | '_ ` _ \| | | | '__/ _` | |"
echo " \__ \ (_| | | | | | | |_| | | | (_| | |"
echo " |___/\__,_|_| |_| |_|\__,_|_|  \__,_|_|"
echo -e "\e[0m"
sec=5
spinner=(⣻ ⢿ ⡿ ⣟ ⣯ ⣷)
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
wget https://gist.githubusercontent.com/Axdhu/31401867c30e2f8fa77ad16521df0aab/raw/45e00d9a84ed94c47bb7d5942992634fafaca749/ssgen.py
pip install telethon
clear
python3 ssgen.py
