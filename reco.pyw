# --------------- #
# Reco PC Server  |
# --------------- #
# Version No: 4.0 |
# --------------- #

# Basic bot dependencies
import discord
from discord.client import Client
from discord.ext.commands import Bot
import platform
import os

import asyncio
from threading import Thread

# Import configurations
import configs
from modules import restricter_module

# Import Restricters
from user_restricter import *
from webhook_restricter import *

# Import logger
from lib.helpers import Logger

# Imports for system tray icon
from pystray import Icon, Menu, MenuItem
from PIL import Image
import webbrowser

# Modules import - this imports all modules under the modules directory
# IDEs will complain about unresolved references, but it runs as intended
from modules import *

# Create a bot client with a description and a command prefix
client = Bot(description="A remote system administration bot for discord", command_prefix=configs.BOT_PREFIX)


@client.event
async def on_ready():
    print('--------')
    print('Reco PC Server Administration Bot by GAK')
    print('--------')
    print('Logged in as ' + client.user.name + ' (ID:' + str(client.user.id) + ') | Connected to '
          + str(len(client.guilds)) + ' servers | Connected to ' + str(len(set(client.get_all_members()))) + ' users')
    print('--------')
    print('Current Discord.py Version: {} | Current Python Version: {}'.format(
        discord.__version__, platform.python_version()))
    print('--------')
    print('Use this link to invite {}:'.format(client.user.name))
    print('https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8'.format(client.user.id))
    print('--------')
    print('Github Link: https://github.com/Arvinth-Krishna/Reco-PC-Server ')
    print('--------')
    print('Reco PC Server - Version N0: {0}'.format(versionChecker_module.currentVersionNo))
    print('--------')
    return await client.change_presence(activity=discord.Game(name='with your PC'))

# Module: restricter
# Description: To control both user and webhook commands permission
@client.event
async def on_message(message):
    await restricter_module.restricter(message,client)

  
# Module: abort
# Description: Abort the Shutdown or Restart schedule
# Usage: !abort 
@client.command()
@Logger(client)
async def abort(ctx):
    text="Aborting the schedule!"
    await notification_module.notification(ctx,text)
    await abort_module.abort(ctx)


# Module: appQuitter
# Description: Quits the application
# Usage: !appquitter "Application Name" or !appquitter "Application Name" minutesToQuit
@client.command()
@Logger(client)
async def appquitter(ctx, appName,minutes=0):
    text= str(appName).capitalize()+" will close in "+str(minutes)+" minutes"
    await notification_module.notification(ctx,text)
    await appQuitter_module.appquitter(ctx,appName, minutes)

    
# Module: batteryLevel
# Description: To see the estimated battery charge remaining
# Usage: !batterylevel
@client.command()
@Logger(client)
async def batterylevel(ctx):
    await batteryLevel_module.batterylevel(ctx)
    
 
# Module: batteryReportGenerator
# Description: Generates detailed report for your battery
# Usage: !batteryreport
@client.command()
@Logger(client)
async def batteryreport(ctx):
    await batteryReportGenerator_module.batteryreport(ctx)    

 
# Module: camera
# Description: Records a video or takes a photo (no audio)
# Usage: !camera command time
@client.command()
@Logger(client)
async def camera(ctx, command, time=5):
    await camera_module.camera(ctx, command, time)


# Module: cmd
# Description: Executes cmd command
# Usage: !cmd "command"
@client.command()
@Logger(client)
async def cmd(ctx, *txt):
    text=" ".join(txt)

    await cmd_module.cmd(ctx, text)


# Module: clipBoard
# Description: Copy to PC's Clipboard
# Usage: !clip txt
@client.command()
@Logger(client)
async def clip(ctx, *txt):
    text=" ".join(txt)

    await clip_module.clip(ctx, text)


# Module: echo
# Description: Turns command output display to discord chat on and off (works for !cmd and !powershell)
# Usage: !echo off or !echo on
@client.command()
@Logger(client)
async def echo(ctx, status):
    await echo_module.echo(ctx, status)


# Module: file
# Description: Allows file download, upload and system navigation
# Usage: !file [command] [[path]|[times]]
@client.command()
@Logger(client)
async def file(ctx, command, *args):
    await file_module.file(ctx, command, *args)


