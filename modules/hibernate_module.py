# Module: hibernate
# Description: Hibernates the system
# Usage: !hibernate or !hibernate secondsToHibernation
# Dependencies: os, asyncio

import os, asyncio, configs
from lib.reco_embeds import recoEmbeds as rm
from modules.notification_module import notification



async def hibernate(ctx,client, minutes=0):
    minutesinmin=minutes
    color=rm.color('colorforCommonMsg')
    if minutes!=0:
        color=rm.color('colorforWaitingMsg')
    info_txt=f'** in **{minutes}** minutes.\n\nTo abort:\n**You have to quit Reco.**' if minutes!=0 else'.**'
    await rm.msg(ctx,f"**Hibernating system{info_txt}",color=color)
    if configs.operating_sys == "Windows":
        minutes=minutes*60
        if minutes != 0:
            text="System hibernates in "+str(minutesinmin)+" minutes."
            await notification(ctx,client,text,noti=False)
            await asyncio.sleep(minutes)
            await rm.msg(ctx,f"**Hibernating system.** (**Time is up! - {minutesinmin} mins**)",color=rm.color('colorforWaitingMsg'))
            
        os.system("rundll32.exe PowrProf.dll,SetSuspendState")
    else:
        await ctx.send("Can't hibernate system.")
        await asyncio.sleep(3)
