# Module: batteryReportGenerator
# Description: Generates detailed report for your battery.
# Usage: !batteryreport
# Dependencies: time, os

import os, time, asyncio, configs


async def batteryreport(ctx):
    await ctx.send("Generating Battery Report")

    if configs.operating_sys == "Windows":
        os.system('powercfg /batteryreport /output "./battery_report.html"')
        os.system('start battery_report.html')
        

    else:
        await ctx.send("Can't generate report. In Reco this feature is not added in for your platform")
        await asyncio.sleep(3)
