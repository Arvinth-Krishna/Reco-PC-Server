from multiprocessing.connection import Client
from pydoc import cli
from turtle import up
import discord,datetime,configs,asyncio,socket,math,psutil,requests,time,logging
from lib import rpc
from lib.helpers import Logger, boolConverter
from lib.reco_embeds import recoEmbeds as rm
from lib.helpers import get_idle_duration
from lib import updatePresence_helper




errorCounter=0

def botStautsUpdate():
    if configs.is_alert_bool and boolConverter(configs.SHOW_DND_BOT_STATUS):
        return discord.Status.dnd
    if (get_idle_duration()>=(float(configs.SHOW_IDLE_STATUS_IN_MINS)*60)) and boolConverter(configs.DYNAMIC_BOT_STATUS):
        return discord.Status.idle
    else:
        return discord.Status.online


async def updatePresence(client):
    try:
        await client.change_presence(status=botStautsUpdate(), activity=discord.Game(name=f'{configs.BOT_PREFIX}commands | Uptime: {datetime.datetime.now().replace(microsecond=0)-configs.begin_time.replace(microsecond=0)}'))
        return True
    except:
        print("Update Presence - Error - Trying to reconnect client...")
        return False

def adderrorcounter():
    updatePresence_helper.errorCounter=updatePresence_helper.errorCounter+1

async def rpcClose(rpc_obj):
    await rpc_obj.close()

def resetUptime():
    configs.begin_time = datetime. datetime. now()
    configs.mk_time= time.mktime(time.localtime())

async def presenceChanger(client):
    while True:
        
        if not await updatePresence(client):
            continue
        if boolConverter(configs.RPC_BOOL):
           break
        await asyncio.sleep(10)

async def custom_rp(client,rpc_obj,bot_image_url,deviceName):
    activity=configs.CUSTOM_RP_ACTIVITY[0]
  
    activity["assets"].update({"small_text" :"Reco PC Server","small_image": "https://i.imgur.com/wwUJmrI.png"})
    try:
        rpc_obj.set_activity(activity)
        await asyncio.sleep(configs.CUSTOM_RP_ACTIVITY[1])
    except:
        print("Custom RPC - Error")
        adderrorcounter()
        

async def rp_reco(client,rpc_obj,bot_image_url,deviceName):
    activity = {
                    "state": f"running on {deviceName}", 
                    "details": "Reco PC Server",
                    "timestamps": {
                        "start": configs.mk_time
                    },
                    "assets": {
                        "small_text": "Reco PC Server", 
                        "small_image": "https://i.imgur.com/wwUJmrI.png",  
                        "large_text": client.user.name,
                        "large_image": bot_image_url 
                    },
                    "buttons": [{"label": 'GitHub', "url":"https://bit.ly/recoserver"},{"label": 'Commands', "url":"https://bit.ly/RecoCommands"}],
                    "instance": False
                }
    try:
        rpc_obj.set_activity(activity)
        await asyncio.sleep(configs.SHOW_RECO_RP[1])
    except:
        print("Reco PC Server RPC - Error")
        adderrorcounter()
        

