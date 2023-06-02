# Module: mouse
# Description: Controls Mouse Movements
# Usage: !mouse or !mouse command time
# Dependencies: time, os

import os, asyncio, configs
import pyautogui
from lib.reco_embeds import recoEmbeds as rm
from modules.notification_module import notification



async def mouse(ctx,action, duration=0,distance=1):

    """
    Perform mouse actions such as moving the cursor and clicking.

    Args:
    - action (str): The mouse action to perform. Possible values are 'up', 'down', 'left', 'right', 'left_click', and 'right_click'.
    - duration (float, optional): The duration (in seconds) for which to perform the action. Default is 0.

    Note:
    - The 'up', 'down', 'left', and 'right' actions move the mouse cursor by a small distance.
    - The 'left_click' and 'right_click' actions simulate a left or right mouse click.
    - The 'duration' parameter is only used for actions that require a duration, such as moving the cursor.

    Example usage:
    - mouse('up') -> Move the mouse cursor up by a small distance.
    - mouse('left_click') -> Simulate a left mouse click.
    - mouse('right', 2.5) -> Move the mouse cursor to the right continuously for 2.5 seconds.
    """

    

    if configs.operating_sys == "Windows":
        if action == 'up':
            color=rm.color('colorforCommonMsg')
            await rm.msg(ctx,f"**Moving mouse up{f'** for **{duration}** seconds.' if duration>1 else'.**'}",color=color)
            pyautogui.move(0, distance*-50, duration=duration)

        elif action == 'down':
            color=rm.color('colorforCommonMsg')
            await rm.msg(ctx,f"**Moving mouse down{f'** for **{duration}** seconds.' if duration>1 else'.**'}",color=color)
            pyautogui.move(0, distance*50, duration=duration)

        elif action == 'left':
            color=rm.color('colorforCommonMsg')
            await rm.msg(ctx,f"**Moving mouse left{f'** for **{duration}** seconds.' if duration>1 else'.**'}",color=color)
            pyautogui.move(distance*-50, 0, duration=duration)

        elif action == 'right':
            color=rm.color('colorforCommonMsg')
            await rm.msg(ctx,f"**Moving mouse right{f'** for **{duration}** seconds.' if duration>1 else'.**'}",color=color)
            pyautogui.move(distance*50, 0, duration=duration)

        elif action == 'left-click':
            color=rm.color('colorforCommonMsg')
            await rm.msg(ctx,"**Mouse left_click pressed**",color=color)
            pyautogui.click(button='left')

        elif action == 'right-click':
            color=rm.color('colorforCommonMsg')
            await rm.msg(ctx,"**Mouse right_click pressed**",color=color)
            pyautogui.click(button='right')
        elif action=="":
            p=configs.BOT_PREFIX
            await rm.msg(ctx,txt=f'''**Help - {p}mouse <direction> <duration> <distance>**\n\n**Commands:**
```{p}mouse <up/down/left/right>
{p}mouse <up/down/left/right> <duration_in_seconds>
{p}mouse <up/down/left/right> <duration_in_seconds> <distance*offset(50)>
```

**Example:**
```
{p}mouse up
{p}mouse up 5
{p}mouse up 5 10```

**FYI**,
🔸 [YouTube video coming soon!](https://www.youtube.com/channel/UCKU73B2c4FBl8o4b1qBBPxA)
''')

    elif configs.operating_sys == "Linux":
        await ctx.send("Currently mouse feature not added in linux.")
    else:
        await ctx.send("Currently mouse feature not added in linux.")
        await asyncio.sleep(3)
