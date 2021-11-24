# Module: restricter
# Description: To control both user and webhook commands permission
# Usage: 
# Dependencies: 

import configs
# Import Restricters
from user_restricter import *
from webhook_restricter import *


media_Volume_Keys=['vol-up','vol-down','vol-mute']
media_ArrowKeys=['key-up','key-down','key-left','key-right']
media_CloseandQuitKeys=['key-close','key-quit']
media_Tab_SpaceandEnterKeys=['key-tab','key-space','key-enter']
media_Function_Keys=['next','prev','stop','play','pause']
media_Music_Control_Keys=['key-loop','key-shuffle','key-f','key-vlc-mute','key-mini']





async def restricter(message,client):
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
    bool_Users_restricter_list=False
    bool_blocked_webhook=False
    bool_allowed_webhook=False
    bool_webhooks_restricter_list=False
    webhook_index=None
    user_index=None
    restricter_data=None

    

    if(messageContentList[0][1:] in client.all_commands):
        print(f"\nCommand Received!--> {varMsgcontent}\n")


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
            for i in user_commands_restricter_list:             
                if i['userId']==msgUserId:
                    bool_Users_restricter_list=True
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
            for i in webhook_commands_restricter_list:                
                if i['webhookId']==msgWebhookId:
                    bool_webhooks_restricter_list=True
                    webhook_index=count
                    break
                count=+1

  
    if (check_bot==True):
        print(f"Allow all webhooks: {allow_all_webhooks}\n")
        print('Webhook\'s profile:')
        print(f'Name   : {message.author.name}')
        print(f'Block  : {bool_blocked_webhook}')
        print(f'Allow  : {bool_allowed_webhook}')
        print(f'WCRList: {bool_webhooks_restricter_list}\n')
        if (bool_blocked_webhook==False):
            if(allow_all_webhooks==False):
                if(bool_allowed_webhook==False):
                    if(bool_webhooks_restricter_list==False):
                        await ctx.reply("❌- Oops! you don't have permission.")
                    else:
                        restricter_data=webhook_commands_restricter_list[webhook_index]
                else:
                    if(bool_webhooks_restricter_list==False ):
                        await client.invoke(ctx)
                    else:
                        restricter_data=webhook_commands_restricter_list[webhook_index]
                
            else:
                if(bool_webhooks_restricter_list==False):
                    await client.invoke(ctx)
                else:
                    restricter_data=webhook_commands_restricter_list[webhook_index]
        else:
            await ctx.reply("❌- Command Denied (Blocked Webhook)")   
    elif check_bot==False:
        print(f"Allow all users: {allow_all_users}\n")
        print('Sender\'s profile:')
        print(f'Name   : {message.author.name}')
        print(f'Block  : {bool_blocked_user}')
        print(f'Allow  : {bool_allowed_user}')
        print(f'UCRList: {bool_Users_restricter_list}\n')
        if (bool_blocked_user==False):
            if(allow_all_users==False):
                if (message.author.guild_permissions.administrator):
                    if(bool_Users_restricter_list==False):
                        await client.invoke(ctx)
                    else:
                        restricter_data=user_commands_restricter_list[user_index]
                
                else:
                    if(bool_allowed_user==False):
                        if(bool_Users_restricter_list==False):
                            await ctx.reply("❌- Oops! you don't have permission.")
                        else:
                            restricter_data=user_commands_restricter_list[user_index]
                    else:
                        if(bool_Users_restricter_list==False):
                            await client.invoke(ctx)
                        else:
                            restricter_data=user_commands_restricter_list[user_index]
            else:
                if(bool_Users_restricter_list==False):
                    await client.invoke(ctx)
                else:
                    restricter_data=user_commands_restricter_list[user_index]
        else:
            await ctx.reply("❌- Command Denied (Blocked User)")   
    
    if restricter_data!=None:
        i=restricter_data
        original_command=messageContentList[0]; 
        messageContentList.insert(0,"!"+messageContentList[0][1:])
        messageContentList.pop(1)
        if(messageContentList[0]=='!media'):
            if(messageContentList[1]in media_Volume_Keys and i['media_Volume_Keys']):
                await client.invoke(ctx)
            elif(messageContentList[1]in media_ArrowKeys and i['media_ArrowKeys']):
                await client.invoke(ctx)
            elif(messageContentList[1]in media_CloseandQuitKeys and i['media_Close&QuitKeys']):
                await client.invoke(ctx)                    
            elif(messageContentList[1]in media_Tab_SpaceandEnterKeys and i['media_Tab,Space&EnterKeys']):
                await client.invoke(ctx)
            elif(messageContentList[1]in media_Function_Keys and i['media_Function_Keys']):
                await client.invoke(ctx)    
            elif(messageContentList[1]in media_Music_Control_Keys and i['music_Controls_Keys']):
                await client.invoke(ctx)      
            else:
                if (check_bot==True):
                    await ctx.send("This webhook: ( "+i['webhookName'] +" ) tried to use permission denied command: ( "+original_command+" "+messageContentList[1]+" )")     
                else:
                    await ctx.send("This user: ( "+i['userName'] +" ) tried to use permission denied command: ( "+original_command+" "+messageContentList[1]+" )")     

        elif not messageContentList[0] in i:
                if (check_bot==True):
                    await ctx.send("This command: ( **"+original_command+"** ) is not added in your \"**webhook_restricter.py**\" file, so it\'s taken as \"**False**\" (Permission denied).\n\n Please add the commad to use: **'"+messageContentList[0]+"':True,** ")     
                else:           
                    await ctx.send("This command: ( **"+original_command+"** ) is not added in your \"**user_restricter.py**\" file, so it\'s taken as \"**False**\" (Permission denied).\n\n Please add the commad to use: **'"+messageContentList[0]+"':True,** ")     
                                     
        elif(i[messageContentList[0]]):
            await client.invoke(ctx)

        else:
            if (check_bot==True):
                await ctx.send("This webhook: ( "+i['webhookName']+" ) tried to use permission denied command: ( "+original_command+" )")          
            else:           
                await ctx.send("This user: ( "+i['userName']+" ) tried to use permission denied command: ( "+original_command+" )")          
                          


    

