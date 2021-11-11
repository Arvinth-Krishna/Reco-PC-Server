# Module: versionChecker
# Description: Here you can check the current verion of Reco PC Server and it's improvements.
# Usage: !version
# Dependencies: time, os

import os, asyncio, configs


currentVersionNo=3.1

print_log = '''_

**Your Current Reco PC Server Version: {0}**

**Updates**
Timer feature for "Pause", "Play", "Stop" added.
!media play <minutes>

eg:
!media pause 10

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
