# Module: youtube
# Description: Searches on YouTube.
# Usage: !youtube or !youtube search
# Dependencies: time, os

import os, time, asyncio, configs


async def youtube(ctx, txt):

    if txt=="":
        url="https://www.youtube.com/"
    else:
        url="https://www.youtube.com/results?search_query={0}".format(txt)

    if configs.operating_sys == "Windows":
        os.system("start {0}".format(url))
    elif configs.operating_sys == "Linux":
        os.popen('xdg-open {0}'.format(url))
    else:
        await ctx.send("Can't use YouTube search command for this platform.")
        await asyncio.sleep(3)
