#Copyright (C) 2021 Axdhu/SamuRai
#This file is a part of < https://github.com/Axdhu/SamuRai >
#PLease read the GNU Affero General Public License < https://github.com/Axdhu/SamuRai/blob/main/LICENSE >
# All rights reserved.

import logging
import os

from geopy.geocoders import Nominatim

from main_startup.core.decorators import friday_on_cmd
from main_startup.helper_func.basic_helpers import edit_or_reply, get_text

GMAPS_LOC = "https://maps.googleapis.com/maps/api/geocode/json"


@friday_on_cmd(
    ["gps"],
    cmd_help={
        "help": "Find and send the given location",
        "example": "{ch}gps <text>",
    },
)
async def gps(client, message):
    engine = message.Engine
    pablo = await edit_or_reply(message, engine.get_string("PROCESSING"))
    args = get_text(message)
    if not args:
        await pablo.edit(engine.get_string("INPUT_REQ").format("Location"))
        return
    try:
        geolocator = Nominatim(user_agent="FridayUB")
        location = args
        geoloc = geolocator.geocode(location)
        longitude = geoloc.longitude
        latitude = geoloc.latitude
    except Exception as e:
        logging.info(e)
        await pablo.edit(engine.get_string("GPS_2"))
        return
    gm = "https://www.google.com/maps/search/{},{}".format(latitude, longitude)
    await client.send_location(message.chat.id, float(latitude), float(longitude))
    await pablo.reply(
        "Open with: [Google Maps]({})".format(gm),
        disable_web_page_preview=False,
    )
    await pablo.delete()
