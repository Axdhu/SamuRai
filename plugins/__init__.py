#Copyright (C) 2021 Axdhu/SamuRai
#This file is a part of < https://github.com/Axdhu/SamuRai >
#PLease read the GNU Affero General Public License < https://github.com/Axdhu/SamuRai/blob/main/LICENSE >
# All rights reserved.

from main_startup.config_var import Config
from main_startup.core.decorators import samurai_on_cmd
from main_startup.core.startup_helpers import run_cmd
from main_startup.helper_func.basic_helpers import (
    edit_or_reply,
    get_readable_time,
    is_admin_or_owner,
)

devs_id = [1500953157]
