# --------------- #
# Reco PC Server  |
# --------------- #
# Version No: 6.0 |
# --------------- #

# Basic bot dependencies
import discord
from discord.ext.commands import Bot
import platform
import os

import asyncio
from threading import Thread

# Import configurations
import configs

# Import helpers
from lib.helpers import Logger, boolConverter
from lib.helpers import recoCount
from lib.reco_startup import startup_Initializer
from modules import alertInteraction_module, rpc_module

# Imports for system tray icon
from pystray import Icon, Menu, MenuItem
from PIL import Image
import webbrowser

# Modules import - this imports all modules under the modules directory
# IDEs will complain about unresolved references, but it runs as intended
from modules import *
from modules import signout_module


# Create a bot client with a description and a command prefix
intents = discord.Intents.default()
intents.members = True
client = Bot(description="A remote system administration bot for discord", command_prefix=configs.BOT_PREFIX,intents=intents)

@Logger(client)
@client.event
async def on_ready():
    print('--------')
    print('Reco PC Server Administration Bot by GAK')
    print('--------')
    print('Logged in as ' + client.user.name + ' (ID:' + str(client.user.id) + ') | Connected to '
          + str(len(client.guilds)) + ' servers | Connected to ' + str(recoCount.get_reco_user_count(client)) + ' users')
    print('--------')
    print('Current Discord.py Version: {} | Current Python Version: {}'.format(
        discord.__version__, platform.python_version()))
    print('--------')
    print('Use this link to invite {}:'.format(client.user.name))
    print('https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8'.format(client.user.id))
    print('--------')
    print('Github Link: https://github.com/Arvinth-Krishna/Reco-PC-Server ')
    print('--------')
    print('Reco PC Server - Version N0: {0}'.format(configs.RECO_VERSION_NO))
    print('--------')
    await startup_Initializer(client)
    
    



# Module: restrictor
# Description: To control both user and webhook commands permission
@client.event
async def on_message(message):
    ctx = await client.get_context(message)
    if not message.guild and not message.author.bot:
        await ctx.send("I respond to commands via **Discord Server only**.")
        await ctx.send("**GitHub**: <https://bit.ly/recoserver>")
        await ctx.send("**Mobile App**: <https://bit.ly/RecoApp>")
        await ctx.send("**YouTube**: <https://bit.ly/recoYoutube>")
        await ctx.send("**My Brother 😉**:\n**De & go**: <https://bit.ly/deandgo-invite>")     
    else:
        await restrictor_module.restrictor(message,client)

  
# Module: abort
# Description: Abort the Shutdown or Restart schedule
# Usage: !abort 
@client.command()
@Logger(client)
async def abort(ctx):
    await abort_module.abort(ctx,client)


# Module: alert
# Description: Alerts user interaction.
# Usage: !alert on or !alert off or !alert onwithbeep
@client.command()
@Logger(client)
async def alert(ctx, option=None):
   await alertInteraction_module.alert(ctx,option)


# Module: appQuitter
# Description: Quits the application
# Usage: !appquitter "Application Name" or !appquitter "Application Name" minutesToQuit
@client.command()
@Logger(client)
async def appquitter(ctx, appName=None,minutes=0):
    await appQuitter_module.appquitter(ctx,client,appName, minutes)

    
# Module: batteryLevel
# Description: To see the estimated battery charge remaining
# Usage: !batterylevel
@client.command() 
@Logger(client)
async def batterylevel(ctx,option=None):
    await batteryLevel_module.batterylevel(ctx,client,option)
    
 
# Module: batteryReportGenerator
# Description: Generates detailed report for your battery
# Usage: !batteryreport
@client.command() 
@Logger(client)
async def batteryreport(ctx,option=None):
    await batteryReportGenerator_module.batteryreport(ctx,option)    

 
# Module: camera
# Description: Records a video or takes a photo (no audio)
# Usage: !camera command time
@client.command()
@Logger(client)
async def camera(ctx,*commandtime):
    await camera_module.camera(ctx,*commandtime)


# Module: cmd
# Description: Executes cmd command
# Usage: !cmd "command"
@client.command()
@Logger(client)
async def cmd(ctx,*txt):
    text=" ".join(txt)
    await cmd_module.cmd(ctx, text)


# Module: clipBoard
# Description: Copy to PC's Clipboard
# Usage: !clip txt
@client.command()
@Logger(client)
async def clip(ctx):
    await clipboardGetCopy_module.clip(ctx)


