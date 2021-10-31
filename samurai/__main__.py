#Copyright (C) 2021 Axdhu/SamuRai
#
#This file is a part of < https://github.com/Axdhu/SamuRai >
#PLease read the GNU Affero General Public License < https://github.com/Axdhu/SamuRai/blob/main/LICENSE >
#
# All rights reserved.

"""Userbot start point"""

from importlib import import_module
from sys import argv

from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
from samurai import LOGS, bot, BOTLOG_CHATID
from samurai.modules import ALL_MODULES


INVALID_PH = '\nERROR: The Phone No. entered is INVALID' \
             '\n Tip: Use Country Code along with number.' \
             '\n or check your phone number and try again !'

try:
    bot.start()
except PhoneNumberInvalidError:
    print(INVALID_PH)
    exit(1)

for module_name in ALL_MODULES:
    imported_module = import_module("userbot.modules." + module_name)

LOGS.info(
    "Congratulations, your userbot is now running !!"
    "Test it by type .on or .alive in any chat."
    "for further assistance, head to https://t.me/AAXDHU")

if not BOTLOG_CHATID:
    LOGS.warning(
        "Yout BOTLOG_CHATID isn't set yet."
        "this variable is highly recomended to fill to make sure"
        "all errors go to your log chat not current chat and considered as a spammer.")


if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
