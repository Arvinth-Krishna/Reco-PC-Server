# Module: music
# Description: Play video music from YouTube.
# Usage: !music query
# Dependencies: os, time, asynci, urllib.request, re

import os, time, asyncio, configs, urllib.request,re
from re import search, split
from modules import media_module

async def music(ctx, txt):


    if txt=="":
        videoResult="https://www.youtube.com/channel/UC-9-kyTW8ZkZNDHQJ6FgpwQ"
    elif txt.__contains__('playlist?list='):
        print("im insiside playlist")
        print(txt)
        list=txt.split("+")
        print(list)
        for i in range(len(list)):
            if list[i].__contains__('playlist?list='):
                txt=list[i]
                print(txt)
        searchResult= urllib.request.urlopen(txt,timeout=5)
        firstResult=re.findall(r"watch\?v=(\S{11})",searchResult.read().decode('utf-8'))
        urlMaker=""
        for id in firstResult:
            urlMaker=urlMaker+" https://www.youtube.com/watch?v="+id
        videoResult=urlMaker
        await ctx.send("**Queued** {0} **tracks**".format(len(firstResult)))
        print("im insiside playlist")
    elif txt!="quit" and txt!="q" and txt!="clear" and txt!="pause" and txt!="play" and txt!="pause"and txt!="stop" and txt!="videos" and txt!="next"and txt!="prev":
        url="https://www.youtube.com/results?search_query={0}+song".format(txt)
        searchResult= urllib.request.urlopen(url,timeout=5)
        firstResult=re.findall(r"watch\?v=(\S{11})",searchResult.read().decode('utf-8'))
        videoResult="https://www.youtube.com/watch?v={0}".format(firstResult[0])

       



    if configs.operating_sys == "Windows":

        if txt=="quit" or txt=="q" or txt=="clear":
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
        elif txt=="videos":
            os.system("cd start videos")
        elif txt=="":
            os.system("start {0}".format(videoResult))
        else:
            await ctx.send("Searching {0}".format(txt))
            os.system("start vlc --one-instance --playlist-enqueue  --loop  {0}".format(videoResult))


    elif configs.operating_sys == "Linux":
        os.popen('xdg-open {0}'.format(url))
    else:
        await ctx.send("Can't use Music command for this platform.")
        await asyncio.sleep(3)
