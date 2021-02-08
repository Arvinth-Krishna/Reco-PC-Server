# Module: sleep
# Description: Puts system to sleep
# Usage: !sleep or !sleep secondsToSleep
# Dependencies: time, os

import time, os, asyncio, configs


async def sleep(ctx, minutes=0):
    if configs.operating_sys == "Windows":
        await ctx.send("Putting system to sleep.")
        minutes=minutes*60

        if minutes != 0:
            await asyncio.sleep(minutes)

        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
    else:
        await ctx.send("Can't put system to sleep.")
        await asyncio.sleep(3)
