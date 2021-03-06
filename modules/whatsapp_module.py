# Module: whatsapp
# Description: Opens the chat Screen for the entered MobileNumber
# Usage: !whatsapp CountryCode_Followed_by_MobileNumber
# Dependencies: time, os

import os, time, asyncio, configs


async def whatsapp(ctx, txt):
    await ctx.send("Opening chat screen for {0}".format(txt))

    if configs.operating_sys == "Windows":
        os.system("start https://api.whatsapp.com/send?phone={0}".format(txt))
    elif configs.operating_sys == "Linux":
        os.popen('xdg-open https://api.whatsapp.com/send?phone={0}'.format(txt))
    else:
        await ctx.send("Can't lock system.")
        await asyncio.sleep(3)
