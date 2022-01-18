# Module: wlanSignal
# Description: To check the signal strength of a Wi-Fi Connection
# Usage: !wlansignal
# Dependencies: time, os

import os, asyncio
from lib.reco_embeds import recoEmbeds as rm


async def wlansignal(ctx):
    cmnd="netsh wlan show interfaces"
    msg=await rm.msg(ctx,"**Gathering Wlan Details**...")
    cmnd_result = os.popen(cmnd).read()
    await rm.extendableMsg(ctx,f"```{cmnd_result}```")
    await asyncio.sleep(0.5)
    await msg.delete()

    await asyncio.sleep(3)
