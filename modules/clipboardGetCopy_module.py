# Module: clipp
# Description: To copy or to get from PC's Clipboard
# Usage: !clip text or !clip get
# Dependencies: asyncio, pyperclip, time

import asyncio, configs,pyperclip,time
import os
from pathlib import Path

import requests
from lib.reco_embeds import recoEmbeds as rm


async def clip(ctx):
    txt = str(ctx.message.content)
    p=configs.BOT_PREFIX
    
    if configs.operating_sys == "Windows":
        getDataBool=False
        if txt=="!clip get":
            msg=await rm.msg(ctx,"**Getting data from Clipboard...**",color=rm.color("colorforWaitingMsg"))
            getdata=pyperclip.paste()
            time.sleep(0.5)
            if getdata =="":
                getDataBool=True
                getdata="**Oops!, No text to paste.**"
            await msg.delete()
            await rm.extendableMsg(ctx,getdata,color=rm.color('colorforError') if getDataBool else rm.color("colorforCommonMsg"))

        elif txt[6:]!="" or len(ctx.message.attachments)!=0:
            filedata=""
            msgCopydata=""
            msgCopydata=txt[6:]
            attachLength=len(ctx.message.attachments)
            if attachLength!=0:
                for i in range(attachLength):
                    filename = ctx.message.attachments[i].filename
                    url = ctx.message.attachments[i].url
                    if filename=='message.txt':
                        r = requests.get(url, allow_redirects=True)
                        if r.status_code / 100 != 2:
                            raise Exception('Download request from Discord returned {}'.r.status_code)
                        file = r.content
                        path = Path('./',filename)
                        path.write_bytes(file)
                        readme = open('message.txt', 'r', encoding="utf8")
                        data = readme.read()
                        readme.close()
                        filedata+=data+"\n\n"
                        os.remove('./message.txt')
                if filedata!="":
                    msgCopydata= filedata+msgCopydata            
            await rm.msg(ctx,f'''**Copying to Clipboard:**\n\n{msgCopydata if filedata=="" else f'Message.txt{ " file" if attachLength==1 else f"({attachLength}) files"} data + msg.contents copied!'}''')
            pyperclip.copy(msgCopydata)

        elif txt in ("!clip", '!clip '):
            await rm.msg(ctx,f"**Help - {p}clip**\n\n**Commands:**\n```{p}clip <text>\n{p}clip get```")
    else:
        await ctx.send("Clipboard feature is not available for your platform.")
        await asyncio.sleep(3)
