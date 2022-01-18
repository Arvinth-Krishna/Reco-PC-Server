# Module: echo
# Description: Turns command output display to discord chat on and off (works for !cmd and !powershell)
# Usage: !echo off or !echo on
# Dependencies: None

import configs
from lib.reco_embeds import recoEmbeds as rm


async def echo(ctx, status):
    p=configs.BOT_PREFIX
    if status == "on":
        configs.initial_display_output = True
        await rm.msg(ctx,f"**{p}cmd and {p}powershell output will be displayed in chat.**")
    elif status == "off":
        configs.initial_display_output = False
        await rm.msg(ctx,f"**{p}cmd and {p}powershell output will be hidden from chat.**")
    else:
        await rm.msg(ctx,f"**Help - {p}echo**\n\n**Commands:**\n```{p}echo on\n{p}echo off```\n\n**FYI**,\n**If echo is on**, {p}cmd and {p}powershell output will be displayed in chat.")

    