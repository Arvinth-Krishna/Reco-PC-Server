# Module: media
# Description: Controls Media Features
# Usage: !media command or !media command times
# Dependencies: pynput, time, helpers, 

import asyncio, configs
from modules import say_module
from lib import helpers
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from lib.reco_embeds import recoEmbeds as rm



devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))


async def notify_alert_media_command_bool(bool):
    if configs.is_alert_bool:
        if not bool:
           await asyncio.sleep(4)
        configs.notify_alert_media_command=bool
    else:
        return
    


async def media(ctx, command, times=0,*time):
    await notify_alert_media_command_bool(True)
    p=configs.BOT_PREFIX
    if command==None:
        await rm.msg(ctx,f'''**Help - {p}media**\n
> **For Volume Up & Down Commands:**
  - **{p}media <command> <times> <time>**
  eg:
     **{p}media vol-up 10 2**
     Explaination: Volume up **10** times after **2** minutes.

> **For Other Commands:**
  - **{p}media <command> <time>**
  eg:
     **{p}media play 5**
     Explaination: Play command will execute after **5** minutes.

**Commands**:
```- {p}media <command> <times/time> <time>
- <times> and <time> are optional arguments.

{p}media vol-up
{p}media vol-down
{p}media vol-mute
{p}media say-cv      cv means Current Volume
{p}media cv
{p}media next
{p}media prev
{p}media stop
{p}media play
{p}media pause
{p}media key-tab
{p}media key-space
{p}media key-enter
{p}media key-up
{p}media key-down
{p}media key-left
{p}media key-right
{p}media key-close
{p}media key-quit```''')
        await notify_alert_media_command_bool(False)
        return
    p=configs.BOT_PREFIX
    timer=0
    minutesinmin=times
    media_control = helpers.MediaControlAdapter(configs.operating_sys)
    switcher = {
        'vol-up': media_control.up_volume,
        'vol-down': media_control.down_volume,
        'vol-mute': media_control.mute_volume,
        'next': media_control.media_next,
        'prev': media_control.media_previous,
        'stop': media_control.media_stop,
        'play': media_control.media_play_pause,
        'pause': media_control.media_play_pause,
        'key-tab':media_control.media_key_tab,
        'key-space':media_control.media_key_space,
        'key-up':media_control.media_key_up,
        'key-left':media_control.media_key_left,
        'key-right':media_control.media_key_right,
        'key-down':media_control.media_key_down,
        'key-enter':media_control.media_key_enter,
        'key-close':media_control.media_key_close,
        'key-quit':media_control.media_key_quit,
        'key-shuffle':media_control.media_key_shuffle,
        'key-loop':media_control.media_key_loop,
        'key-f':media_control.media_key_fullscreen,
        'key-mini':media_control.media_key_mini,
        'key-vlc-mute':media_control.media_key_vlc_mute,
        

    }

    if command not in switcher and command not in('say-cv','cv'):
        await notify_alert_media_command_bool(False)
        return 
    media_commands=['pause','play','stop','loop','vol-mute']
    bool_media_command=False

    for check in media_commands:
        if check == command:
            bool_media_command=True
            break
    if(command=="say-cv"or command=="cv"):
        bool_media_command=None


    if bool_media_command ==False:
        
        times=1 if times==0 else times
        if len(time)!=0:
            minutesinmin=time[0]
            timer=int(time[0])*60
        if timer !=0:
            await rm.msg(ctx,'Command: **{0} {1}** will be executed within **{2}** minutes'.format(command.capitalize(),times,time[0]))
            await notify_alert_media_command_bool(False)
            await asyncio.sleep(timer)
            await notify_alert_media_command_bool(True)
        else:
            if command in('vol-up','vol-down'):
              inform_msg=await rm.msg(ctx,f'**{"Increasing" if command=="vol-up" else "Decreasing"} your Volume{f"** (**{times}**)**.**" if times!=1 else ".**"}',color=rm.color("colorforWaitingMsg"))
            else:
              inform_msg=await rm.msg(ctx,f'Executing **{command}{f"** (**{times}**)**.**" if times!=1 else ".**"}',color=rm.color("colorforWaitingMsg"))

        for i in range(0, times):
            switcher[command]()
            await asyncio.sleep(0.5)
        currentVolume=(round(volume.GetMasterVolumeLevelScalar()*100))
        await notify_alert_media_command_bool(False)
        
    elif bool_media_command==None:
        if command=="say-cv":
            await say_module.say(ctx,txt=f"Current volume level is **{(round(volume.GetMasterVolumeLevelScalar()*100))}%**")
            await notify_alert_media_command_bool(False)
        elif command=="cv":
            await rm.msg(ctx,f"Current volume level is **{(round(volume.GetMasterVolumeLevelScalar()*100))}%**.")
            await notify_alert_media_command_bool(False)



    else:
        timer=times*60
        if timer !=0:
             await rm.msg(ctx,'Command: **{0}** will be executed within **{1}** minutes'.format(command.capitalize(),times))
             await notify_alert_media_command_bool(False)
             await asyncio.sleep(timer)
             await notify_alert_media_command_bool(True)
        switcher[command]()
        
        
        
    if command in ('vol-up','vol-down') or not bool_media_command and command not in('say-cv','cv'):
       if len(time)==0 :
           await inform_msg.delete()
       msg=await rm.msg(ctx,f"{f'(**Time is up! - {minutesinmin} mins**)' if len(time)!=0 else ''}\n\n**{p}{command}**{f' (**{times}**)' if times!=1 else ''} - Media Command Executed!!")
       
    elif command not in('say-cv','cv'):
        await rm.msg(ctx,f"{f'(**Time is up! - {minutesinmin} mins**)' if (minutesinmin!=0) else ''}\n\n**{p}{command}** - Media Command Executed!")
        await notify_alert_media_command_bool(False)
    await asyncio.sleep(0.8)
    if command in ('vol-up','vol-down'):
        await rm.editMsg(ctx,msg,f"{f'(**Time is up! - {minutesinmin} mins**)' if len(time)!=0 else ''}\n\n**{command}**{f' (**{times}**)' if times!=1 else ''} - **Media Adjusted!**\n\nCurrent volume level is **{currentVolume}%**.")
        await notify_alert_media_command_bool(False)


