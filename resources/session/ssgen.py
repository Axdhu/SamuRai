#!/usr/bin/python3
#Copyright (C) 2021 Axdhu/SamuRai
#This file is a part of < https://github.com/Axdhu/SamuRai >
#PLease read the GNU Affero General Public License < https://github.com/Axdhu/SamuRai/blob/main/LICENSE >
# All rights reserved.

import os
from time import sleep

a = r"""
                                    (_)
 ___  __ _ _ __ ___  _   _ _ __ __ _ _ 
| __|/ _` | '_ ` _ \| | | | '__/ _` | |
|__ \ (_| | | | | | | |_| | | | (_| | |
|___/\__,_|_| |_| |_|\__,_|_|  \__,_|_|
"""


def spinner():
    print("Checking if Telethon is installed...")
    for _ in range(3):
        for frame in r"-\|/-\|/":
            print("\b", frame, sep="", end="", flush=True)
            sleep(0.1)


def clear_screen():
    
    if os.name == "posix":
        os.system("clear")
    else:
        # for windows platfrom
        os.system("cls")


def get_api_id_and_hash():
    print(
        "Get your API ID and API HASH from my.telegram.org  to proceed.\n\n",
    )
    try:
        API_ID = int(input("Please enter your API ID: "))
    except ValueError:
        print("APP ID must be an integer.\nQuitting...")
        exit(0)
    API_HASH = input("Please enter your API HASH: ")
    return API_ID, API_HASH


def telethon_session():
    try:
        spinner()

        x = "\bFound an existing installation of Telethon...\nSuccessfully Imported.\n\n"
    except BaseException:
        print("Installing Telethon...")
        os.system("pip install -U telethon")

        x = "\bDone. Installed and imported Telethon."
    clear_screen()
    print(a)
    print(x)

    # the imports

    from telethon.errors.rpcerrorlist import ApiIdInvalidError, PhoneNumberInvalidError
    from telethon.sessions import StringSession
    from telethon.sync import TelegramClient

    API_ID, API_HASH = get_api_id_and_hash()

    # logging in
    try:
        with TelegramClient(StringSession(), API_ID, API_HASH) as SamuRai:
            print("Generating a user session for SamuRai...")
            ult = SamuRai.send_message(
                "me",
                f"**SamuRai** `SESSION`:\n\n`{SamuRai.session.save()}`\n\n**Do not share this anywhere!**",
            )
            print(
                "Your SESSION has been generated. Check your telegram saved messages!"
            )
            exit(0)
    except ApiIdInvalidError:
        print(
            "Your API ID/API HASH combination is invalid. Kindly recheck.\nQuitting..."
        )
        exit(0)
    except ValueError:
        print("API HASH must not be empty!\nQuitting...")
        exit(0)
    except PhoneNumberInvalidError:
        print("The phone number is invalid!\nQuitting...")
        exit(0)


def main():
    clear_screen()
    print(a)
    telethon_session()
    x = input("Run again? (y/n")
    if x == "y":
        main()
    else:
        exit(0)


main()
