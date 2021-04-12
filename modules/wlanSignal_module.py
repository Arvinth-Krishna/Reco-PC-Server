# Module: wlanSignal
# Description: To check the signal strength of a Wi-Fi Connection
# Usage: !wlansignal
# Dependencies: time, os

import os, asyncio, configs


async def wlansignal(ctx):
    cmnd="netsh wlan show interfaces"
    await ctx.send("Executing in command prompt: " + cmnd)
    cmnd_result = os.popen(cmnd).read()
    await ctx.send(cmnd_result)
    os.system('cmd /c "netsh wlan show interfaces && timeout 25"')

    await asyncio.sleep(3)
