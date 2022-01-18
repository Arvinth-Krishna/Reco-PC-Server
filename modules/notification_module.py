# Module: notification
# Description: Sends a notification to the computer
# Usage: !notification "Notification Content"
# Dependencies: plyer

import os
import asyncio
# from plyer import notification as notifier
from plyer import utils as plyerUtils
from lib.reco_embeds import recoEmbeds as rm
from win10toast import ToastNotifier


async def notification(ctx,client,txt,noti=True):
    if noti and txt!="":
        await rm.msg(ctx,"**Sending Notification:**\n\n" + txt)
    # Bypass plyer bug on macosx and use already included applescript
    if plyerUtils.platform == 'macosx':
        os.system("osascript -e 'display notification \"{}\"\'".format(txt))
    else:
        if txt!="":
            toaster = ToastNotifier()
            toaster.show_toast(client.user.name,
            txt,
            icon_path="icon.ico",
            duration=12)
            # notifier.notify(title=client.user.name,
            #         message=txt,
            #         app_name="Reco PC Server",
            #         app_icon="icon.ico",
            #         timeout=2)
        else:
            await rm.msg(ctx,"!notification **Please enter some text to show!**",color=rm.color('colorforError'))
    await asyncio.sleep(1)
