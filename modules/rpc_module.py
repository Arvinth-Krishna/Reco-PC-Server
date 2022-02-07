# Module: rpc
# Description: Starts the Rich Presence
# Usage: !rpc or !rpc start or !rpc stop
# Dependencies: asyncio

import asyncio, configs
from lib.reco_embeds import recoEmbeds as rm
from custom_rich_presence import ENABLE_CUSTOM_RICH_PRESENCE as crpbool
from lib.updatePresence_helper import reco_rpc
from lib.helpers import boolConverter


async def rpc(ctx,client,option=None):
    p=configs.BOT_PREFIX
    
        
    
    if configs.operating_sys == "Windows":
        txt= "Custom" if crpbool else "Reco"
        if option==None:
            await rm.msg(ctx,f"**Help - {p}rpc**\n\n**Commands:**\n```{p}rpc start\n{p}rpc stop```\n\n**Current Status**,\nRPC Enabled: **{configs.RPC_BOOL}**\nCustom RPC Enabled: **{configs.ENABLE_CUSTOM_RICH_PRESENCE}**")
        if (boolConverter(configs.RPC_BOOL) and not configs.desktop_discord_client) and option!="stop":
            return
        if option == "start" :
            if not configs.rpc_started:
               await rm.msg(ctx,f"**Starting {txt} Rich Presence!**",color=0x50C878)
               await reco_rpc(client)
            else:
                if boolConverter(configs.RPC_BOOL):
                    await rm.msg(ctx,f"FYI,\nYour **{txt} Rich Presence** is **currently running!**\n\nBut if you can't see, please use\n**{p}rpc restart**",color=rm.color('colorforWaitingMsg'))
                else:
                    await rm.msg(ctx,f"**Please try again later**...\n\nCurrent process:\n**Quitting {txt} Rich Presence!**")

            
        elif option == "stop" :
            await rm.msg(ctx,f"**Quitting {txt} Rich Presence!**",color=rm.color('colorforError'))
            configs.RPC_BOOL=False
        elif option == "restart":
            await rpc(ctx,client,'stop')
            while True:
                if not configs.rpc_started:
                    break
                await asyncio.sleep(5)
            await rpc(ctx,client,'start')
                    

    else:
        await ctx.send("This command is not currently available in your platform.")
        await asyncio.sleep(1)