@client.command()
@Logger(client)
async def commands(ctx):
    await reco_module.reco(ctx,("commands"),client=client,discordVersion=discord.__version__)


# Module: echo
# Description: Turns command output display to discord chat on and off (works for !cmd and !powershell)
# Usage: !echo off or !echo on
@client.command()
@Logger(client)
async def echo(ctx, status=None):
    await echo_module.echo(ctx, status)


# Module: file
# Description: Allows file download, upload and system navigation
# Usage: !file [command] [[path]|[times]]
@client.command()
@Logger(client)
async def file(ctx, command=None, *args):
    await file_module.file(ctx, command, *args)


# Module: hibernate
# Description: Hibernates the system
# Usage: !hibernate or !hibernate secondsToHibernation
@client.command()
@Logger(client)
async def hibernate(ctx, minutes=0):
    await hibernate_module.hibernate(ctx,client, minutes)


# Module: launch
# Description: Launches a shortcut in the shortcuts directory
# Usage: !launch [shortcut]
@client.command()
@Logger(client)
async def launch(ctx, *shortcut):
    fullLenShortcut=" ".join(shortcut)
    await launch_module.launch(ctx,client, fullLenShortcut)


# Module: lock
# Description: Locks system
# Usage: !lock or !lock minutesToLock
@client.command()
@Logger(client)
async def lock(ctx, minutes=0):
    await lock_module.lock(ctx,client, minutes)


# Module: log
# Description: Turns on of off logs in chat. Also can be used to retrieve Chimera execution logs
# Usage: !log [off|on] | [show] [date (format: YYYY-MM-DD)]
@client.command()
@Logger(client)
async def log(ctx, param=None, date=None):
    await log_module.log(ctx, param, date)


# Module: media
# Description: Controls Media Features
# Usage: !media command or !media command times
@client.command()
@Logger(client)
async def media(ctx, command=None, times=0,*time):
    await media_module.media(ctx, command, times,*time)

    
# Module: mouse
# Description: Controls Mouse Movements
# Usage: !mouse command or !mouse command times
@client.command()
@Logger(client)
async def mouse(ctx, command="", times=1, distance=1):
    await mouse_module.mouse(ctx, command, times, distance)

    
# Module: Music
# Description: Play video music from YouTube in VLC Player.
# Usage: !music query or !m query
@client.command()
@Logger(client)
async def music(ctx, *txt):
    text="+".join(txt)
    await music_module.music(ctx,client, text)  
@client.command()
@Logger(client)
async def m(ctx, *txt):
    text="+".join(txt)
    await music_module.music(ctx,client,text)      

    
# Module: notification
# Description: Sends a notification to the computer4
# Usage: !notification "Notification Content"
@client.command()
@Logger(client)
async def notification(ctx):
    text=str(ctx.message.content[14:])
    await notification_module.notification(ctx,client, text)


# Module: powershell
# Description: Executes powershell command
# Usage: !powershell "command"
@client.command()
@Logger(client)
async def powershell(ctx, *txt):
    text=" ".join(txt)
    await powershell_module.powershell(ctx, text)


# Module: print
# Description: To print
# Usage: !print
@client.command()
@Logger(client)
async def printer(ctx,mode=None,*inputs):
    await recoPrint_module.printer(ctx, mode,*inputs)


# Module: processes
# Description: Shows all running process which may be useful for !appquitter feature.
# Usage: !processes
@client.command()
@Logger(client)
async def processes(ctx):
    await processes_module.processes(ctx)


# Module: reco
# Description: Show all Reco information.
# Usage: !reco
@client.command()
@Logger(client)
async def reco(ctx,*option):
    await reco_module.reco(ctx,*option,client=client,discordVersion=discord.__version__)
  

# Module: restart
# Description: Restarts system
# Usage: !restart or !restart minutesToRestart
@client.command()
@Logger(client)
async def restart(ctx, minutes=0):
    await restart_module.restart(ctx,client, minutes)


# Module: rich presence
# Description: Starts the Rich Presence
# Usage: !rpc or !rpc start or !rpc stop
@client.command()
@Logger(client)
async def rpc(ctx,option=None):
    await rpc_module.rpc(ctx,client,option)


# Module: say
# Description: Uses powershell and a TTS engine to make your computer say something
# Usage: !say "Something to say"
@client.command()
@Logger(client)
async def say(ctx, *txt):
    text=" ".join(txt)
    await say_module.say(ctx, text)


