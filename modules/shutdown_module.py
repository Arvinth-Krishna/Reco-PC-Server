# Module: shutdown
# Description: Shuts system down
# Usage: !shutdown or !shutdown secondsToShutdown
# Dependencies: time, os

import time, os, asyncio, configs


async def shutdown(ctx, minutes=0):
    await ctx.send("Shutting system down.")
    if configs.operating_sys == "Windows":
        minutes=minutes*60

         
        os.system("shutdown.exe -s -t {0}".format(minutes))
    elif configs.operating_sys == "Linux":
        minutes=minutes*60

        if minutes != 0:
            await asyncio.sleep(minutes)
        os.system("shutdown")
    else:
        await ctx.send("Can't shutdown system.")
        await asyncio.sleep(3)
