# Module: echo
# Description: Turns command output display to discord chat on and off (works for !cmd and !powershell)
# Usage: !echo off or !echo on
# Dependencies: ctypes

import ctypes
from lib.reco_embeds import recoEmbeds as rm
import configs




async def wake(ctx, option):
    
    if option == "on":
        print("Always On - Enabled")
        configs.WAKE_BOOL=True
        ctypes.windll.kernel32.SetThreadExecutionState(0x80000002)
        await rm.msg(ctx,"**!wake - Enabled**\n\nFYI, !wake on - goes back to your settings; if you quit Reco.")

    elif option == "off":
        print("Always On - Disabled")
        configs.WAKE_BOOL=False
        ctypes.windll.kernel32.SetThreadExecutionState(0x80000000)
        await rm.msg(ctx,"**!wake - Disabled**")
    elif option==None:
         await rm.msg(ctx,"**Parameter of !wake can be on or off.**\n\n**!wake on** - Keep Screen always on.\n**!wake off** - Resets (goes back to your Settings.)\n\n** FYI, !wake on will be disabled &  goes back to your setting if you quit Reco.**")

    