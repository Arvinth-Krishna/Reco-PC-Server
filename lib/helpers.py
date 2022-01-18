
import asyncio
from lib.input_commands import InputCommands
import configs,logging,os,sys
from datetime import datetime
from inspect import signature
import webhook_restricter as wr
import user_restricter as ur

reco_restart_bool=False

class Logger(object):

    DIRECTORY = 'logs'
    if not os.path.exists(DIRECTORY):
        os.makedirs(DIRECTORY)
    now = (datetime.now())
    logging.basicConfig(filename='{}/{}.txt'.format(DIRECTORY,now.strftime('%Y-%m-%d')))
    log = logging.getLogger()

    def __init__(self,client):
        self.client = client

    def __call__(self, f):
        
        async def run(*args, **kwargs):
            
            try:
                return await f(*args,**kwargs)
            except Exception as e:
                message = '{} - [{}] while executing [!{}] with params [{}] and named params [{}]'.format(self.now.strftime('%Y-%m-%d %H:%M:%S'),str(e),f.__name__,args,kwargs)
                if boolConverter(configs.DISK_LOGS_ENABLED):
                    self.log.error(message)
                if boolConverter(configs.discord_logs_enabled):
                    await self.client.say("`{}`".format(message))
                raise
                
        run.__name__ = f.__name__
        run.__signature__ = signature(f)
        return run
    
# def logger(f):
#     directory = 'logs'
#     if not os.path.exists(directory):
#         os.makedirs(directory)
#     now = (datetime.now())
#     logging.basicConfig(filename='{}/{}.txt'.format(directory,now.strftime('%Y-%m-%d')))
#     log = logging.getLogger()
#     
#     async def decorator(*args,**kwargs):
#         try:
#             return await f(*args,**kwargs)
#         except Exception as e:
#             message = '{} - [{}] while executing ![{}] with params [{}] and named params [{}]'.format(now.strftime('%Y-%m-%d %H:%M:%S'),str(e),f.__name__,args,kwargs)
#             if Configs.DISK_LOGS_ENABLED:
#                 log.error(message)
#             if Configs.discord_logs_enabled:
#                 await client.say(message)
#             raise
#     
#     decorator.__name__ = f.__name__
#     return decorator

def boolConverter(bool):
    if bool=="True":
        return True
    elif bool=="False":
        return False
    elif bool:
        return True
    elif not bool:
        return False

def checkfolder():
    if not os.path.isdir('downloads'):
            os.mkdir("./downloads")  
    if not os.path.isdir('shortcuts'):
        os.mkdir("./shortcuts")  
def savefoldercheck():
    if not os.path.isdir('downloads'):
            os.mkdir("./downloads")  
    if not os.path.isdir('downloads/saved_files'):
        os.mkdir("./downloads/saved_files")  

        


class recoCount():
    def get_reco_user_count(client):
        user_set = set()
        for guild in client.guilds:
            for member in guild.members:
                if not member.bot:
                    user_set.add(member)
        return len(user_set)

    def get_reco_bot_count(client):
        bot_set = set()
        for guild in client.guilds:
            for member in guild.members:
                if member.bot:
                    bot_set.add(member)
        return len(bot_set)-1
    
    def get_reco_total_member_count(client):
        total_member_set = set()
        for guild in client.guilds:
            for member in guild.members:
                total_member_set.add(member)
        return len(total_member_set)-1
    
    def get_reco_block_user_count():
        return len(ur.blocked_users_Id_list)

    def get_reco_block_webhook_count(): 
        return len(wr.blocked_webhooks_Id_list)
    
    
    


def get_operating():
    platforms = {
        'linux': 'Linux',
        'linux1': 'Linux',
        'linux2': 'Linux',
        'darwin': 'OS X',
        'win32': 'Windows'
    }
    if sys.platform not in platforms:
        return sys.platform

    return platforms[sys.platform]

