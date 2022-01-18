# Module: powershell
# Description: Executes powershell command
# Usage: !powershell "command"
# Dependencies: time, os

import os, asyncio, configs
from lib.helpers import boolConverter
from lib.reco_embeds import recoEmbeds as rm



async def powershell(ctx, cmnd):
    if configs.operating_sys == "Windows":
        await rm.msg(ctx,"**Executing in PowerShell:**\n\n" + cmnd)
        cmnd_result = os.popen("powershell {}".format(cmnd)).read()
        if boolConverter(configs.initial_display_output):
            if cmnd_result!="":
              await rm.extendableMsg(ctx,cmnd_result)
            else:
                await rm.msg(ctx,"**Opps!, No output to show.**",color=rm.color('colorforError'))
    else:
        await rm.msg(ctx,"Powershell is only available in Windows")
    await asyncio.sleep(3)
