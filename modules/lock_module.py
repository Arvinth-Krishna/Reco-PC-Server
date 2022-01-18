# Module: lock
# Description: Locks system
# Usage: !lock or !lock secondsToLock
# Dependencies: time, os

import os, asyncio, configs
from lib.reco_embeds import recoEmbeds as rm
from modules.notification_module import notification



async def lock(ctx,client, minutes=0):
    minutesinmin=minutes
    color=rm.color('colorforCommonMsg')
    if minutes!=0:
        color=rm.color('colorforWaitingMsg')
    await rm.msg(ctx,f"**Locking system{f'** in **{minutes}** minutes.' if minutes!=0 else'.**'}",color=color)
    
    minutes=minutes*60
    if minutes != 0:
        text="System locks in "+str(minutesinmin)+" minutes."
        await notification(ctx,client,text,noti=False)
        await asyncio.sleep(minutes)
        await rm.msg(ctx,f"**Locking system.** (**Time is up! - {minutesinmin} mins**)")
    if configs.operating_sys == "Windows":
        os.system("rundll32.exe user32.dll,LockWorkStation")
    elif configs.operating_sys == "Linux":
        os.popen('gnome-screensaver-command --lock')
    else:
        await ctx.send("Can't lock system.")
        await asyncio.sleep(3)
