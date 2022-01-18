# Module: log
# Description: Turns on of off logs in chat. Also can be used to retrieve Chimera execution logs
# Usage: !log [off|on] | [show] [date (format: YYYY-MM-DD)]
# Dependencies: logging, datetime

import configs, discord
from datetime import datetime
from lib.helpers import Logger
from lib.reco_embeds import recoEmbeds as rm



async def log(ctx, param, date=None):
    p=configs.BOT_PREFIX
    if param == "on":
        configs.discord_logs_enabled = True
        await rm.msg(ctx,"**Exceptions log will now be displayed in chat.**")
    elif param == "off":
        configs.discord_logs_enabled = False
        await rm.msg(ctx,"**Running on silent mode now.**")
    elif param == "show":
        date = date if date else (datetime.now()).strftime('%Y-%m-%d')
        await ctx.send(file=discord.File('{}/{}.txt'.format(Logger.DIRECTORY, date)))
    else:
        await rm.msg(ctx,f'''**Help - {p}log**\n
**Commands**:!
```{p}log on
{p}log off
{p}log show
{p}log show YYYY-MM-DD```''')
