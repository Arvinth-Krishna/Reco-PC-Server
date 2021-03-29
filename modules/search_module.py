# Module: search
# Description: Your query will be searched on Google.
# Usage: !search or !search query
# Dependencies: time, os

import os, time, asyncio, configs


async def search(ctx, txt):

    if configs.operating_sys == "Windows":
        os.system("start https://www.google.com/search?q={0}".format(txt))
    elif configs.operating_sys == "Linux":
        os.popen('xdg-open https://www.google.com/search?q={0}'.format(txt))
    else:
        await ctx.send("Can't use search command for this platform.")
        await asyncio.sleep(3)
