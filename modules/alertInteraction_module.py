# Module: alert 
# Description: Alerts user interaction.
# Usage: !alert on or !alert off or !alert onwithbeep
# Dependencies: asyncio, socket, random


import configs,asyncio
from playsound import playsound
from lib.helpers import MediaControlAdapter, get_idle_duration
from lib.reco_embeds import recoEmbeds as rm
from modules import alertInteraction_module
from socket import gethostname
from random import choice
from modules.media_module import volume

alert_bool=False
alert_withmsg_bool=False
alert_withbeep_bool=False

async def checkVolume():
    while True:
            if (round(volume.GetMasterVolumeLevelScalar()*100))<=int(configs.BEEP_MINUMUM_VOLUME):
                configs.notify_alert_media_command=True
                while (round(volume.GetMasterVolumeLevelScalar()*100))<=int(configs.BEEP_MINUMUM_VOLUME):
                    MediaControlAdapter.up_volume(MediaControlAdapter(configs.operating_sys))
                    await asyncio.sleep(0.1)
                configs.notify_alert_media_command=False
            if alert_bool:
                break
            await asyncio.sleep(1)

async def startAlert(ctx,beep=False): 
    if beep:
        asyncio.create_task(checkVolume())
       
    
    dontList=[f"**Hey, I got a sense. 👀 Someone is using your system**(**{gethostname()}**).",f"⚠ **Found some user interaction in your system**(**{gethostname()}**).",f"⚠ **Beware, your system**(**{gethostname()}**) **in use!**"]

    alertInteraction_module.alert_bool=False
    while True:
        if alert_bool:
            break

        print(f"{(round(volume.GetMasterVolumeLevelScalar()*100))}%")
        print(configs.notify_alert_media_command)
        if get_idle_duration()<0.3 and not configs.notify_alert_media_command:
            await rm.msg(ctx,choice(dontList))
            if beep:
                playsound(f'{configs.RECO_PATH}/lib/alert_beep.mp3')
            await asyncio.sleep(2)
        elif configs.notify_alert_media_command:
            await asyncio.sleep(3)
        else:
             await asyncio.sleep(0.5)


async def alert(ctx,options):
    p=configs.BOT_PREFIX
    if configs.operating_sys == "Windows":
        if options=="on":
            if not configs.is_alert_bool:
                alertInteraction_module.alert_withmsg_bool=True
                await rm.msg(ctx,"**Alert mode is turned ON** (**Message Mode**).")
                configs.is_alert_bool=True
                asyncio.create_task(startAlert(ctx))
            else:
                 await rm.msg(ctx,f"**Alert with {'Message Mode' if alert_withmsg_bool else 'Message & Beep Mode'} is already ON.**")

        elif options=="onwithbeep":
            if not configs.is_alert_bool:
                alertInteraction_module.alert_withbeep_bool=True
                await rm.msg(ctx,"**Alert mode is turned ON** (**Message & Beep Mode**).")
                configs.is_alert_bool=True
                asyncio.create_task(startAlert(ctx,beep=True))
            else:
                 await rm.msg(ctx,f"**Alert with {'Message Mode' if alert_withmsg_bool else 'Message & Beep Mode'} is already ON.**")
        elif options=="off":
            configs.is_alert_bool=False
            await rm.msg(ctx,f"**Alert mode is turned OFF** (**{'Message Mode' if alert_withmsg_bool else 'Message & Beep Mode'}**).")
            alertInteraction_module.alert_bool=True
        else:
            await rm.msg(ctx,f'**Help - {p}alert**\n\n**Commands:**\n```{p}alert  on\n{p}alert  onwithbeep\n{p}alert  off```\n')

        

    else:
        await ctx.send("Currently, this feature is not available in your platform.")
        await asyncio.sleep(3)
