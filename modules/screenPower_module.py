# Module: screenPower
# Description: Control screen to turn on or off
# Usage: !screen on or !screen off
# Dependencies: 

import configs,asyncio
from ctypes import windll


async def screen(ctx,option=None):

    if configs.operating_sys == "Windows":
        if option=="off":
            #to turn off use :-
            windll.user32.SendMessageW(65535, 274,61808, 2)
        elif option=="on":
            #turn on use :-
            windll.user32. SendMessageW(65535, 274, 61808, -1)

    else:
        await ctx.send("Currently this feature is not available for your platform.")
        await asyncio.sleep(1)
