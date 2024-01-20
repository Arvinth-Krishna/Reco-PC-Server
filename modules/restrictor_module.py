# Module: restricter
# Description: To control both user and webhook commands permission
# Usage: 
# Dependencies: 

import configs
# Import Restrictors
from user_restrictor import *
from webhook_restrictor import *
from lib.reco_command_counter import addcount
from lib.helpers import boolConverter
from modules import restrictor_module as rp
from lib.reco_embeds import recoEmbeds as rm


allow_all_users=boolConverter(configs.ALLOW_ALL_USERS)
allow_all_webhooks=boolConverter(configs.ALLOW_ALL_WEBHOOKS)


media_Volume_Keys=['vol-up','vol-down','vol-mute',]
media_ArrowKeys=['key-up','key-down','key-left','key-right']
media_CloseandQuitKeys=['key-close','key-quit']
media_Tab_SpaceandEnterKeys=['key-tab','key-space','key-enter']
media_Function_Keys=['next','prev','stop','play','pause']
media_Music_Control_Keys=['key-loop','key-shuffle','key-f','key-vlc-mute','key-mini']
other_media_commands=['cv','say-vol']



rpc_alert_count=0

async def restrictor(message,client):
    messageContentList=[]
    ctx = await client.get_context(message)
    varMsgcontent=message.content
    messageContentList=varMsgcontent.split(" ")
    msgWebhookId = str(message.webhook_id)
    msgUserId = str(message.author.id)


    
    check_bot=None
    webhook_found=False
    bool_blocked_user=False
    bool_allowed_user=False
    bool_Users_restrictor_list=False
    bool_blocked_webhook=False
    bool_allowed_webhook=False
    bool_webhooks_restrictor_list=False
    webhook_index=None
    user_index=None
    restrictor_data=None

    

    if(messageContentList[0][1:] in client.all_commands):
        print(f"\nCommand Received!--> {varMsgcontent}\n")
    else:
        return
    
    if boolConverter(configs.RPC_BOOL )and not configs.desktop_discord_client:
        
        rp.rpc_alert_count=rp.rpc_alert_count+1
        if rpc_alert_count in (2,6,11) or (messageContentList[0][1:]=="rpc" and not configs.desktop_discord_client):
            await rm.msg(ctx,"FYI,\n**Your RPC is not running!**\n\nTo run please Open/Install **Discord Desktop Client(App)**.\n\n **[Discord.com](https://discord.com)**",color=rm.color('colorforWaitingMsg'))

        


    if( (message.author.bot and message.webhook_id!=None) and f"{configs.BOT_PREFIX}" in messageContentList[0] and messageContentList[0][1:] in client.all_commands ):
        check_bot=True
    elif ((message.author.bot and message.webhook_id==None)  and f"{configs.BOT_PREFIX}" in messageContentList[0] and client.user.id!=message.author.id):
        await ctx.send("❌ **Denied** - Only Users & Webhook bots can control 😇.")          
    elif message.author.bot==False and f"{configs.BOT_PREFIX}" in messageContentList[0] and messageContentList[0][1:] in client.all_commands:
        check_bot=False

    if check_bot==False:
        for i in blocked_users_Id_list:
            if i==msgUserId:
                bool_blocked_user=True
                break
        if bool_blocked_user==False:
            for i in allowed_users_Id_list:
                if i==msgUserId:
                    bool_allowed_user=True
                    break
        if bool_blocked_user==False:
            count=0
            for i in user_commands_restrictor_list:             
                if i['userId']==msgUserId:
                    bool_Users_restrictor_list=True
                    user_index=count
                    break
                count+=1
            if user_index==None and boolConverter(configs.LIMIT_ALL_USER_COMMAND)==True:
                count=0
                for i in user_commands_restrictor_list:             
                    if i['userId']=='everyone':
                        bool_Users_restrictor_list=True
                        user_index=count
                        break
                    count+=1
                
    elif check_bot==True:
        for i in blocked_webhooks_Id_list:
            if i==msgWebhookId:
                
                bool_blocked_webhook=True
                break
        if bool_blocked_webhook==False:
            for i in allowed_webhooks_Id_list:
                if i==msgWebhookId:
                    bool_allowed_webhook=True
                    break
        if bool_blocked_webhook==False:
            count=0
            for i in webhook_commands_restrictor_list:                
                if i['webhookId']==msgWebhookId:
                    bool_webhooks_restrictor_list=True
                    webhook_index=count
                    break
                count=+1

  
    if (check_bot==True):
        print(f"Allow all webhooks: {allow_all_webhooks}\n")
        print('Webhook\'s profile:')
        print(f'Name   : {message.author.name}')
        print(f'Block  : {bool_blocked_webhook}')
        print(f'Allow  : {bool_allowed_webhook}')
        print(f'WCRList: {bool_webhooks_restrictor_list}\n')
        if (bool_blocked_webhook==False):
            if(allow_all_webhooks==False):
                if(bool_allowed_webhook==False):
                    if(bool_webhooks_restrictor_list==False):
                        await ctx.reply("❌- Oops! you don't have permission.")
                    else:
                        restrictor_data=webhook_commands_restrictor_list[webhook_index]
                else:
                    if(bool_webhooks_restrictor_list==False ):
                        await addcount(ctx)
                        await client.invoke(ctx)
                    else:
                        restrictor_data=webhook_commands_restrictor_list[webhook_index]
                
            else:
                if(bool_webhooks_restrictor_list==False):
                    await addcount(ctx)
                    await client.invoke(ctx)

                else:
                    restrictor_data=webhook_commands_restrictor_list[webhook_index]
        else:
            await ctx.reply("❌- Command Denied (Blocked Webhook)")   
    elif check_bot==False:
        print(f"Allow all users: {allow_all_users}\n")
        print('Sender\'s profile:')
        print(f'Name   : {message.author.name}')
        print(f'ID   : {message.author.id}')
        print(f'Block  : {bool_blocked_user}')
        print(f'Allow  : {bool_allowed_user}')
        print(f'UCRList: {bool_Users_restrictor_list}\n')
        if (bool_blocked_user==False):
            if(allow_all_users==False):
                if ((message.author.guild_permissions.administrator and boolConverter(configs.ALLOW_ADMINS)) or configs.RECO_OWNER_USER_ID==str(message.author.id)):
                    if(bool_Users_restrictor_list==False):
                        await addcount(ctx)
                        await client.invoke(ctx)
                    else:
                        restrictor_data=user_commands_restrictor_list[user_index]
                
                else:
                    if(bool_allowed_user==False):
                        if(bool_Users_restrictor_list==False):
                            await ctx.reply("❌- Oops! you don't have permission.")
                        else:
                            restrictor_data=user_commands_restrictor_list[user_index]
                    else:
                        if(bool_Users_restrictor_list==False):
                            await addcount(ctx)
                            await client.invoke(ctx)
                        else:
                            restrictor_data=user_commands_restrictor_list[user_index]
            else:
                if(bool_Users_restricter_list==False or (boolConverter(configs.ALLOW_ADMINS) or configs.RECO_OWNER_USER_ID==str(message.author.id))):
                    await addcount(ctx)
                    await client.invoke(ctx)
                else:
                    restrictor_data=user_commands_restrictor_list[user_index]
        else:
            await ctx.reply("❌- Command Denied (Blocked User)")   
    
    if restrictor_data!=None:
        i=restrictor_data
        original_command=messageContentList[0]; 
        messageContentList.insert(0,"!"+messageContentList[0][1:])
        messageContentList.pop(1)
        if(messageContentList[0]=='!media'):
            if(messageContentList[1]in media_Volume_Keys and i['media_Volume_Keys']):
                await addcount(ctx)
                await client.invoke(ctx)
                
            elif(messageContentList[1]in media_ArrowKeys and i['media_ArrowKeys']):
                await addcount(ctx)
                await client.invoke(ctx)
                
            elif(messageContentList[1]in media_CloseandQuitKeys and i['media_Close&QuitKeys']):
                await addcount(ctx)
                await client.invoke(ctx)
                                    
            elif(messageContentList[1]in media_Tab_SpaceandEnterKeys and i['media_Tab,Space&EnterKeys']):
                await addcount(ctx)
                await client.invoke(ctx)
                
            elif(messageContentList[1]in media_Function_Keys and i['media_Function_Keys']):
                await addcount(ctx)
                await client.invoke(ctx) 
                   
            elif(messageContentList[1]in media_Music_Control_Keys and i['music_Controls_Keys']):
                await addcount(ctx)
                await client.invoke(ctx)
                     
            elif(messageContentList[1]in other_media_commands and i['other_media_commands']):
                await addcount(ctx)
                await client.invoke(ctx) 

            else:
                if (check_bot==True):
                    await ctx.send("This webhook: ( "+i['webhookName'] +" ) tried to use permission denied command: ( "+original_command+" "+messageContentList[1]+" )")     
                else:
                    await ctx.send(f"This user: ( **{message.author.name}** ) tried to use permission denied command: ( **"+original_command+" "+messageContentList[1]+"** )")     

        elif not messageContentList[0] in i:
                if (check_bot==True):
                    await ctx.send("This command: ( **"+original_command+"** ) is not added in your \"**webhook_restrictor.py**\" file, so it\'s taken as \"**False**\" (Permission denied).\n\n Please add the commad to use: **'"+messageContentList[0]+"':True,** ")     
                else:           
                    await ctx.send("This command: ( **"+original_command+"** ) is not added in your \"**user_restrictor.py**\" file, so it\'s taken as \"**False**\" (Permission denied).\n\n Please add the commad to use: **'"+messageContentList[0]+"':True,** ")     
                                     
        elif(i[messageContentList[0]]):
            await addcount(ctx)
            await client.invoke(ctx)
            

        else:
            if (check_bot==True):
                await ctx.send("This webhook: ( "+i['webhookName']+" ) tried to use permission denied command: ( "+original_command+" )")          
            else:           
                await ctx.send(f"This user: ( **{message.author.name}** ) tried to use permission denied command: ( **"+original_command+"** )")          
                          


    