# Module: hibernate
# Description: Hibernates the system
# Usage: !hibernate or !hibernate secondsToHibernation
@client.command()
@Logger(client)
async def hibernate(ctx, minutes=0):
    text="System hibernates in "+str(minutes)+" minutes"
    await notification_module.notification(ctx,text)
    await hibernate_module.hibernate(ctx, minutes)


# Module: launch
# Description: Launches a shortcut in the shortcuts directory
# Usage: !launch [shortcut]
@client.command()
@Logger(client)
async def launch(ctx, *shortcut):
    fullLenShortcut=" ".join(shortcut)
    await launch_module.launch(ctx, fullLenShortcut)


# Module: lock
# Description: Locks system
# Usage: !lock or !lock minutesToLock
@client.command()
@Logger(client)
async def lock(ctx, minutes=0):
    await lock_module.lock(ctx, minutes)


# Module: log
# Description: Turns on of off logs in chat. Also can be used to retrieve Chimera execution logs
# Usage: !log [off|on] | [show] [date (format: YYYY-MM-DD)]
@client.command()
@Logger(client)
async def log(ctx, param, date=None):
    await log_module.log(ctx, param, date)


# Module: logoff
# Description: Logs the user out of the system
# Usage: !logoff or !logoff secondsToLogoff
@client.command()
@Logger(client)
async def logoff(ctx, minutes=0):
    text="System logout in "+str(minutes)+" minutes"
    await notification_module.notification(ctx,text)
    await logoff_module.logoff(ctx, minutes)


# Module: media
# Description: Controls Media Features
# Usage: !media command or !media command times
@client.command()
@Logger(client)
async def media(ctx, command, times=0):
    await media_module.media(ctx, command, times)

    
# Module: Music
# Description: Play video music from YouTube in VLC Player.
# Usage: !music query or !m query
@client.command()
@Logger(client)
async def music(ctx, *txt):
    text="+".join(txt)

     
    await music_module.music(ctx, text)  
    
@client.command()
@Logger(client)
async def m(ctx, *txt):
    text="+".join(txt)
   
    await music_module.music(ctx, text)      

    
# Module: notification
# Description: Sends a notification to the computer
# Usage: !notification "Notification Content"
@client.command()
@Logger(client)
async def notification(ctx, *txt):
    text=" ".join(txt)
 
    await notification_module.notification(ctx, text)


# Module: powershell
# Description: Executes powershell command
# Usage: !powershell "command"
@client.command()
@Logger(client)
async def powershell(ctx, *txt):
    text=" ".join(txt)

    await powershell_module.powershell(ctx, text)


# Module: restart
# Description: Restarts system
# Usage: !restart or !restart minutesToRestart
@client.command()
@Logger(client)
async def restart(ctx, minutes=0):
    text="System restart in "+str(minutes)+" minutes"
    await notification_module.notification(ctx,text)
    await restart_module.restart(ctx, minutes)


# Module: say
# Description: Uses powershell and a TTS engine to make your computer say something
# Usage: !say "Something to say"
@client.command()
@Logger(client)
async def say(ctx, *txt):
    text=" ".join(txt)
    await say_module.say(ctx, text)


# Module: screenshot
# Description: Takes a screenshot and sends it back
# Usage: !screenshot or !screenshot secondsToScreenshot
@client.command()
@Logger(client)
async def screenshot(ctx, seconds=0):
    await screenshot_module.screenshot(ctx, seconds)


# Module: search
# Description: Your query will be searched on Google.
# Usage: !search or !search query
@client.command()
@Logger(client)
async def search(ctx, *txt):
    text=''''''
    for txxt in txt: 
        text = text+"+"+txxt   
  
    await search_module.search(ctx, text)


# Module: shutdown
# Description: Shuts system down
# Usage: !shutdown or !shutdown minutesToShutdown
@client.command()
@Logger(client)
async def shutdown(ctx, minutes=0):
    text="System shutdown in "+str(minutes)+" minutes"
    await notification_module.notification(ctx,text)
    await shutdown_module.shutdown(ctx, minutes)


