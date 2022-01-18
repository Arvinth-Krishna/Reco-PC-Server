# Module: signout
# Description: Sign out the user out of the system
# Usage: !signout or !signout minutes
# Dependencies: os, asyncio

import os, asyncio, configs
from lib.reco_embeds import recoEmbeds as rm
from modules.notification_module import notification


async def signout(ctx,client, minutes=0):
    minutesinmin=minutes
    color=rm.color('colorforCommonMsg')
    if minutes!=0:
        color=rm.color('colorforWaitingMsg')
    info_txt=f'** in **{minutes}** minutes.\n\nTo abort:\n**You have to quit Reco.**' if minutes!=0 else'.**'
    await rm.msg(ctx,f"**System signing out{info_txt}",color=color)
    
    minutes=minutes*60
    if minutes != 0:
        text="System signing out in "+str(minutesinmin)+" minutes."
        await notification(ctx,client,text,noti=False)
        await asyncio.sleep(minutes)
        await rm.msg(ctx,f"**System signing out.** (**Time is up! - {minutesinmin} mins**)")
        
    if configs.operating_sys == "Windows":
        os.system("Shutdown.exe -l")
    else:
        await ctx.send("Can't logoff system.")
        await asyncio.sleep(3)
