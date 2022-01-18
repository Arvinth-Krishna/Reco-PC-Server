# Module: url
# Description: Launch websites
# Usage: !url website
# Dependencies: os, time, asyncio, configs

import os, asyncio, configs
from lib.reco_embeds import recoEmbeds as rm


async def url(ctx):
    txt = str(ctx.message.content[5:])
    await rm.msg(ctx,f"**Launching the website**:\n{txt}")

    print(txt)
    list=txt.split(" ")
    
    for i in range(len(list)):
        if list[i].__contains__('https') or list[i].__contains__('www') :
            txt=list[i]
            print(txt)
            break

    if configs.operating_sys == "Windows":
        os.system("start {0}".format(txt))
    elif configs.operating_sys == "Linux":
        os.popen('xdg-open {0}'.format(txt))
    else:
        await ctx.send("URL feature is not available in this platform.")
        await asyncio.sleep(3)
