import configs, psutil,discord
from socket import gethostname
from lib.helpers import checkfolder
from lib.helpers import boolConverter
from lib.printHelper import print_Folders_Checker
from lib.reco_embeds import recoEmbeds as rm
from datetime import datetime as dt

from lib.updatePresence_helper import presenceChanger, reco_rpc, resetUptime


objectChannel=[]



def objectChannelGetter(client):
    objectChannel.clear()
    for channel in client.get_all_channels():
            if isinstance(channel,discord.TextChannel):
                if channel.topic!=None:
                    topic=channel.topic.lower()
                    if topic.__contains__('reco pc server') and topic.__contains__(client.user.discriminator):
                            objectChannel.append(channel)

async def startup_Initializer(client):

    online_Notifier_Bool=boolConverter(configs.RECO_ONLINE_NOTIFIER)
    checkfolder()
    print_Folders_Checker()
    deviceName=gethostname()
    battery = psutil.sensors_battery()
    user    = psutil.users()
    now = dt.now()
    batteryInfo=""
    if battery!=None:  
        print("Battery percentage : ", battery.percent)
        batteryInfo=f" | {'⚡' if battery.power_plugged else '🔋' } **{battery.percent}%**" 

    msg=f"\n\n👉 👑 **{user[0].name.capitalize()}** | {'💻' if battery!=None else '🖥'} **{deviceName.capitalize()}**{batteryInfo}"
    if online_Notifier_Bool:
        objectChannelGetter(client)
        if len(objectChannel)!=0:
            for ctx in objectChannel:
                await rm.recoOnline(ctx,f"\u200B\n**🟢 Online** ({now.strftime('%Y-%m-%d %H:%M:%S %Z%z')}){msg}",         
         
           authorName=client.user.name,authorIcon=client.user.avatar_url,authorURL="https://bit.ly/recoserver",color=0x2F3136)
    resetUptime()
    if boolConverter(configs.RPC_BOOL):
        print("Starting RPC & Bot Presence...")
        if configs.rpc_started:
            return
        else:
            configs.rpc_started=True
        await reco_rpc(client)
    else:
        print("Starting Bot Presence...")
        await presenceChanger(client)

def onlineNotifierChannelCount(client):
    objectChannelGetter(client)
    return len(objectChannel)
    



    
