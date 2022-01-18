# Module: camera
# Description: Records a video or takes a photo (no audio)
# Usage: !camera command time
# Dependencies: os, discord

import os, configs, discord
from lib.reco_embeds import recoEmbeds as rm

async def camera(ctx,*commandtime):
    command=None
    time=5
    if len(commandtime)>=2:
        time= commandtime[1]
        command=commandtime[0]
    elif len(commandtime)==1:
        command=commandtime[0]
    p=configs.BOT_PREFIX
    python_alias = configs.PYTHON_ALIAS

    if command == 'photo':
        # CameraControl.photo_capture()
        await rm.msg(ctx,'**Taking Photo!**')
        os.system("{} lib/camera_control.py photo".format(python_alias))  # workaround
        await ctx.send(file=discord.File('photo.jpg'))

    elif command == 'video':
        if str(time).isnumeric():
            # await CameraControl.video_capture(time=time)
            await rm.msg(ctx,'**Recording!**')
            os.system("{} lib/camera_control.py video {}".format(python_alias, time))  # workaround
            await ctx.send(file=discord.File('video.avi'))
        else:
            await rm.msg(ctx,"**❌ Invalid time input!**",color=rm.color('colorforError'))
    
    elif command not in ('photo','video'):
        await rm.msg(ctx,f"**Help - {p}camera**\n\n**Commands:**\n```{p}camera photo       -> To take photo\n{p}camera video Sec   -> To take video```")
                                             
    