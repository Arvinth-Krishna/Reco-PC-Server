# Module: url
# Description: Launch websites
# Usage: !url website
# Dependencies: os, time, asyncio, configs

import os, time, asyncio, configs


async def url(ctx, txt):
    await ctx.send("Launching the website")

    if configs.operating_sys == "Windows":
        os.system("start {0}".format(txt))
    elif configs.operating_sys == "Linux":
        os.popen('xdg-open {0}'.format(txt))
    else:
        await ctx.send("URL feature is not available in this platform.")
        await asyncio.sleep(3)
