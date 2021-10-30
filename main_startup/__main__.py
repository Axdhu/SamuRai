
import logging
import os
import platform

import telethon
from telethon import __version__
from bot_utils_files.Localization.engine import Engine
from database.localdb import check_lang
from main_startup import (
    samurai,
    samurai2,
    samurai3,
    samurai4,
    bot,
    friday_version,
    mongo_client,
)
from main_startup.core.startup_helpers import (
    load_plugin,
    load_xtra_mod,
    plugin_collecter,
    run_cmd,
    update_it
)

from .config_var import Config


async def mongo_check():
    """Check Mongo Client"""
    try:
        await mongo_client.server_info()
    except BaseException as e:
        logging.error("Something Isn't Right With Mongo! Please Check Your URL")
        logging.error(str(e))
        quit(1)


async def load_unofficial_modules():
    """Load Extra Plugins."""
    logging.info("Loading X-Tra Plugins!")
    await run_cmd(f'bash bot_utils_files/other_helpers/xtra_plugins.sh {Config.XTRA_PLUGINS_REPO}')
    xtra_mods = plugin_collecter("./xtraplugins/")
    for mods in xtra_mods:
        try:
            load_xtra_mod(mods)
        except Exception as e:
            logging.error(
                "[USER][XTRA-PLUGINS] - Failed To Load : " + f"{mods} - {str(e)}"
            )


async def fetch_plugins_from_channel():
    """Fetch Plugins From Channel"""
    try:
        async for message in Friday.search_messages(
            Config.PLUGIN_CHANNEL, filter="document", query=".py"
        ):
            hmm = message.document.file_name
            if not os.path.exists(os.path.join("./plugins/", hmm)):
                await Friday.download_media(message, file_name="./plugins/")
    except BaseException as e:
        logging.error(f"Failed! To Install Plugins From Plugin Channel Due To {e}!")
        return
    logging.info("All Plugins From Plugin Channel Loaded!")


async def run_bot():
    try:
        await update_it()
    except:
        pass
    """Run The Bot"""
    await mongo_check()
    if bot:
        await bot.start()
        bot.me = await bot.get_me()
        assistant_mods = plugin_collecter("./assistant/")
        for mods in assistant_mods:
            try:
                load_plugin(mods, assistant=True)
            except Exception as e:
                logging.error("[ASSISTANT] - Failed To Load : " + f"{mods} - {str(e)}")
    await samurai.start()
    samurai.me = await samurai.get_me()
    samurai.selected_lang = await check_lang()
    LangEngine = Engine()
    LangEngine.load_language()
    samurai.has_a_bot = bool(bot)
    if samurai2:
        await samurai2.start()
        samurai2.me = await samurai2.get_me()
        samurai2.has_a_bot = True if bot else False
    if samurai3:
        await samurai3.start()
        samurai3.me = await samurai3.get_me()
        samurai3.has_a_bot = bool(bot)
    if samurai4:
        await samurai4.start()
        samurai4.me = await samurai4.get_me()
        samurai4.has_a_bot = bool(bot)
    if Config.PLUGIN_CHANNEL:
        await fetch_plugins_from_channel()
    needed_mods = plugin_collecter("./plugins/")
    for nm in needed_mods:
        try:
            load_plugin(nm)
        except Exception as e:
            logging.error("[USER] - Failed To Load : " + f"{nm} - {str(e)}")
    if Config.LOAD_UNOFFICIAL_PLUGINS:
        await load_unofficial_modules()
    full_info = f"""Friday Based On Pyrogram V{__version__}
Python Version : {platform.python_version()}
samurai Version : {samurai_version}
You Can Visit @samuraiSupportOfficial For Updates And @samuraibotChat For Any Query / Help!
"""
    logging.info(full_info)
    await telethon.idle()


if __name__ == "__main__":
    samurai.loop.run_until_complete(run_bot())
