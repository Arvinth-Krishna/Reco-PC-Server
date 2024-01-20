# Load configuration parameters
from pathlib import Path
from dotenv import load_dotenv
import os, lib.helpers,datetime,time,custom_rich_presence as crp
from recoVersion import RECO_VERSION_NO

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

# Don't edit any thing in the file (configs.py), Please use env file.

# -----------------------------------------------
begin_time = datetime. datetime. now()
mk_time= time.mktime(time.localtime())
WAKE_BOOL = False
rpc_started=False
desktop_discord_client=False
is_alert_bool=False
notify_alert_media_command=False
# -----------------------------------------------

RECO_VERSION_NO = RECO_VERSION_NO

BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')

BOT_PREFIX = os.getenv('DISCORD_BOT_PREFIX', '!')

RECO_PATH = os.getcwd()
# -----------------------------------------------

# Reco Online Notifier
RECO_ONLINE_NOTIFIER = os.getenv('RECO_ONLINE_NOTIFIER',default= True)
# -----------------------------------------------

# Update Notifier
UPDATE_NOTIFIER = os.getenv('UPDATE_NOTIFIER','True')

UPDATE_NOTIFIER_INTERVAL = os.getenv('UPDATE_NOTIFIER_INTERVAL',8)
# -----------------------------------------------

# Alert Command
SHOW_DND_BOT_STATUS= os.getenv('SHOW_DND_BOT_STATUS',True)
BEEP_MINUMUM_VOLUME= os.getenv('BEEP_MINUMUM_VOLUME',20)
# -----------------------------------------------

# Rich Presence
RPC_BOOL= os.getenv('RPC_BOOL',False)
SHOW_PC_STATUS_IN_CPU_USAGE= os.getenv('SHOW_PC_STATUS_IN_CPU_USAGE',False)
# -----------------------------------------------

# Bot Status
DYNAMIC_BOT_STATUS= os.getenv('DYNAMIC_BOT_STATUS',True)
SHOW_IDLE_STATUS_IN_MINS= os.getenv('SHOW_IDLE_STATUS_IN_MINS',2)
# -----------------------------------------------

# Custom Rich Presence
ENABLE_CUSTOM_RICH_PRESENCE =crp.ENABLE_CUSTOM_RICH_PRESENCE

SHOW_RECO_RP =crp.SHOW_RECO_RP
SHOW_CPU_USAGE_RP =crp.SHOW_CPU_USAGE_RP
CUSTOM_RP_ACTIVITY =crp.CUSTOM_RP_ACTIVITY
# -----------------------------------------------

# Restricters
ALLOW_ADMINS = os.getenv('ALLOW_ADMINS','True')

RECO_OWNER_USER_ID = os.getenv('RECO_OWNER_USER_ID','0000000000')

ALLOW_ALL_USERS = os.getenv('ALLOW_ALL_USERS','True')

ALLOW_ALL_WEBHOOKS = os.getenv('ALLOW_ALL_WEBHOOKS','True')

LIMIT_ALL_USER_COMMAND = os.getenv('LIMIT_ALL_USER_COMMAND','False')
# -----------------------------------------------

# Embeds

DEFAULT_EMBEDS_COLOR = os.getenv('DEFAULT_EMBEDS_COLOR',0xf5c816)

SECONDARY_EMBEDS_COLOR = os.getenv('SECONDARY_EMBEDS_COLOR',0xF19306)
# -----------------------------------------------

# File Upload Size
FILE_UPLOAD_SIZE = os.getenv('FILE_UPLOAD_SIZE',8.3)
# -----------------------------------------------

# Printer
CURRENT_PRINTER_NUMBER = os.getenv('CURRENT_PRINTER_NUMBER', None)       # !printer showprinters 

NO_OF_COPIES = os.getenv('NO_OF_COPIES',1)

COLOR_MODE = os.getenv('COLOR_MODE', 'b')                                # b -> Black   and c -> Color

ORIENTATION = os.getenv('ORIENTATION','p')                               # p -> Potrait and l -> Landscape
# -----------------------------------------------

# Others
CHANNEL_ID = os.getenv('DISCORD_CHANNEL_ID')

PYTHON_ALIAS = os.getenv('PYTHON_ALIAS', 'python')

DISK_LOGS_ENABLED = os.getenv('DISK_LOGS_ENABLED', 'True')

initial_display_output = os.getenv('INITIAL_DISPLAY_OUTPUT', 'True')

initial_path = os.getenv('INITIAL_PATH')

discord_logs_enabled = os.getenv('DISCORD_LOGS_ENABLED', 'False')

operating_sys = lib.helpers.get_operating()
# -----------------------------------------------
