# Module: hibernate
# Description: Hibernates the system
# Usage: !hibernate or !hibernate secondsToHibernation
# Dependencies: time, os

import time, os, asyncio, configs


async def hibernate(ctx, minutes=0):
    await ctx.send("Hibernating system.")
    if configs.operating_sys == "Windows":
        minutes=minutes*60

        if minutes != 0:
            await asyncio.sleep(minutes)
        os.system("rundll32.exe PowrProf.dll,SetSuspendState")
    else:
        await ctx.send("Can't hibernate system.")
        await asyncio.sleep(3)
