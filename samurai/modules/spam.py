#Copyright (C) 2021 Axdhu/SamuRai
#
#This file is a part of < https://github.com/Axdhu/SamuRai >
#PLease read the GNU Affero General Public License < https://github.com/Axdhu/SamuRai/blob/main/LICENSE >
#

import asyncio
from asyncio import sleep

from samurai import BOTLOG_CHATID, CMD_HELP
from samurai.events import register


@register(outgoing=True, pattern=r"\.cspam (.*)")
async def leter_spam(cspammer):
    cspam = str(cspammer.pattern_match.group(1))
    message = cspam.replace(" ", "")
    await cspammer.delete()
    for letter in message:
        await cspammer.respond(letter)
    if BOTLOG_CHATID:
        await cspammer.client.send_message(
            BOTLOG_CHATID, "#CSPAM\n"
            "TSpam was executed successfully")


@register(outgoing=True, pattern=r"\.wspam (.*)")
async def word_spam(wspammer):
    wspam = str(wspammer.pattern_match.group(1))
    message = wspam.split()
    await wspammer.delete()
    for word in message:
        await wspammer.respond(word)
    if BOTLOG_CHATID:
        await wspammer.client.send_message(
            BOTLOG_CHATID, "#WSPAM\n"
            "WSpam was executed successfully")


@register(outgoing=True, pattern=r"\.spam (.*)")
async def spammer(spamm):
    counter = int(spamm.pattern_match.group(1).split(' ', 1)[0])
    spam_message = str(spamm.pattern_match.group(1).split(' ', 1)[1])
    await spamm.delete()
    await asyncio.wait([spamm.respond(spam_message) for i in range(counter)])
    if BOTLOG_CHATID:
        await spamm.client.send_message(BOTLOG_CHATID, "#SPAM\n"
                                        "Spam was executed successfully")


@register(outgoing=True, pattern=r"\.picspam")
async def tiny_pic_spam(pspam):
    message = pspam.text
    text = message.split()
    counter = int(text[1])
    link = str(text[2])
    await pspam.delete()
    for _ in range(1, counter):
        await pspam.client.send_file(pspam.chat_id, link)
    if BOTLOG_CHATID:
        await pspam.client.send_message(
            BOTLOG_CHATID, "#PICSPAM\n"
            "PicSpam was executed successfully")


@register(outgoing=True, pattern=r"\.delayspam (.*)")
async def dspammer(dspam):
    spamDelay = float(dspam.pattern_match.group(1).split(' ', 2)[0])
    counter = int(dspam.pattern_match.group(1).split(' ', 2)[1])
    spam_message = str(dspam.pattern_match.group(1).split(' ', 2)[2])
    await dspam.delete()
    for _ in range(1, counter):
        await dspam.respond(spam_message)
        await sleep(spamDelay)
    if BOTLOG_CHATID:
        await dspam.client.send_message(
            BOTLOG_CHATID, "#DelaySPAM\n"
            "DelaySpam was executed successfully")


CMD_HELP.update({
    "spam":
    "`.cspam` <text>"
    "\nUsage: Spam the text letter by letter."
    "\n\n`.spam` <count> <text>"
    "\nUsage: Floods text in the chat !!"
    "\n\n`.wspam` <text>"
    "\nUsage: Spam the text word by word."
    "\n\n`.picspam` <count> <link to image/gif>"
    "\nUsage: As if text spam was not enough !!"
    "\n\n`.delayspam` <delay> <count> <text>"
    "\nUsage: .bigspam but with custom delay."
    "\n\n\nNOTE : Spam at your own risk !!"
})
