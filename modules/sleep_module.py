# Module: sleep
# Description: Puts system to sleep
# Usage: !sleep or !sleep secondsToSleep
# Dependencies: time, os

import time, os, asyncio, configs
from lib.reco_embeds import recoEmbeds as rm
from modules.notification_module import notification
from lib.helpers import MediaControlAdapter

async def sleep(ctx,client, minutes=0):
    configs.notify_alert_media_command=True
    minutesinmin=minutes
    color=rm.color('colorforCommonMsg')
    if minutes!=0:
        color=rm.color('colorforWaitingMsg')
    info_txt=f'** in **{minutes}** minutes.\n\nTo abort:\n**You have to quit Reco.**' if minutes!=0 else'.**'
    await rm.msg(ctx,f"**Putting system to Sleep{info_txt}",color=color)
    if configs.operating_sys == "Windows":
        minutes=minutes*60
        if minutes != 0:
            text="Putting system to Sleep in "+str(minutesinmin)+" minutes."
            await notification(ctx,client,text,noti=False)
            await asyncio.sleep(minutes)
            await rm.msg(ctx,f"**Putting system to Sleep. ** (**Time is up! - {minutesinmin} mins**)")
        await MediaControlAdapter.win_sleep(MediaControlAdapter(configs.operating_sys))
        configs.notify_alert_media_command=False
    else:
        await ctx.send("Can't put system to sleep.")
        await asyncio.sleep(3)
