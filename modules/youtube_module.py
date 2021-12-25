# Module: youtube
# Description: Searches on YouTube.
# Usage: !youtube or !youtube search
# Dependencies: time, os

import os, time, asyncio, configs,urllib,re


async def youtube(ctx, txt):

    if txt=="":
        url="https://www.youtube.com/"
    elif txt.__contains__('play') :
        url="https://www.youtube.com/results?search_query={0}+song".format(txt)
        searchResult= urllib.request.urlopen(url,timeout=5)
        firstResult=re.findall(r"watch\?v=(\S{11})",searchResult.read().decode('utf-8'))
        url="https://www.youtube.com/watch?v={0}".format(firstResult[0])
    else:
        url="https://www.youtube.com/results?search_query={0}".format(txt)
    

    if configs.operating_sys == "Windows":
        os.system("start {0}".format(url))
    elif configs.operating_sys == "Linux":
        os.popen('xdg-open {0}'.format(url))
    else:
        await ctx.send("Can't use YouTube search command for this platform.")
        await asyncio.sleep(3)