# Module: sleep
# Description: Puts system to sleep
# Usage: !sleep or !sleep minutesToSleep
@client.command()
@Logger(client)
async def sleep(ctx, minutes=0):
    text="System sleep in "+str(minutes)+" minutes"
    await notification_module.notification(ctx,text)
    await sleep_module.sleep(ctx, minutes)

    
# Module: systemInfo
# Description: Generates System Info
# Usage: !systeminfo
@client.command()
@Logger(client)
async def systeminfo(ctx):
    await systemInfo_module.systeminfo(ctx)
    

# Module: urlLauncher
# Description: Launch the website
# Usage: !url website
@client.command()
@Logger(client)
async def url(ctx, *txt):
    text=" ".join(txt)
    await urlLauncher_module.url(ctx, text)


# Module: versionChecker
# Description: Here you can check the current verion of Reco PC Server and it's improvements.
# Usage: !version
@client.command()
@Logger(client)
async def version(ctx):
    await versionChecker_module.version(ctx)
    

# Module: wlanSignal
# Description: To check the signal strength of a Wi-Fi Connection
# Usage: !wlansignal
@client.command()
@Logger(client)
async def wlansignal(ctx):
    await wlanSignal_module.wlansignal(ctx)

    
# Module: whatapp
# Description: Opens the chat Screen for the entered MobileNumber
# Usage: !whatsapp CountryCode_Followed_by_MobileNumber
@client.command()
@Logger(client)
async def whatsapp(ctx, num=0):
    await whatsapp_module.whatsapp(ctx, num)


# Module: youtube
# Description: Searches on YouTube.
# Usage: !youtube or !youtube search
@client.command()
@Logger(client)
async def youtube(ctx, *txt):
    text=''''''
    for txxt in txt: 
        text = text+"+"+txxt   
   
    await youtube_module.youtube(ctx, text)


# System Tray menu functions

# Starts the bot client
def iconRun():
    loop = asyncio.get_event_loop()
    loop.create_task(client.start(configs.BOT_TOKEN))
    t1=Thread(target=loop.run_forever)
    t1.start()


# Shows logs folder
def showLogs(): os.startfile("logs")


# Shows shortcuts folder
def showShortcuts(): os.startfile("shortcuts")

# Shows shortcuts folder
def showdownloads(): os.startfile("downloads")

# Opens bot invitation link in the browser
def connectInfo(): webbrowser.open(
    'https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8'.format(client.user.id))

# Opens webhook_restricter.py file
def open_Webhook_restricter(): os.startfile("webhook_restricter.py")

# Opens webhook_restricter.py file
def open_User_restricter(): os.startfile("user_restricter.py")

# Hides the application
def applicationHide():
    # This doesn't quit the bot client.
    # This merely stops the icon from showing on the taskbar.
    icon.visible = False
    icon.stop()
    client.logout()
   
# Exits the application
def applicationExit():
    # This will Force quit all the pythonw.exe program running in your computer
     os.system("taskkill /F /IM pythonw.exe")


# About
def about(): webbrowser.open('https://github.com/Arvinth-Krishna/Reco-PC-Server')


# Instructions
def instructions(): webbrowser.open('https://github.com/Arvinth-Krishna/Reco-PC-Server#features-documentation')


# Create system tray icon and start running the client
def iconSetup():
    iconImage = Image.open("Reco_logo.png")
    iconMenu = Menu(
        MenuItem("Connect", action=connectInfo, default=True),
        MenuItem("Instructions", action=instructions),
        MenuItem("Show Logs", action=showLogs),
        MenuItem("Show Shortcuts", action=showShortcuts),
        MenuItem("Show Downloads", action=showdownloads),
        MenuItem("User Restricter", action=open_User_restricter),
        MenuItem("Webhook Restricter", action=open_Webhook_restricter),
        MenuItem("Hide Icon", action=applicationHide),
        MenuItem("About", action=about),
        MenuItem("Force Quit",action=applicationExit),

    )
    icon = Icon('Reco', icon=iconImage, menu=iconMenu)
    return icon


# Application Entry Point - starts icon and bot client
icon = iconSetup()
iconRun()
icon.run()
