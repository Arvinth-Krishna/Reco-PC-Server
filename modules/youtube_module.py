# Module: youtube
# Description: Searches on YouTube.
# Usage: !youtube or !youtube search
# Dependencies: time, os

import os, asyncio, configs,urllib,re
from lib.reco_embeds import recoEmbeds as rm


async def youtube(ctx):
    p=configs.BOT_PREFIX
    
    txt = str(ctx.message.content)
    if txt.__contains__(f"{p}youtube"):
        txt = str(ctx.message.content[9:])
    elif txt.__contains__(f"{p}yt"):
        txt = str(ctx.message.content[4:])
       


    print(txt)
    print(txt[:5])

    

    if txt=="":
        await rm.msg(ctx,f"**Help - {p}Youtube / {p}yt**\n\n**Commands:**\n```{p}yt web\n{p}yt <search>\n{p}yt play <txt>\n\n**eg:**\n{p}yt GAKventure\n{p} play The Nights")
        return
    elif txt=="web":
        await rm.msg(ctx,"**Opening [Youtube](https://www.youtube.com/)**...")
        url="https://www.youtube.com/"
    elif txt[:4]==('play') :
        query=txt[5:].capitalize()
        urlQuery=txt[5:].replace(" ","+")
        msg=await rm.msg(ctx,f"**Searching**: {query}" )
        txt=txt[5:].replace(" ","+")
        url=f"https://www.youtube.com/results?search_query={urlQuery}"
        searchResult= urllib.request.urlopen(url,timeout=5)
        firstResult=re.findall(r"watch\?v=(\S{11})",searchResult.read().decode('utf-8'))
        url="https://www.youtube.com/watch?v={0}".format(firstResult[0])
        await rm.editMsg(ctx,msg,f"**Query**: {query}\n\n**Playing ⇩**")
        await ctx.send(url)
    else:
        await rm.msg(ctx,f"**Searching**: {txt.capitalize()}" )
        txt=txt.replace(" ","+")
        url="https://www.youtube.com/results?search_query={0}".format(txt)
    

    if configs.operating_sys == "Windows":
        os.system("start {0}".format(url))
    elif configs.operating_sys == "Linux":
        os.popen('xdg-open {0}'.format(url))
    else:
        await ctx.send("Can't use YouTube search command for this platform.")
        await asyncio.sleep(3)
