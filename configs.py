# Load configuration parameters
from pathlib import Path
from dotenv import load_dotenv
import os, lib.helpers
from recoVersion import RECO_VERSION_NO

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


RECO_VERSION_NO = RECO_VERSION_NO

BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')

BOT_PREFIX = os.getenv('DISCORD_BOT_PREFIX', '!')

RECO_PATH = os.getcwd()

# Reco Online Notifier
RECO_ONLINE_NOTIFIER = os.getenv('RECO_ONLINE_NOTIFIER',default= True)

# Update Notifier

UPDATE_NOTIFIER = os.getenv('UPDATE_NOTIFIER','True')

UPDATE_NOTIFIER_INTERVAL = os.getenv('UPDATE_NOTIFIER_INTERVAL',8)

# Features
WAKE_BOOL = False

# Restricters
ALLOW_ALL_USERS = os.getenv('ALLOW_ALL_USERS','True')

ALLOW_ALL_WEBHOOKS = os.getenv('ALLOW_ALL_WEBHOOKS','True')

# Embeds

EMBEDS_COLOR = os.getenv('DEFAULT_EMBEDS_COLOR',0xf5c816)

SECONDARY_EMBEDS_COLOR = os.getenv('SECONDARY_EMBEDS_COLOR',0xF19306)

# File Upload Size
FILE_UPLOAD_SIZE = os.getenv('FILE_UPLOAD_SIZE',8.3)

# Printer
CURRENT_PRINTER_NUMBER = os.getenv('CURRENT_PRINTER_NUMBER', None)       # !printer showprinters 

NO_OF_COPIES = os.getenv('NO_OF_COPIES',1)

COLOR_MODE = os.getenv('COLOR_MODE', 'b')                                # b -> Black   and c -> Color

ORIENTATION = os.getenv('ORIENTATION','p')                               # p -> Potrait and l -> Landscape

# Others
CHANNEL_ID = os.getenv('DISCORD_CHANNEL_ID')

PYTHON_ALIAS = os.getenv('PYTHON_ALIAS', 'python')

DISK_LOGS_ENABLED = os.getenv('DISK_LOGS_ENABLED', 'True')

initial_display_output = os.getenv('INITIAL_DISPLAY_OUTPUT', 'True')

initial_path = os.getenv('INITIAL_PATH')

discord_logs_enabled = os.getenv('DISCORD_LOGS_ENABLED', 'False')

operating_sys = lib.helpers.get_operating()

