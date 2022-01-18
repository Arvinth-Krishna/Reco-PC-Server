# Module: shutdown
# Description: Shuts system down
# Usage: !shutdown or !shutdown secondsToShutdown
# Dependencies: time, os

import time, os, asyncio, configs
from lib.reco_embeds import recoEmbeds as rm
from modules.notification_module import notification



async def shutdown(ctx,client, minutes=0):

    p=configs.BOT_PREFIX
    color=rm.color('colorforCommonMsg')
    if minutes!=0:
        color=rm.color('colorforWaitingMsg')
    info_txt=f'** in **{minutes}** minutes.\n\nTo abort:\n**{p}abort**' if minutes!=0 else'.**'
    text="System shutdown in "+str(minutes)+" minutes."
    
    await rm.msg(ctx,f"**Shutting down system{info_txt}",color=color)
    if configs.operating_sys == "Windows":
        minutes=minutes*60
        os.system("shutdown.exe -s -t {0}".format(minutes))
        if minutes!=0:
           await notification(ctx,client,text,noti=False)  
    elif configs.operating_sys == "Linux":
        minutes=minutes*60

        if minutes != 0:
            await asyncio.sleep(minutes)
        os.system("shutdown")
    else:
        await ctx.send("Can't shutdown system.")
        await asyncio.sleep(3)
