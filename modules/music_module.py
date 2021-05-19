# Module: music
# Description: Play video music from YouTube.
# Usage: !music query
# Dependencies: os, time, asynci, urllib.request, re

import os, time, asyncio, configs, urllib.request,re

from modules import media_module

async def music(ctx, txt):
    
    if txt=="":
        videoResult="https://www.youtube.com/channel/UC-9-kyTW8ZkZNDHQJ6FgpwQ"
    elif txt!="quit" and txt!="pause" and txt!="play"and txt!="stop"and txt!="next"and txt!="prev":
        url="https://www.youtube.com/results?search_query={0}+song".format(txt)
        searchResult= urllib.request.urlopen(url,timeout=5)
        firstResult=re.findall(r"watch\?v=(\S{11})",searchResult.read().decode())
        videoResult="https://www.youtube.com/watch?v={0}".format(firstResult[0])
        await ctx.send("IM inside Elif")



    if configs.operating_sys == "Windows":
        if txt=="quit":
            os.system("taskkill /F /IM vlc.exe")
        elif txt=="pause":
            await media_module.media(ctx, "pause", 1)
        elif txt=="play":
            await media_module.media(ctx, "play", 1)
        elif txt=="stop":
            await media_module.media(ctx, "stop", 1)
        elif txt=="next":
            await media_module.media(ctx, "next", 1)
        elif txt=="prev":
            await media_module.media(ctx, "prev", 1)

        else:
            await ctx.send("Searching {0}".format(txt))
            os.system("start vlc --one-instance --playlist-enqueue {0}".format(videoResult))


    elif configs.operating_sys == "Linux":
        os.popen('xdg-open {0}'.format(url))
    else:
        await ctx.send("Can't use Music command for this platform.")
        await asyncio.sleep(3)
