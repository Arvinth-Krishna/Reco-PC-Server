# Module: music
# Description: Play video music from YouTube.
# Usage: !music query
# Dependencies: os, time, asynci, urllib.request, re

import os, time, asyncio, configs, urllib.request,re
from re import search, split
from modules import media_module
import pytube

async def music(ctx, txt):
    
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
        await ctx.send("**Fetching your Music from your playlist** <{0}> **and all your audio files will be downloaded soon.\n\n⚠⚠ Till then Reco can\'t be used.**".format(txt))
        info = "Downloader_info.txt"
             # popen() is similar to open()
        file = open(info, 'w')
        file.write("**Fetching your Music from your playlist** <{0}> **and all your audio files will be downloaded soon.\n\nTill then Reco can\'t be used.**".format(txt))
        file.close()
        os.system("start Downloader_info.txt")

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
            await ctx.send("This music is downloaded: **{0}**.\n **{1}** tracks downloaded.".format(yt.title,count))
        print('all files downloaded')
        await ctx.send("**Downloaded** {0} **tracks**".format(count))

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
        await ctx.send("**Fetching the audio from the URL given** <{0}> **and audio file will be downloaded soon.\n\n⚠⚠ Till then Reco can\'t be used.**".format(link))
        info = "Downloader_info.txt"
             # popen() is similar to open()
        file = open(info, 'w')
        file.write("**Fetching the audio from the URL given** <{0}> **and audio file will be downloaded soon.\n\nTill then Reco can\'t be used.**".format(link))
        file.close()
        os.system("start Downloader_info.txt")

        yt = pytube.YouTube(link)
        stream = yt.streams.filter(only_audio=True).first()
        await ctx.send("**Downloading your music** <{0}>".format(link))


        audiomp4=stream.download(r'./downloads/youtube_music')
        base, ext=os.path.splitext(audiomp4)
        new_file=base+'.mp3'
        os.rename(audiomp4,new_file)

    elif (splitTxt[0]=="dm" or splitTxt[0]=="DM" or splitTxt[0]=="Dm"):
        await ctx.send("**Searching your Music by the keyword given and your audio file will be downloaded soon.\n\n⚠⚠ Till then Reco can\'t be used.**")
        info = "Downloader_info.txt"
             # popen() is similar to open()
        file = open(info, 'w')
        file.write("**Searching your Music by the keyword given and your audio file will be downloaded soon.\n\nTill then Reco can\'t be used.**")
        file.close()
        os.system("start Downloader_info.txt")

        print("im inside the youtube downloader")
        print(len(txt))
        slice_txt = txt[2: len(txt): 1]
        


        print(slice_txt)

        url="https://www.youtube.com/results?search_query={0}+song".format(slice_txt)
        searchResult= urllib.request.urlopen(url,timeout=5)
        firstResult=re.findall(r"watch\?v=(\S{11})",searchResult.read().decode('utf-8'))
        link="https://www.youtube.com/watch?v={0}".format(firstResult[0])
        await ctx.send("**Downloading your music** {0}".format(link))
        

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
        await ctx.send("**Fetching your videos from your playlist** <{0}> **and video files will be downloaded soon.\n\n⚠⚠ Till then Reco can\'t be used.**".format(txt))
        info = "Downloader_info.txt"
             # popen() is similar to open()
        file = open(info, 'w')
        file.write("**Fetching your videos from your playlist** <{0}> **and video files will be downloaded soon.\n\nTill then Reco can\'t be used.**".format(txt))
        file.close()
        os.system("start Downloader_info.txt")

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
            await ctx.send("This video is downloaded: **{0}**.\n **{1}** tracks downloaded.".format(yt.title,count))

        
        print('all files downloaded')
        await ctx.send("**Downloaded** {0} **tracks**".format(count))

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
        await ctx.send("**Fetching the video from the URL given** <{0}> **and video file will be downloaded soon.\n\n⚠⚠ Till then Reco can\'t be used.**".format(link))
        info = "Downloader_info.txt"
             # popen() is similar to open()
        file = open(info, 'w')
        file.write("**Fetching the video from the URL given** <{0}> **and video file will be downloaded soon.\n\nTill then Reco can\'t be used.**".format(link))
        file.close()
        os.system("start Downloader_info.txt")

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
        await ctx.send("**Searching your video by the keyword given and your video file will be downloaded soon.\n\n⚠⚠ Till then Reco can\'t be used.**")
        info = "Downloader_info.txt"
             # popen() is similar to open()
        file = open(info, 'w')
        file.write("**Searching your video by the keyword given and your video file will be downloaded soon.\n\nTill then Reco can\'t be used.**")
        file.close()
        os.system("start Downloader_info.txt")

        print("im inside the youtube downloader")
        print(len(txt))
        slice_txt = txt[2: len(txt): 1]
        


        print(slice_txt)

        url="https://www.youtube.com/results?search_query={0}+song".format(slice_txt)
        searchResult= urllib.request.urlopen(url,timeout=5)
        firstResult=re.findall(r"watch\?v=(\S{11})",searchResult.read().decode('utf-8'))
        link="https://www.youtube.com/watch?v={0}".format(firstResult[0])
        await ctx.send("Downloading this video {0}".format(link))
        

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
        await ctx.send("**Queued** {0} **tracks**".format(count))
        print("im insiside playlist")


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
        print("im insiside url")


    elif txt!="quit" and txt!="q" and txt!="clear" and txt!="pause" and txt!="df" and txt!="DF" and txt!="Df" and txt!="dF" and txt!="play" and txt!="pause"and txt!="stop"  and txt!="next"and txt!="prev":
        url="https://www.youtube.com/results?search_query={0}+song".format(txt)
        searchResult= urllib.request.urlopen(url,timeout=5)
        firstResult=re.findall(r"watch\?v=(\S{11})",searchResult.read().decode('utf-8'))
        videoResult="https://www.youtube.com/watch?v={0}".format(firstResult[0])


       



    if configs.operating_sys == "Windows":

        if txt=="quit" or txt=="q" or txt=="clear":
            os.system("taskkill /F /IM vlc.exe")
        elif (splitTxt[0]=="dv" or splitTxt[0]=="DV" or splitTxt[0]=="Dv"):
            info = "Downloader_info.txt"
             # popen() is similar to open()
            file = open(info, 'w')
            file.write("Videos - Download Completed.\nNow you can use your Reco.")
            file.close()
            os.system("start Downloader_info.txt")
            await ctx.send("🥳 Videos - Download completed.\n\n**Now you can use your Reco.**")
        elif (splitTxt[0]=="dm" or splitTxt[0]=="DM" or splitTxt[0]=="Dm"):
            info = "Downloader_info.txt"
             # popen() is similar to open()
            file = open(info, 'w')
            file.write("Music - Download Completed.\nNow you can use your Reco.")
            file.close()
            os.system("start Downloader_info.txt")
            await ctx.send("🥳 Music - Download Completed.\n\n**Now you can use your Reco.**")
        elif txt=="df" or txt=="DF" or txt=="Df" or txt=="dF":
            
            print(os.getcwd())
            os.system("start downloads")
            await ctx.send("Opening Downloads Folder")

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
        
        elif txt=="":
            os.system("start {0}".format(videoResult))
        else:
            await ctx.send("Searching {0}".format(txt))
            await ctx.send("**Sending this search result to VLC**\n{0}".format(videoResult))
            os.system("start vlc --one-instance --playlist-enqueue  --loop  {0}".format(videoResult))


    elif configs.operating_sys == "Linux":
        os.popen('xdg-open {0}'.format(url))
    else:
        await ctx.send("Can't use Music command for this platform.")
        await asyncio.sleep(3)
