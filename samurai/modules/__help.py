#Copyright (C) 2021 Axdhu/SamuRai
#
#This file is a part of < https://github.com/Axdhu/SamuRai >
#PLease read the GNU Affero General Public License < https://github.com/Axdhu/SamuRai/blob/main/LICENSE >
#
# All rights reserved.
# Thanks @Spechide.

import logging

from samurai import BOT_USERNAME, BOT_TOKEN
from samurai.events import register
from telethon.errors.rpcerrorlist import BotInlineDisabledError

logging.basicConfig(
    format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
    level=logging.WARNING)


@register(outgoing=True, pattern=r"\.helpme")
async def yardim(event):
    tgbotusername = BOT_USERNAME
    if tgbotusername and BOT_TOKEN:
        try:
            results = await event.client.inline_query(
                tgbotusername,
                "@AAXDHU"
            )
        except BotInlineDisabledError:
            return await event.edit("`Bot can't be used in inline mode.\nMake sure to turn on inline mode!`")
        await results[0].click(
            event.chat_id,
            reply_to=event.reply_to_msg_id,
            hide_via=True
        )
        await event.delete()
    else:
        return await event.edit("`The bot doesn't work! Please set the Bot Token and Username correctly.`"
                                "\n`The module has been stopped.`")
