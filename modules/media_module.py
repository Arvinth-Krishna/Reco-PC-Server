# Module: media
# Description: Controls Media Features
# Usage: !media command or !media command times
# Dependencies: pynput, time, helpers

import asyncio, configs
from lib import helpers


async def media(ctx, command, times=1):
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
        'key-quit':media_control.media_key_quit

    }

    for time in range(0, times):
        switcher[command]()
        await asyncio.sleep(0.5)

    await ctx.send('Media Adjusted!')