async def rp_cpu_usage(client,rpc_obj,bot_image_url,deviceName):
    battery=psutil.sensors_battery()    
    platform_pic= "https://user-images.githubusercontent.com/49812701/152082249-5d0c7812-f09a-47ef-97c2-32c4f97437d3.png" if battery==None else "https://user-images.githubusercontent.com/49812701/152082182-0a6d900a-3c76-4bd4-87f1-1fbcba5a228b.png" 
    for i in range(0,configs.SHOW_CPU_USAGE_RP[1]):
               
                if not boolConverter(configs.RPC_BOOL):
                    break
                pcStatus=""
                if boolConverter(configs.SHOW_PC_STATUS_IN_CPU_USAGE):
                    pcStatus="🌙 | " if get_idle_duration()>=(float(configs.SHOW_IDLE_STATUS_IN_MINS)*60) else "🟢 | "
                cpu_per = round(psutil.cpu_percent(),1) # Get CPU Usage
                mem = psutil.virtual_memory()
                mem_per = round(psutil.virtual_memory().percent,1)
                activity = {
                        "state": "CPU: "+str(cpu_per)+"%", 
                        "details": f"RAM:  {round(mem.used/1000000000,1)}/{math.trunc(mem.total/1000000000)} GB ( {str(mem_per)}% )",
                        "assets": {
                            "small_text": "Reco PC Server", 
                            "small_image": "https://i.imgur.com/wwUJmrI.png",  
                            "large_text": f"{pcStatus}{deviceName} | {'⚡' if battery.power_plugged else '🔋'} {battery.percent}%" if battery!=None else f"{deviceName}",
                            "large_image": platform_pic 
                        },
                        "buttons": [{"label": 'GitHub', "url":"https://bit.ly/recoserver"},{"label": 'Commands', "url":"https://bit.ly/RecoCommands"}],
                        "instance": False
                    }
                try:
                   rpc_obj.set_activity(activity)
                except:
                    print("CPU Usage RPC - Error")
                    adderrorcounter()
                   
                await asyncio.sleep(1)



async def rp_Runner(client,rp_order,rpc_obj,bot_image_url,deviceName):
    while True:
            
            while True:
                try:
                    requests.get("http://www.google.com", timeout=5)
                    break
                except (requests.ConnectionError, requests.Timeout) as exception:
                    print("No Internet Connection - Resetting Uptime!")
                    resetUptime()
                    print(configs.begin_time," -- ",configs.mk_time)
                    await updatePresence(client)
                await asyncio.sleep(5)
            
            if not boolConverter(configs.RPC_BOOL) or errorCounter>25:
                print("Quitting rp from while loop")
                try:
                   rpc_obj.close()
                except:
                    pass
                await asyncio.sleep(7)
                configs.rpc_started=False
                if errorCounter>25:
                    updatePresence_helper.errorCounter=0
                    await reco_rpc(client)
                await presenceChanger(client)    
                return
                
            for i in rp_order:
                await updatePresence(client)
                await i[1](client,rpc_obj,bot_image_url,deviceName)
            
            

async def reco_rpc(client):
    configs.rpc_started=True
    configs.RPC_BOOL=True
    client_id = client.user.id
    while True:
        try:
           rpc_obj = rpc.DiscordIpcClient.for_platform(client_id)  # Send the client ID to the rpc module
           configs.desktop_discord_client=True
           break
        except:
            
            if not boolConverter(configs.RPC_BOOL):
                configs.RPC_BOOL=False
                configs.rpc_started=False
                return await presenceChanger(client)
            print("Please Make sure Discord Desktop client is running...")
            configs.desktop_discord_client=False
            await updatePresence(client)
            await asyncio.sleep(10)
       
    print("RPC connection successful.")
    bot_image_url=str(client.user.avatar_url).split("?")[0]+"?size=512"
    deviceName=socket.gethostname()
    if configs.ENABLE_CUSTOM_RICH_PRESENCE:
        rp_order=[[configs.SHOW_RECO_RP[2],rp_reco],[configs.SHOW_CPU_USAGE_RP[2],rp_cpu_usage],[configs.CUSTOM_RP_ACTIVITY[2],custom_rp]]
        if not configs.SHOW_CPU_USAGE_RP[0]:
            rp_order.pop(1)
        if not configs.SHOW_RECO_RP[0]:
            rp_order.pop(0)
        rp_order.sort()
        await rp_Runner(client,rp_order,rpc_obj,bot_image_url,deviceName)
    else:
        rp_order=[(1,rp_reco),(2,rp_cpu_usage)]
        await rp_Runner(client,rp_order,rpc_obj,bot_image_url,deviceName)

        





        



