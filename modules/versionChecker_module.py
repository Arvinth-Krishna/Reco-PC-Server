# Module: versionChecker
# Description: Here you can check the current verion of Reco PC Server and it's improvements.
# Usage: !version
# Dependencies: time, os

import os, asyncio, configs


currentVersionNo=4.1

print_log = '''_

**Your Current Reco PC Server Version: {0}**

**Updates**
Webhook and User Restricter feature added.

New !media commands also added.
!media say-vol
!media cv


_'''.format(currentVersionNo)




async def version(ctx):
     
        if configs.operating_sys == "Windows":
             
             await ctx.send("Getting Current Version Info.")
             info = "Reco_current_version_checker.txt"
             
             file = open(info, 'w')
             file.write(print_log)
             file.close()
             await ctx.send(print_log)
             os.system("start {0}".format(info))
             
        else:
             await ctx.send(print_log)
        await asyncio.sleep(3)
