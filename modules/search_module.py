# Module: search
# Description: Your query will be searched on Google.
# Usage: !search or !search query
# Dependencies: os, asyncio

import os, asyncio, configs
from lib.reco_embeds import recoEmbeds as rm


async def search(ctx):
    url_bool=False
    txt = str(ctx.message.content[8:])
    await rm.msg(ctx,f"**Searching**:\n{txt}")
    list=txt.split(" ")
    for i in range(len(list)):
        if list[i].__contains__('https') or list[i].__contains__('www') :
            txt=list[i]
            print(txt)
            url_bool=True
            break
    if not url_bool:
        txt = str(ctx.message.content[8:])
        txt=txt.replace(" ","+")
    
    
    
    if configs.operating_sys == "Windows":
        if url_bool:
            os.system("start {0}".format(txt))
        else:
           os.system("start https://www.google.com/search?q={0}".format(txt))
    elif configs.operating_sys == "Linux":
        os.popen('xdg-open https://www.google.com/search?q={0}'.format(txt))
    else:
        await ctx.send("Can't use search command for this platform.")
        await asyncio.sleep(3)
