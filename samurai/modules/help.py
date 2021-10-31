#Copyright (C) 2021 Axdhu/SamuRai
#
#This file is a part of < https://github.com/Axdhu/SamuRai >
#PLease read the GNU Affero General Public License < https://github.com/Axdhu/SamuRai/blob/main/LICENSE >
#
"""Userbot help command"""

import asyncio

from samurai import CMD_HELP
from samurai.events import register


@register(outgoing=True, pattern=r"\.help(?: |$)(.*)")
async def help(event):
    """For .help command"""
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            msg = await event.edit(str(CMD_HELP[args]))
        else:
            msg = await event.edit("Please specify a valid module name.")
    else:
        string = "Specify which module do you want help for !!\n**Usage:** `.help` <module name>\n\n"
        for i in sorted(CMD_HELP):
            string += "`" + str(i) + "`"
            string += "\t\t\t||\t\t\t "
        msg = await event.edit(string)
    await asyncio.sleep(45)
    try:
        await msg.delete()
    except BaseException:
        return  # just in case if msg deleted first
