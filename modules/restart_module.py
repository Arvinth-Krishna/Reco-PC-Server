# Module: restart
# Description: Restarts system
# Usage: !restart or !restart secondsToRestart
# Dependencies: time, os

import time, os, asyncio, configs


async def restart(ctx, minutes=0):
    await ctx.send("Restarting system.")
    if configs.operating_sys == "Windows":
        minutes=minutes*60

        
        os.system("Shutdown.exe -r -t {0}".format(minutes))
    elif configs.operating_sys == "Linux":
        minutes=minutes*60

        if minutes != 0:
            await asyncio.sleep(minutes)
        os.system("reboot")
    else:
        await ctx.send("Can't restart system.")
        await asyncio.sleep(3)
