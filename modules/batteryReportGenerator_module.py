# Module: batteryReportGenerator
# Description: Generates detailed report for your battery.
# Usage: !batteryreport
# Dependencies: os, asyncio, discord

import os, asyncio, configs, discord
from lib.reco_embeds import recoEmbeds as rm


async def batteryreport(ctx,option=None):
    p=configs.BOT_PREFIX
    

    if configs.operating_sys == "Windows":
        msg=""
        if option in(None,'file'):
           msg=await rm.msg(ctx,"**Generating your Battery Report!**",color=rm.color('colorforWaitingMsg'))
           os.system('powercfg /batteryreport /output "./battery_report.html"')
           if option==None:
               await rm.editMsg(ctx,msg,"**Opening Battery Report in your system.**",color=0x00BB00)
               os.system('start battery_report.html')
           await ctx.send(file=discord.File('battery_report.html'))
           await rm.editMsg(ctx,msg,"**Battery Report is ready to download! ⭳**\n\n**FYI**, Open the file using **browser**.")
        
        if option not in (None,'file'):
            await rm.msg(ctx,f"**Help - {p}batteryreport**\n\n**Commands:**\n```{p}batteryreport      -> Shows report\n{p}batteryreport file -> Sends file only```")
                                                                                


    else:
        await rm.msg(ctx,"Can't generate report. In Reco this feature is not added in for your platform")
        await asyncio.sleep(3)
