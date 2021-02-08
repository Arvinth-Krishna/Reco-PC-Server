# Module: abort
# Description: Abort the Shutdown or Restart schedule
# Usage: !abort
# Dependencies: time, os

import time, os, asyncio, configs


async def abort(ctx):
    await ctx.send("Aborting schedule.")
    if configs.operating_sys == "Windows":
        

        os.system("Shutdown.exe -a")
        
    elif configs.operating_sys == "Linux":
        
        os.system("shutdown -c")
    else:
        await ctx.send("Can't Abort the schedule.")
        await asyncio.sleep(3)