class MediaControlAdapter():
    VK_VOLUME_DOWN = 0
    VK_VOLUME_UP = 1
    VK_VOLUME_MUTE = 2
    VK_MEDIA_NEXT_TRACK = 3
    VK_MEDIA_PREV_TRACK = 4
    VK_MEDIA_STOP = 5
    VK_MEDIA_PLAY_PAUSE = 6
    VK_KEY_TAB = 7
    VK_KEY_SPACE = 8
    VK_KEY_UP = 9
    VK_KEY_LEFT = 10
    VK_KEY_RIGHT = 11
    VK_KEY_DOWN = 12
    VK_KEY_ENTER = 13
    VK_KEY_CTRL = 14
    VK_KEY_F4 = 15
    VK_KEY_W = 16
    VK_KEY_ALT = 17
    VK_KEY_M=18
    VK_KEY_L=19
    VK_KEY_F = 20
    VK_KEY_R=21
    VK_KEY_THREE=22
    VK_KEY_WIN=19
    VK_KEY_X = 20
    VK_KEY_U=21
    VK_KEY_S=22
    
    
    
    _command_list = {
        'Linux':{
            VK_VOLUME_MUTE:269025042,
            VK_VOLUME_DOWN:269025041,
            VK_VOLUME_UP:269025043,
            VK_MEDIA_NEXT_TRACK:269025047,
            VK_MEDIA_PREV_TRACK:269025046,
            VK_MEDIA_STOP:269025045,
            VK_MEDIA_PLAY_PAUSE:269025044,
            VK_KEY_TAB:65289

        },
        'Windows':{
            VK_VOLUME_MUTE:173,
            VK_VOLUME_DOWN:174,
            VK_VOLUME_UP:175,
            VK_MEDIA_NEXT_TRACK:176,
            VK_MEDIA_PREV_TRACK:177,
            VK_MEDIA_STOP:178,
            VK_MEDIA_PLAY_PAUSE:179,
            VK_KEY_TAB:9,
            VK_KEY_SPACE:32,
            VK_KEY_UP:38,
            VK_KEY_LEFT:37,
            VK_KEY_RIGHT:39,
            VK_KEY_DOWN:40,
            VK_KEY_ENTER:13,
            VK_KEY_CTRL:17,
            VK_KEY_F4:115,
            VK_KEY_W:87,
            VK_KEY_ALT:18,
            VK_KEY_M:77,
            VK_KEY_L:76,
            VK_KEY_F:70,
            VK_KEY_R:82,
            VK_KEY_THREE:51,
            VK_KEY_WIN:92,
            VK_KEY_X:88,
            VK_KEY_U:85,
            VK_KEY_S:83,
            
        }
    }
    
    def __init__(self,os_name):
        self.os_name = os_name
        self.input_commands = InputCommands()
        
    def up_volume(self):
        virtual_key_id = self._command_list[self.os_name][self.VK_VOLUME_UP]
        self.input_commands.press_release(virtual_key_id)
    def down_volume(self):
        virtual_key_id = self._command_list[self.os_name][self.VK_VOLUME_DOWN]
        self.input_commands.press_release(virtual_key_id)
    def mute_volume(self):
        virtual_key_id = self._command_list[self.os_name][self.VK_VOLUME_MUTE]
        self.input_commands.press_release(virtual_key_id)
    def media_next(self):
        virtual_key_id = self._command_list[self.os_name][self.VK_MEDIA_NEXT_TRACK]
        self.input_commands.press_release(virtual_key_id)
    def media_previous(self):
        virtual_key_id = self._command_list[self.os_name][self.VK_MEDIA_PREV_TRACK]
        self.input_commands.press_release(virtual_key_id)
    def media_stop(self):
        virtual_key_id = self._command_list[self.os_name][self.VK_MEDIA_STOP]
        self.input_commands.press_release(virtual_key_id)
    def media_play_pause(self):
        virtual_key_id = self._command_list[self.os_name][self.VK_MEDIA_PLAY_PAUSE]
        self.input_commands.press_release(virtual_key_id)
    def media_key_tab(self):
        virtual_key_id = self._command_list[self.os_name][self.VK_KEY_TAB]
        self.input_commands.press_release(virtual_key_id)
    def media_key_space(self):
        virtual_key_id = self._command_list[self.os_name][self.VK_KEY_SPACE]
        self.input_commands.press_release(virtual_key_id)
    def media_key_up(self):
        virtual_key_id = self._command_list[self.os_name][self.VK_KEY_UP]
        self.input_commands.press_release(virtual_key_id)
    def media_key_left(self):
        virtual_key_id = self._command_list[self.os_name][self.VK_KEY_LEFT]
        self.input_commands.press_release(virtual_key_id)
    def media_key_right(self):
        virtual_key_id = self._command_list[self.os_name][self.VK_KEY_RIGHT]
        self.input_commands.press_release(virtual_key_id)
    def media_key_down(self):
        virtual_key_id = self._command_list[self.os_name][self.VK_KEY_DOWN]
        self.input_commands.press_release(virtual_key_id)
    def media_key_enter(self):
        virtual_key_id = self._command_list[self.os_name][self.VK_KEY_ENTER]
        self.input_commands.press_release(virtual_key_id) 
    def media_key_close(self):
        virtual_key_id = self._command_list[self.os_name][self.VK_KEY_CTRL]
        virtual_key_id2 = self._command_list[self.os_name][self.VK_KEY_W]
        self.input_commands.hold_release(virtual_key_id,virtual_key_id2)
    def media_key_quit(self):
        virtual_key_id = self._command_list[self.os_name][self.VK_KEY_ALT]
        virtual_key_id2 = self._command_list[self.os_name][self.VK_KEY_F4]
        self.input_commands.hold_release(virtual_key_id,virtual_key_id2)
    def media_key_loop(self):
        virtual_key_id = self._command_list[self.os_name][self.VK_KEY_ALT]
        virtual_key_id2 = self._command_list[self.os_name][self.VK_KEY_L]
        self.input_commands.hold_release(virtual_key_id,virtual_key_id2)
    def media_key_shuffle(self):
        virtual_key_id = self._command_list[self.os_name][self.VK_KEY_ALT]
        virtual_key_id2 = self._command_list[self.os_name][self.VK_KEY_R]
        self.input_commands.hold_release(virtual_key_id,virtual_key_id2)
    def media_key_fullscreen(self):
        virtual_key_id = self._command_list[self.os_name][self.VK_KEY_ALT]
        virtual_key_id2 = self._command_list[self.os_name][self.VK_KEY_F]
        self.input_commands.hold_release(virtual_key_id,virtual_key_id2)
    def media_key_mini(self):
        virtual_key_id = self._command_list[self.os_name][self.VK_KEY_ALT]
        virtual_key_id2 = self._command_list[self.os_name][self.VK_KEY_THREE]
        self.input_commands.hold_release(virtual_key_id,virtual_key_id2)
    def media_key_vlc_mute(self):
        virtual_key_id = self._command_list[self.os_name][self.VK_KEY_M]
        self.input_commands.press_release(virtual_key_id) 
    async def win_sleep(self):
        virtual_key_id = self._command_list[self.os_name][self.VK_KEY_WIN]
        virtual_key_id2 = self._command_list[self.os_name][self.VK_KEY_X]
        self.input_commands.hold_release(virtual_key_id,virtual_key_id2)
        await asyncio.sleep(0.5)
        virtual_key_id = self._command_list[self.os_name][self.VK_KEY_U]
        self.input_commands.press_release(virtual_key_id)
        virtual_key_id = self._command_list[self.os_name][self.VK_KEY_S]
        self.input_commands.press_release(virtual_key_id)
        


