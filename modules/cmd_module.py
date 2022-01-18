# Module: cmd
# Description: Executes cmd command
# Usage: !cmd "command"
# Dependencies: os, asyncio

import os, asyncio, configs
from lib.reco_embeds import recoEmbeds as rm
from lib.helpers import boolConverter

async def cmd(ctx, cmnd):
    msg=await rm.msg(ctx,"**Executing in command prompt:**\n\n" + cmnd)
    cmnd_result = os.popen(cmnd).read() 

    if boolConverter(configs.initial_display_output):
        await rm.extendableMsg(ctx,'''```diff\n- Error!\n- The input is not recognized as an internal or external command.\n```''' if cmnd_result=="" and not (cmnd.__contains__('start') or cmnd.__contains__('cd')) else cmnd_result if cmnd_result!="" else '**Opps!, No output to show.**',color=rm.color('colorforError') if cmnd_result=="" else rm.color("colorforCommonMsg"))
    await asyncio.sleep(3)
