# Module: media
# Description: Controls Media Features
# Usage: !media command or !media command times
# Dependencies: pynput, time, helpers

import asyncio, configs
from modules import say_module
from lib import helpers
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

async def media(ctx, command, times):
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

    
    media_commands=['pause','play','stop','loop','mute']
    bool_media_command=False

    for check in media_commands:
        if check == command:
            bool_media_command=True
            break
    if(command=="say-vol"or command=="cv"):
        bool_media_command=None


    if bool_media_command ==False:
        
        times=1 if times==0 else times
        for time in range(0, times):
             switcher[command]()
             await asyncio.sleep(0.5)
    elif bool_media_command==None:
        if command=="say-vol":
            await say_module.say(ctx,txt=f"Current volume level is {(round(volume.GetMasterVolumeLevelScalar()*100))}%")
        elif command=="cv":
            await ctx.send(f"Current volume level is **{(round(volume.GetMasterVolumeLevelScalar()*100))}%**.")


    else:
        timer=times*60
        if timer !=0:
             await ctx.send('Command: {0} will be executed within {1} minutes'.format(command,times))
        await asyncio.sleep(timer)
        
        switcher[command]()
        
    if(command=="vol-up"or command=="vol-down"):
        await ctx.send(f"Current volume level is **{(round(volume.GetMasterVolumeLevelScalar()*100))}%**.")
        
    if(bool_media_command==True or command=="vol-up"or command=="vol-down" or command=='vol-mute'):
        await ctx.send('Media Adjusted!')
    elif (bool_media_command!=None):
        await ctx.send('Media Command Executed!')


