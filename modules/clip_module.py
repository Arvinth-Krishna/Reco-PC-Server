# Module: clip
# Description: copy to PC's Clipboard
# Usage: !clip text
# Dependencies: time, os

import os, time, asyncio, configs


async def clip(ctx, txt):
    await ctx.send("Copying to clipboard")

    if configs.operating_sys == "Windows":
        os.system('''echo {0} |clip'''.format(txt))
    else:
        await ctx.send("Can't copy")
        await asyncio.sleep(3)
