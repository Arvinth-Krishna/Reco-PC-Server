# Module: launch
# Description: Lauches a custom shortcut in the shortcuts directory
# Usage: !launch [shortcut]
# Dependencies: os, time, glob 

import os, configs,time

from lib.helpers import checkfolder
from lib.reco_embeds import recoEmbeds as rm
from glob import glob

async def launch(ctx,client, shortcut=None):
    p=configs.BOT_PREFIX
    fileOpened=False
    checkfolder()

    if configs.operating_sys == "Windows":

        if shortcut!="":
            if shortcut.isnumeric():
                msg=await rm.msg(ctx,f"**Opening File No: {shortcut}**",color=rm.color('colorforWaitingMsg'))
            elif shortcut=="list":
                msg=await ctx.send("> Gathering files from **Shortcut Folder**.")
            else:
                msg=await rm.msg(ctx,f"Searching **{shortcut.capitalize()}**",color=rm.color('colorforWaitingMsg'))
        elif shortcut=="":
            await rm.msg(ctx,f'''**Help - {p}launch**

Using launch command you can easily open any application or file which are available in your Reco's **Shortcut folder**.

**Commands:**
```{p}launch list
{p}launch open
{p}launch File_Number
{p}launch File_Name```
            
**🎬 YouTube**
**[How to use {p}launch in {client.user.name}?](https://youtu.be/-b-7-8oK1tI)**''')
            return
        shortcutFolderPath=configs.RECO_PATH+"/shortcuts/*"
        files = glob(shortcutFolderPath)

        print(len(files))
        print(files)
        time.sleep(1)
        if len(files)!=0:
           folderExtensions=set([f".{e.split('.')[-1]}" for e in files])
           folderFileNames=[f"{f.split(chr(92))[-1]}" for f in files]
           print(folderExtensions)
        else:
            await msg.delete()
            await rm.msg(ctx,f"**Shortcut Folder is Empty!**\n\n**Path**: {shortcutFolderPath}",rm.color('colorforError'))
            return

        if shortcut=="list":
            await msg.delete()
            filenames=f"Files Count: **{len(files)}** \n\n"+"\n".join([f"**{n}** - **{f.split(chr(92))[-1].replace('_',f'{chr(92)}_')}**" for n,f in enumerate(files)])
            await rm.extendableMsg(ctx,filenames)

        elif shortcut.isnumeric():
            if int(shortcut)<len(files):
                await rm.editMsg(ctx,msg,f"**Opening {files[int(shortcut)].split(chr(92))[-1]}**...")
                os.startfile(files[int(shortcut)])

            else:
                await rm.editMsg(ctx,msg,f"**❌ Invalid File Number!**\n\nTry:\n**{p}launch list**",color=rm.color('colorforError'))
        elif shortcut!="":     
            if shortcut!=None:
                    for e in folderExtensions:
                        if (os.path.isfile("shortcuts/" + shortcut + e)):
                           await rm.editMsg(ctx,msg,f'**Opening {shortcut.capitalize() }{e}**...')
                           os.startfile("shortcuts\\" + shortcut + e)
                           fileOpened=True
                           break
                        elif shortcut.__contains__("."):
                            if (os.path.isfile("shortcuts/" + shortcut)):
                               await rm.editMsg(ctx,msg,f'**Opening {shortcut.capitalize()}**...')
                               os.startfile("shortcuts\\" + shortcut)
                               fileOpened=True
                               break
                    if not fileOpened:
                        for f in folderFileNames:
                            file=f.lower()
                            print("File Finder: ",shortcut,"->",file)
                            if file.__contains__(shortcut.lower()):
                                index= folderFileNames.index(f)
                                await rm.editMsg(ctx,msg,f'**Opening {files[index].split(chr(92))[-1]}**...')
                                os.startfile(files[index])
                                fileOpened=True
                                break
                   
            if not fileOpened:
                await rm.editMsg(ctx,msg,"**No such file in your shortcuts folder.**",color=rm.color('colorforError'))
       
            
    else:
        await ctx.send("Module not yet supported on Linux and macOS")