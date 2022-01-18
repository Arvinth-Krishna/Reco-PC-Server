# Module: say
# Description: Uses powershell and a TTS engine to make your computer say something
# Usage: !say "Something to say"
# Dependencies: time, os

import os, asyncio, configs
from lib.reco_embeds import recoEmbeds as rm


async def say(ctx, txt,noti=True):

    if configs.operating_sys == "Windows":
        if noti:
            await rm.msg(ctx,"**Saying**: " + txt)
        os.system(
            "powershell Add-Type -AssemblyName System.Speech; $synth = New-Object -TypeName System.Speech.Synthesis.SpeechSynthesizer; $synth.Speak('" + txt + "')")
    elif configs.operating_sys == "Linux":
        await rm.msg(ctx,"Saying: " + txt)
        os.system('spd-say "{}"'.format(txt))
    else:
        await ctx.send("Can't use TTS")
    await asyncio.sleep(3)
