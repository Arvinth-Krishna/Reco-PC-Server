# Module: music
# Description: Play video music from YouTube.
# Usage: !music query
# Dependencies: os, time, asynci, urllib.request, re


import os, asyncio, configs, urllib.request,re
from re import search, split
from modules import media_module
from modules import notification_module
import pytube
from lib.reco_embeds import recoEmbeds as rm


async def music(ctx,client, txt):
    
    splitTxt=txt.split("+")
    print(splitTxt)

    if txt=="":
        videoResult="https://www.youtube.com/channel/UC-9-kyTW8ZkZNDHQJ6FgpwQ"
    elif txt.__contains__('playlist?list=') and (splitTxt[0]=="dm" or splitTxt[0]=="DM" or splitTxt[0]=="Dm") :
        print("im insiside youtube download playlist")
        print(txt)
        list=txt.split("+")
        print(list)
        for i in range(len(list)):
            if list[i].__contains__('playlist?list='):
                txt=list[i]
                print(txt)
                break
        await rm.msg(ctx,"**Fetching your Music from your playlist** <{0}> **and all your audio files will be downloaded soon.\n\n⚠⚠ Till then Reco can\'t be used.**".format(txt))
        await notification_module.notification(ctx,client,txt="Fetching Music from playlist.\n All songs will be downloaded soon.\n⚠⚠ Till then Reco can\'t be used.",noti=False)

        searchResult= urllib.request.urlopen(txt,timeout=5) 
        firstResult=re.findall(r"watch\?v=(\S{11})",searchResult.read().decode('utf-8'))
        
        count=0
        
        urlMaker=""
       
        for id in firstResult:
            if (urlMaker.__contains__(id)):
                continue
            count=count+1
            urlMaker=urlMaker+" https://www.youtube.com/watch?v="+id
            link=" https://www.youtube.com/watch?v="+id
            yt = pytube.YouTube(link)
            stream = yt.streams.filter(only_audio=True).first()


            audiomp4=stream.download(r'./downloads/youtube_music')
            base, ext=os.path.splitext(audiomp4)
            new_file=base+'.mp3'
            os.rename(audiomp4,new_file)        
            await rm.msg(ctx,"Downloaded Music: **{0}**.\nTrack No: **{1}**.".format(yt.title,count))
        print('all files downloaded')
        await rm.msg(ctx,"**Downloaded** {0} **tracks**".format(count))

    elif txt.__contains__('https://') and (splitTxt[0]=="dm" or splitTxt[0]=="DM" or splitTxt[0]=="Dm"):
        print("im insiside download url")
        print(txt)
        list=txt.split("+")
        print(list)
        for i in range(len(list)):
            if list[i].__contains__('https://'):
                link=list[i]
                print(txt)
                break
        await rm.msg(ctx,"**Fetching the audio from the URL given** <{0}> **and audio file will be downloaded soon.\n\n⚠⚠ Till then Reco can\'t be used.**".format(link))
        await notification_module.notification(ctx,client,txt="Fetching Music from the URL.\n Audio file will be downloaded soon.\n⚠⚠ Till then Reco can\'t be used.",noti=False)


        yt = pytube.YouTube(link)
        stream = yt.streams.filter(only_audio=True).first()
        await rm.msg(ctx,"**Downloading your music** <{0}>".format(link))


        audiomp4=stream.download(r'./downloads/youtube_music')
        base, ext=os.path.splitext(audiomp4)
        new_file=base+'.mp3'
        os.rename(audiomp4,new_file)

    elif (splitTxt[0]=="dm" or splitTxt[0]=="DM" or splitTxt[0]=="Dm"):
        await rm.msg(ctx,"**Searching your Music by the keyword given and your audio file will be downloaded soon.\n\n⚠⚠ Till then Reco can\'t be used.**")
        await notification_module.notification(ctx,client,txt="Searching your Music by the keyword given and your audio file will be downloaded soon.\n⚠⚠ Till then Reco can\'t be used.",noti=False)

        print("im inside the youtube downloader")
        print(len(txt))
        slice_txt = txt[2: len(txt): 1]
        


        print(slice_txt)

        url="https://www.youtube.com/results?search_query={0}+song".format(slice_txt)
        searchResult= urllib.request.urlopen(url,timeout=5)
        firstResult=re.findall(r"watch\?v=(\S{11})",searchResult.read().decode('utf-8'))
        link="https://www.youtube.com/watch?v={0}".format(firstResult[0])
        await rm.msg(ctx,"**Downloading your music:**")
        await ctx.send("{0}".format(link))
        

        yt = pytube.YouTube(link)
        stream = yt.streams.filter(only_audio=True).first()

        audiomp4=stream.download(r'./downloads/youtube_music')
        base, ext=os.path.splitext(audiomp4)
        new_file=base+'.mp3'
        os.rename(audiomp4,new_file)

    

        



        
    elif txt.__contains__('playlist?list=') and (splitTxt[0]=="dv" or splitTxt[0]=="DV" or splitTxt[0]=="Dv") :
        print("im insiside youtube download playlist")
        print(txt)
        list=txt.split("+")
        print(list)
        for i in range(len(list)):
            if list[i].__contains__('playlist?list='):
                txt=list[i]
                print(txt)
        await rm.msg(ctx,"**Fetching Music Videos from your playlist** <{0}> **and video files will be downloaded soon.\n\n⚠⚠ Till then Reco can\'t be used.**".format(txt))
        await notification_module.notification(ctx,client,txt="Fetching Music Videos from your playlist and video files will be downloaded soon.\n⚠⚠ Till then Reco can\'t be used.",noti=False)

  

        searchResult= urllib.request.urlopen(txt,timeout=5) 
        firstResult=re.findall(r"watch\?v=(\S{11})",searchResult.read().decode('utf-8'))
        count=0
        
        urlMaker=""
       
        for id in firstResult:
            if (urlMaker.__contains__(id)):
                continue
            count=count+1
            urlMaker=urlMaker+" https://www.youtube.com/watch?v="+id
            link=" https://www.youtube.com/watch?v="+id
            yt = pytube.YouTube(link)
            stream = yt.streams.filter(res="720p").first()
            if stream==None:
                stream = yt.streams.filter(res="480p").first()
            if stream==None:
                stream = yt.streams.filter(res="360p").first()
            if stream==None:
                stream = yt.streams.filter(res="240p").first()
            stream.download(r'./downloads/youtube_videos')
            await rm.msg(ctx,"Downloaded Video: **{0}**.\nTrack No: **{1}**".format(yt.title,count))

        
        print('all files downloaded')
        await rm.msg(ctx,"**Downloaded** {0} **tracks**".format(count))

    elif txt.__contains__('https://') and (splitTxt[0]=="dv" or splitTxt[0]=="DV" or splitTxt[0]=="Dv"):
        print("im insiside download url")
        print(txt)
        list=txt.split("+")
        print(list)
        for i in range(len(list)):
            if list[i].__contains__('https://'):
                link=list[i]
                print(txt)
                break
        await rm.msg(ctx,"**Fetching the video from the URL given** <{0}> **and video file will be downloaded soon.\n\n⚠⚠ Till then Reco can\'t be used.**".format(link))
        await notification_module.notification(ctx,client,txt="Fetching the video from the URL and file will be downloaded soon.\n⚠⚠ Till then Reco can\'t be used.",noti=False)

        yt = pytube.YouTube(link)
        stream = yt.streams.filter(res="720p").first()
        await ctx.send("**Downloading your video** <{0}>".format(link))
        if stream==None:
            stream = yt.streams.filter(res="480p").first()
        if stream==None:
            stream = yt.streams.filter(res="360p").first()
        if stream==None:
            stream = yt.streams.filter(res="240p").first()

        stream.download(r'./downloads/youtube_videos')

    elif (splitTxt[0]=="dv" or splitTxt[0]=="DV" or splitTxt[0]=="Dv"):
        await rm.msg(ctx,"**Searching your video by the keyword given and your video file will be downloaded soon.\n\n⚠⚠ Till then Reco can\'t be used.**")
        await notification_module.notification(ctx,client,txt="Searching your video by the keyword and the video file will be downloaded soon.\n⚠⚠ Till then Reco can\'t be used.",noti=False)

        print("im inside the youtube downloader")
        print(len(txt))
        slice_txt = txt[2: len(txt): 1]
        


        print(slice_txt)

        url="https://www.youtube.com/results?search_query={0}+song".format(slice_txt)
        searchResult= urllib.request.urlopen(url,timeout=5)
        firstResult=re.findall(r"watch\?v=(\S{11})",searchResult.read().decode('utf-8'))
        link="https://www.youtube.com/watch?v={0}".format(firstResult[0])
        await rm.msg(ctx,"**Downloading this video:**")
        await ctx.send("{0}".format(link))
        

        yt = pytube.YouTube(link)
        stream = yt.streams.filter(res="720p").first()
        if stream==None:
            stream = yt.streams.filter(res="480p").first()
        if stream==None:
            stream = yt.streams.filter(res="360p").first()
        if stream==None:
            stream = yt.streams.filter(res="240p").first()
        stream.download(r'./downloads/youtube_videos')

        videoResult="https://www.youtube.com/channel/UC-9-kyTW8ZkZNDHQJ6FgpwQ"

    

        


    elif txt.__contains__('playlist?list='):
        print("im insiside playlisttttt")
        print(txt)
        list=txt.split("+")
        print(list)
        for i in range(len(list)):
            if list[i].__contains__('playlist?list='):
                txt=list[i]
                print(txt)
                break
        searchResult= urllib.request.urlopen(txt,timeout=5) 
        firstResult=re.findall(r"watch\?v=(\S{11})",searchResult.read().decode('utf-8'))
        count=0
        urlMaker=""
        for id in firstResult:
            if (urlMaker.__contains__(id)):
                continue
            count=count+1
            urlMaker=urlMaker+" https://www.youtube.com/watch?v="+id
        videoResult=urlMaker
        print(urlMaker)
        await rm.msg(ctx,"**Queued** {0} **tracks**".format(count))

    elif txt.__contains__('https://'):
        print("im insiside url")
        print(txt)
        list=txt.split("+")
        print(list)
        for i in range(len(list)):
            if list[i].__contains__('https://'):
                txt=list[i]
                print(txt)
                break
        videoResult=txt

    elif txt!="quit" and txt!="q" and txt!="clear" and txt!="pause" and txt!="df" and txt!="DF" and txt!="Df" and txt!="dF" and txt!="play" and txt!="pause"and txt!="stop"  and txt!="next"and txt!="prev":
        url="https://www.youtube.com/results?search_query={0}+song".format(txt)
        searchResult= urllib.request.urlopen(url,timeout=5)
        firstResult=re.findall(r"watch\?v=(\S{11})",searchResult.read().decode('utf-8'))
        videoResult="https://www.youtube.com/watch?v={0}".format(firstResult[0])


       



    if configs.operating_sys == "Windows":

        if txt=="quit" or txt=="q" or txt=="clear":
            await rm.msg(ctx,"**Quitting VLC Player!**")
            os.system("taskkill /F /IM vlc.exe")
        elif (splitTxt[0]=="dv" or splitTxt[0]=="DV" or splitTxt[0]=="Dv"):
           await notification_module.notification(ctx,client,txt="Videos - Download Completed.\nNow you can use your Reco.",noti=False)
           await rm.msg(ctx,"🥳 Videos - Download completed.\n\n**Now you can use your Reco.**")
        elif (splitTxt[0]=="dm" or splitTxt[0]=="DM" or splitTxt[0]=="Dm"):
           await notification_module.notification(ctx,client,txt="🥳 Music - Download Completed.\nNow you can use your Reco.",noti=False)
           await rm.msg(ctx,"🥳 Music - Download Completed.\n\n**Now you can use your Reco.**")
        elif txt=="df" or txt=="DF" or txt=="Df" or txt=="dF":
            
            print(os.getcwd())
            os.system("start downloads")
            await rm.msg(ctx,"Opening Downloads Folder.")

        elif txt=="pause":
            await media_module.media(ctx, "pause")
        elif txt=="play":
            await media_module.media(ctx, "play")
        elif txt=="stop":
            await media_module.media(ctx, "stop")
        elif txt=="next":
            await media_module.media(ctx, "next")
        elif txt=="prev":
            await media_module.media(ctx, "prev")
        
        elif txt=="":
            p=configs.BOT_PREFIX
            await rm.msg(ctx,txt=f'''**Help - {p}Music / {p}m**\n\n**Commands:**
```{p}m    <Song Name/YouTube Video URL/Playlist URL>
{p}m dm <Song Name/YouTube Video URL/Playlist URL> 
{p}m dv <Song Name/YouTube Video URL/Playlist URL>
{p}m df
{p}m play
{p}m pause
{p}m stop
{p}m next
{p}m prev

* dm -> download music | dv -> download video | df -> download folder```

**FYI**,
🔸 Make sure you have VLC Player installed.
🔸 If you wanna use Play, Pause and other commands, globally then you have to add them in  **VLC  -> Tools -> Preference -> Hotkey**.
🔸 [YouTube video coming soon!](https://www.youtube.com/channel/UCKU73B2c4FBl8o4b1qBBPxA)
''')
        else:
            await rm.msg(ctx,"Searching {0}".format(txt))
            myTruncatedString = videoResult[0:1500]
            await rm.msg(ctx,"**Sending this search result to VLC:**\n")
            await ctx.send("{0}".format(myTruncatedString))
            os.system("start vlc --one-instance --playlist-enqueue  --loop  {0}".format(videoResult))


    elif configs.operating_sys == "Linux":
        await ctx.send("Can't use Music command for this platform.")
    else:
        await ctx.send("Can't use Music command for this platform.")
        await asyncio.sleep(3)
