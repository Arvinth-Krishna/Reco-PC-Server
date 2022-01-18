# Module: whatsapp
# Description: Opens the chat Screen for the entered MobileNumber
# Usage: !whatsapp CountryCode_Followed_by_MobileNumber
# Dependencies: time, os

from distutils.command.config import config
import os, asyncio, configs
from lib.reco_embeds import recoEmbeds as rm


async def whatsapp(ctx, num, platform):
    if configs.operating_sys in ("Windows","Linux"):
        p=configs.BOT_PREFIX
        if num==None:
            await rm.msg(ctx,f"**Help -{p}whatsApp**\n\n**Commands:**\n```{p}whatsapp web\n{p}whatsapp mobileNumber\n{p}whatsapp mobileNumber mobile```\n**eg:**\n{p}whatsapp 9195\*\*\*\*595\n\nFYI,\n**CountryCode_Followed_by_MobileNumber** must be **used**.")
        if num=='web' and platform=='pc':
            await rm.msg(ctx,"**Opening WhatsApp Web**...")
        elif num!=None and platform =='pc':
            await rm.msg(ctx,f"Opening chat screen for **[{num}](https://api.whatsapp.com/send?phone={num})**.")
        elif num!=None and platform =='mobile':
            await rm.msg(ctx,f"WhatsApp link for mobile: **[{num}](https://api.whatsapp.com/send?phone={num})**.")


    if configs.operating_sys == "Windows":
        if num=='web' and platform=='pc':
            os.system("start https://web.whatsapp.com/")
        elif num!=None and platform=='pc' :
            os.system(f"start https://api.whatsapp.com/send?phone={num}")
    elif configs.operating_sys == "Linux":
        if num=='web' and platform=='pc':
           os.popen(f'xdg-open https://web.whatsapp.com/')
        elif num!=None and platform=='pc' :
            os.popen(f'xdg-open https://api.whatsapp.com/send?phone={num}')
    else:
        await ctx.send("Not availale for this platform in Reco.")
        await asyncio.sleep(3)
