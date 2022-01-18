# Module: abort
# Description: Abort the Shutdown or Restart schedule
# Usage: !abort
# Dependencies: os, asyncio

import os, asyncio, configs
from lib.reco_embeds import recoEmbeds as rm
from modules.notification_module import notification



async def abort(ctx,client):
    await rm.msg(ctx,"**Aborting the shutdown\\restart schedule!**")
    
    if configs.operating_sys == "Windows":  
        os.system("Shutdown.exe -a")
        text="Aborting the schedule!"
        await notification(ctx,client,text,noti=False)

    elif configs.operating_sys == "Linux":
        
        os.system("shutdown -c")
    else:
        await rm.msg(ctx,"Can't Abort the schedule.")
        await asyncio.sleep(3)