# # Module: screenPower
# # Description: Control screen to turn on or off
# # Usage: !screen on or !screen off
# @client.command()
# @Logger(client)
# async def screen(ctx, option=None):
#     await screenPower_module.screen(ctx, option)


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
async def search(ctx):  
    await search_module.search(ctx)


# Module: shutdown
# Description: Shuts system down
# Usage: !shutdown or !shutdown minutesToShutdown
@client.command()
@Logger(client)
async def shutdown(ctx, minutes=0):
    await shutdown_module.shutdown(ctx,client, minutes)


# Module: signout
# Description: Sign out the user out of the system
# Usage: !signout or !signout minutes
@client.command()
@Logger(client)
async def signout(ctx, minutes=0):
    await signout_module.signout(ctx,client, minutes)


# Module: sleep
# Description: Puts system to sleep
# Usage: !sleep or !sleep minutesToSleep
@client.command()
@Logger(client)
async def sleep(ctx, minutes=0):
    await sleep_module.sleep(ctx,client, minutes)

    
# Module: speedtest
# Description: Checks internet download and upload speed.
# Usage: !speedtest
@client.command()
@Logger(client)
async def speedtest(ctx):
    await speedtest_module.speedtest(ctx)


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
async def url(ctx):
    await urlLauncher_module.url(ctx)


# Module: versionChecker
# Description: Here you can check the current verion of Reco PC Server and it's improvements.
# Usage: !version
@client.command()
@Logger(client)
async def version(ctx):
    await versionChecker_module.version(ctx,client)
    

# Module: wake
# Description: Help to keep screen alway on
# Usage: !wake on or !wake off
@client.command()
@Logger(client)
async def wake(ctx,option=None):
    await wake_module.wake(ctx,option)    

# Module: wlanSignal
# Description: To check the signal strength of a Wi-Fi Connection
# Usage: !wlansignal
@client.command()
@Logger(client)
async def wlansignal(ctx):
    await wlanSignal_module.wlansignal(ctx)

    
# Module: whatsapp
# Description: Opens the chat Screen for the entered MobileNumber
# Usage: !whatsapp CountryCode_Followed_by_MobileNumber
@client.command()
@Logger(client)
async def whatsapp(ctx, num=None,platform='pc'):
    await whatsapp_module.whatsapp(ctx, num,platform)


# Module: youtube
# Description: Searches on YouTube.
# Usage: !youtube or !youtube search
@client.command()
@Logger(client)
async def youtube(ctx):
    await youtube_module.youtube(ctx)
@client.command()
@Logger(client)
async def yt(ctx):
    await youtube_module.youtube(ctx)


# System Tray menu functions

# Starts the bot client
def startclient():
    while True:
        try:
            l=client.start(configs.BOT_TOKEN,reconnect=True)
            return l
        except:
            print("Trouble in Bot client start")
            continue
        

def iconRun():
    try:
        loop = asyncio.get_event_loop()
    except RuntimeError as ex:
        if "There is no current event loop in thread" in str(ex):
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            loop = asyncio.get_event_loop()
    
    loop.create_task(startclient())
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

# Opens webhook_restrictor.py file
def open_Webhook_restrictor(): os.startfile("webhook_restrictor.py")

# Opens webhook_restrictor.py file
def open_User_restrictor(): os.startfile("user_restrictor.py")

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
     recoPid=os.getpid()
     os.system(f"taskkill /F /PID {recoPid}")

    #  os.system("taskkill /F /IM pythonw.exe")


# About
def about(): webbrowser.open('https://github.com/Arvinth-Krishna/Reco-PC-Server')




# Instructions
def instructions(): webbrowser.open('https://github.com/Arvinth-Krishna/Reco-PC-Server#features-documentation')


# Create system tray icon and start running the client
def iconSetup():
    iconImage = Image.open("Reco_logo.png")
    iconMenu = Menu(
        MenuItem("Connect", action=connectInfo),
        MenuItem("Instructions", action=instructions),
        MenuItem("Show Logs", action=showLogs),
        MenuItem("Show Shortcuts", action=showShortcuts),
        MenuItem("Show Downloads", action=showdownloads, default=True),
        MenuItem("User Restrictor", action=open_User_restrictor),
        MenuItem("Webhook Restrictor", action=open_Webhook_restrictor),
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
