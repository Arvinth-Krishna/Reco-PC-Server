# Module: reco
# Description: Show all Reco information.
# Usage: !reco 
# Dependencies: os


from distutils.command.config import config
import os
from platform import python_version
import win32print
import configs
from lib import helpers
import lib.reco_embeds as rm
import requests
from lib.helpers import boolConverter, recoCount as rc 
from lib.reco_command_counter import getCommandCount, getUpdateRemainderCount
from lib import printHelper
from modules import recoPrint_module,recoRestart_module
from lib.reco_startup import onlineNotifierChannelCount
from lib.updatePresence_helper import  reco_rpc



async def reco(ctx,*options,client,discordVersion):
    print(options)
    if options!=():
      option=options[0] if len(options)>=1 else None
      option2=options[1] if len(options)>=2 else None
    else:
        option=None
        option2=None

    print(option)
    print(option2)
    
    
    if option in (None,"commands","showall", "servers","printer"):
       await ctx.send(f"> Gathering information from **{client.user.name}**...",delete_after=3)
    response = requests.get("https://api.github.com/repos/Arvinth-Krishna/Reco-PC-Server/releases/latest")
    response2 = requests.get("https://api.github.com/repos/Arvinth-Krishna/Reco-PC-Server")
    current_version_response = requests.get(f"https://api.github.com/repos/Arvinth-Krishna/Reco-PC-Server/releases/tags/v{configs.RECO_VERSION_NO}")
    recoGitData=response.json()
    recoGitData2=response2.json()
    current_version_response_json=current_version_response.json()
    prefix=configs.BOT_PREFIX

    readme = open('readme.md', 'r', encoding="utf8")
    readme = readme.read()
    readme = readme.split('## ')
    readme=readme[5]
    features =readme.split('* ')
    features.pop(0)
    mtxt,mtxt1,mtxt2,mtxt3="","","",""
    for x in features:
        mtxt=mtxt+"‣ "+x
    
    mtxt="**🔮 Commands List ("+str(len(features))+"):**\n\n"+mtxt
    for x in features[:12]:
        mtxt1=mtxt1+"‣ "+x
    for x in features[12:24]:
        mtxt2=mtxt2+"‣ "+x
    for x in features[24:]:
        mtxt3=mtxt3+"‣ "+x    


    serverlist=client.guilds
    t=[]
    for x in serverlist:
        t.append(x.name)
    serverListTxt=""
    for sn in t[:8]:
        serverListTxt=serverListTxt+"\n‣ "+sn
    if len(t)>10:
        serverListTxt=serverListTxt+f'\nUse " {prefix}reco servers " command to see all Servers.'
    
    
    print(f"The Current Command Executed Count: {getCommandCount()}")

    if response2.status_code==200:
        gitdataInBanner=f"o_o {recoGitData2['subscribers_count']} ┆ Ψ {recoGitData2['forks']} ┆ ★ {recoGitData2['stargazers_count']} -  "
    else:
        gitdataInBanner=""
    banner=f"{'' if (option == None and not response.status_code!=200) else '┃'} **[{gitdataInBanner if (option==None and response2.status_code==200) else ''}GitHub](https://bit.ly/recoserver)** ┃ **[Discord](https://discord.gg/THwBTUHnwZ)** ┃ **[YouTube](https://bit.ly/recoYoutube)** ┃ **[Instagram](https://bit.ly/GAKventrueIG)** ┃"
    
    if response2.status_code==200:
        gitstats=f'''```Repo Name   : {recoGitData2["name"]}
Version No  : {recoGitData["tag_name"][1:]} 
Downloads   : {recoGitData["assets"][0]["download_count"]} ({recoGitData["tag_name"]})
Size        : {recoGitData["assets"][0]["size"]/1000} KB
Owner       : {recoGitData2["owner"]["login"]}
Stars       : {recoGitData2["stargazers_count"]}
Forks       : {recoGitData2["forks"]}
Watchers    : {recoGitData2["subscribers_count"]}
Open Issues : {recoGitData2["open_issues_count"]}
License     : {recoGitData2["license"]["name"]}```'''
    else:
        gitstats='''```fix\n⚠ Under API Rate Limt - Please Try Again Later!\n```'''""

    all_printers = [printer[2] for printer in win32print.EnumPrinters(2)]
    allPrinterTxt="\n".join([f"{n} {p}" for n, p in enumerate(all_printers)])+"\n"
    updateTxt=""
    wakeNotifier=""
    currentVersionDownloads=""
    currentPrintertxt=f'''```{win32print.GetDefaultPrinterW() if printHelper.current_Printer== None else all_printers[printHelper.current_Printer]}```'''
    
    if configs.WAKE_BOOL:
        wakeNotifier=f'''```fix\n⚠ {prefix}wake is Enabled.\n```'''
    print(f"wake bool:{configs.WAKE_BOOL}")

    



    


    if response.status_code==200 and (option==None or option=="showall") :
        currentVersionDownloads=f'({current_version_response_json["assets"][0]["download_count"]} downloads)'
        if (float(recoGitData["tag_name"][1:])>float(configs.RECO_VERSION_NO)and (getUpdateRemainderCount()!=1 or not boolConverter(configs.UPDATE_NOTIFIER)) ):
            updateTxt= f'''```diff\n+{recoGitData["name"]} Available✨\n{recoGitData["body"]}\n```**[Download]({recoGitData["assets"][0]["browser_download_url"]})** ({recoGitData["assets"][0]["download_count"]})\n'''
        elif(float(recoGitData["tag_name"][1:])==float(configs.RECO_VERSION_NO)):
            updateTxt=f'''```bash\n"You have the latest version of Reco PC Server. [{recoGitData["assets"][0]["download_count"]}]" \n```'''
        else:
            updateTxt="\u200B"
    elif response.status_code==403 and (option==None or option=="showall")and (getUpdateRemainderCount()!=1 or not boolConverter(configs.UPDATE_NOTIFIER)):
            updateTxt='''```fix\n⚠ Update Notifier Under API Rate Limt!\n```'''
    if (option==None or option=="showall"):
    # await ctx.send("")
        await rm.recoEmbeds.recoMmsg(ctx,txt= f'''{updateTxt}{wakeNotifier}
```Reco PC Server Version : {configs.RECO_VERSION_NO} {currentVersionDownloads}
Discord.py Version     : {discordVersion}
Python Version         : {python_version()}```''',
fieldname12="Current Printer:",
fieldvalue12=currentPrintertxt if currentPrintertxt!=None else None,
fieldname1="Statistics:",
fieldvalue1= f'''```Connected Servers       : {len(client.guilds)}
Online Notifiers        : {onlineNotifierChannelCount(client)}
Reco Available Commands : {str(len(features))}
Commands Executed Count : {getCommandCount()[:-1]}
Total Connected Members : {rc.get_reco_total_member_count(client)}
Connected Users         : {rc.get_reco_user_count(client)}
Connected Bots          : {rc.get_reco_bot_count(client)}
Blocked Users           : {rc.get_reco_block_user_count()}
Blocked Webhooks        : {rc.get_reco_block_webhook_count()}```''',
fieldname2="Configs:",
fieldvalue2= f'''```Reco Bot Prefix        : {configs.BOT_PREFIX}
Operating System       : {configs.operating_sys}

# Reco Online Notifier
Online Notifier        : {configs.RECO_ONLINE_NOTIFIER}

# Update Notifier
Update Notifier        : {configs.UPDATE_NOTIFIER}
Notifier Interval      : {configs.UPDATE_NOTIFIER_INTERVAL}

# Alert Command
Alert Enabled          : {configs.is_alert_bool}
Show DND Status        : {configs.SHOW_DND_BOT_STATUS}
Beep Minimum Volume    : {configs.BEEP_MINUMUM_VOLUME}%

# Rich Presence
RPC Enabled            : {configs.RPC_BOOL}
Custom RPC Enabled     : {configs.ENABLE_CUSTOM_RICH_PRESENCE}
Show PC Status         : {configs.SHOW_PC_STATUS_IN_CPU_USAGE}

# Bot Status
Dynamic Status         : {configs.DYNAMIC_BOT_STATUS}
Idle Time              : {configs.SHOW_IDLE_STATUS_IN_MINS} mins

# Restricters
Allow All Users        : {configs.ALLOW_ALL_USERS}
Allow All Webhooks     : {configs.ALLOW_ALL_WEBHOOKS}

# Others
Discord Logs Enabled   : {configs.discord_logs_enabled}
Disk Logs Enabled      : {configs.DISK_LOGS_ENABLED}
Initial Display Output : {configs.initial_display_output}
Python Alias           : {configs.PYTHON_ALIAS}```''',
fieldname3=None if option=="showall" else "Connected Servers:",
fieldvalue3=f"```{serverListTxt}```",

fieldname4="Other Reco Commands:",
fieldvalue4=f'''```{prefix}reco showall
{prefix}reco servers
{prefix}reco commands
{prefix}reco github
{prefix}reco printer
{prefix}reco restart
{prefix}reco quit
```''',
fieldname5="\u200B",

fieldvalue5=f"{banner} **[Donate](https://www.buymeacoffee.com/ArvinthKrishna)** {'┃' if(option == 'showall' or(option==None and response2.status_code!=200)) else ''}",
    
fieldname6=None if option=="showall" else "**🔮 Commands List ("+str(len(features))+"):**",
fieldvalue6=f'''{mtxt1}''',
fieldname7=None if option=="showall" else '\u200B',
fieldvalue7=f'''{mtxt2}''',
fieldname8=None if option=="showall" else '\u200B',
fieldvalue8=f'''{mtxt3}''',
fieldname9='GitHub Stats:' if (option=="showall" and response2.status_code==200) else None,
fieldvalue9=f'''{gitstats}''',
authorName=client.user.name,authorIcon=client.user.avatar_url,authorURL="https://bit.ly/recoserver",
fieldname10="Printer Configs:" if option=="showall" else None,
fieldvalue10=f'''```Printer No   (p) : {configs.CURRENT_PRINTER_NUMBER}
No of Copies (n) : {configs.NO_OF_COPIES}
Color Mode   (c) : {"Black" if printHelper.colorConverter(configs.COLOR_MODE)==1 else "Color"}
Orientation  (o) : {"Portrait" if printHelper.orinetationConverter(configs.ORIENTATION)==1 else "Landscape"}```''',
fieldname11="Available Printers:",
fieldvalue11=f'''```{allPrinterTxt}```''',
)

    
    
    # invitelink=f"https://discord.gg/{ic[0]}"
    
    # if len(ic)==0:
    # guild = client.get_guild("796238588760817685")
    # channel = guild.text_channels[0]
    # print(channel)
    # invitelink = await channel.create_invite(xkcd=True,max_age=0,max_uses=0)
    # server = client.get_Server(796238588760817685)
    # link = client.create_invite(destination=server,xkcd=True,max_age=0,max_uses=0)
    # await client.say(link)
    # print(client.guild)
    # for guild in client.fetch_guilds(limit=150):
    #     print(guild.id)

    # for guild in client.guilds:
    #     for channel in guild.channels:
    #         yield channel
    #         print(channel)
    # print(invitelink)
    #    newInvite=await ctx.channel.create_invite(xkcd=True, max_age = 0, max_uses = 0)
    #    print(newInvite)
    # for server in client.servers:
    #     print(server.name)
    
    


           



    

  

    if option=="servers" or option=="showall":
            text_channel_list = []
            objectChannel=[]
            channels=""
            chaIvite=[]
            
            for guild in client.guilds:
                for channel in guild.text_channels:
                    objectChannel.append(channel)
                    channels=channel
                    break
                
                text_channel_list.append({"name":guild.name,"serverid:": guild.id,"channelId":channels.id})
            for x in text_channel_list:
                print(x)
            invitelinkURL=""
            for i in range(len(objectChannel)):

                inviteCodeList=await objectChannel[i].invites()
                if len(inviteCodeList)==0:
                    invitelinkURL = await objectChannel[i].create_invite(xkcd=True,max_age=0,max_uses=0)
                else:
                    invitelinkURL=inviteCodeList[0]
                chaIvite.append({"serverName":text_channel_list[i]["name"],"inviteURL":invitelinkURL})
            
            cserverListTxt=""
            for sn in chaIvite:
                cserverListTxt=cserverListTxt+"\n‣ "+f"**{sn['serverName']}**\_[invite]({sn['inviteURL']})"
    
            await rm.recoEmbeds.fieldEmbed(ctx,txt=f"**{client.user.name}** Connected Servers (**{len(chaIvite)}**):\n{cserverListTxt}",
            fieldname1=None if option=="showall" else '\u200B',
            fieldvalue1=banner

            )

    if option=="commands" or option=="showall":
       await rm.recoEmbeds.fieldEmbed(ctx,mtxt,fieldname1=None if option=="showall" else '\u200B',fieldvalue1=banner            )

    if option=="github":
        await rm.recoEmbeds.fieldEmbed(ctx,txt=f'''**GitHub Stats:**\n\n{gitstats}''',fieldname1=None if response2.status_code!=200 else '\u200B',fieldvalue1=banner)
    
    if option== "printer":
        await recoPrint_module.printer(ctx,mode="reco")
    if option=="quit":
        if option2==None:
            helpers.reco_restart_bool=True
            await rm.recoEmbeds.msg(ctx,f"⚠ **Reco PC Server may start again, if you have assigned [Task Scheduler](https://bit.ly/reco-taskscheduler)**.\n\nTo confirm quit:\n**{prefix}reco quit yes**",color=rm.colorforWaitingMsg)
        elif option2.lower()=="yes":
            if helpers.reco_restart_bool:
                await rm.recoEmbeds.msg(ctx,"Quitting **Reco PC Server!**")    
                os.system(f"taskkill /F /PID {os.getpid()}")
            else:
                await rm.recoEmbeds.msg(ctx,"Opps!, you can't use this command before calling:\n\n**!reco quit**",color=rm.colorforError)
            


    if option == "restart" :
        if option2==None:
            helpers.reco_restart_bool=True
            await rm.recoEmbeds.msg(ctx,f'''⚠ **This command is not Recommended!**

⭕ **This command will close all running Python Programs**,
⭕ and, then restart **Reco PC Server** manually,
⭕ which may leads to two instances if you have assigned **[Task Scheduler](https://bit.ly/reco-taskscheduler)**.

Use this command to confirm the restart:
**{prefix}reco restart yes**''',color=rm.colorforWaitingMsg)

        elif option2.lower()=="yes":
            if helpers.reco_restart_bool:
                await rm.recoEmbeds.msg(ctx,"Restarting **Reco PC Server!**")
                recoRestart_module.forceRestart()
            else:
                await rm.recoEmbeds.msg(ctx,"Opps!, you can't use this command before calling:\n\n**!reco restart**",color=rm.colorforError)
            

        



    


