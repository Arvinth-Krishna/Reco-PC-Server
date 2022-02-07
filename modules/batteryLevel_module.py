# Module: BatteryLevel
# Description: To see the estimated battery charge remaining
# Usage: !batterylevel
# Dependencies: os, asyncio,time

import os, asyncio, configs,time,psutil
from socket import gethostname

from lib.reco_embeds import recoEmbeds as rm
from modules.notification_module import notification

def convertTime(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return "%d:%02d:%02d" % (hours, minutes, seconds)

async def batterylevel(ctx,client,option=None):
        p=configs.BOT_PREFIX
        cr=""
       
        if configs.operating_sys == "Windows":
              if option in(None,'show'):
                    battery = psutil.sensors_battery()
                    editEmbed=await rm.msg(ctx,txt="**Getting Battery Level!**",color=rm.color("colorforWaitingMsg"))
                    if battery!=None:
                         batteryInfoTxt=f"💻 **{gethostname().capitalize()}**\n\n{'⚡' if battery.power_plugged else '🔋' } **{battery.percent}%** | Battery left: **{convertTime(battery.secsleft)}**"
                    else:
                         batteryInfoTxt="Opps!, No battery connected to your system."

 
                    time.sleep(1)
                    if battery!=None:
                        await rm.editMsg(ctx,editEmbed,editmsg=batteryInfoTxt)
                    else:
                         await rm.editMsg(ctx,editEmbed,editmsg=batteryInfoTxt,color=rm.color('colorforError'))
                    if option == "show"and battery!=None:
                         await notification(ctx,client,txt=f"{'⚡' if battery.power_plugged else '🔋' } {battery.percent}% | Battery left: {convertTime(battery.secsleft)}",noti=False)
                    elif option=="show" and battery==None:
                         await notification(ctx,client,txt=batteryInfoTxt,noti=False)


              else:
                   await rm.msg(ctx,f"**Help - {p}battery level**\n\n**Commands:**\n```{p}batterylevel      -> Shows in Discord\n{p}batterylevel show -> Shows in PC```")

        else:
             await rm.msg(ctx,"**This feature is only available in Windows.**")
             
        await asyncio.sleep(1)

