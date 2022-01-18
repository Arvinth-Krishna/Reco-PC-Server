# Everytime you make changes in this file, you have to restart the Reco client (reco.pyw).


# ⚠ All Ids and URL entries should be in quotes('') and followed by comma (,)


# True -> Allows all webhooks. 
# False -> only allow - allowed webhooks (in allowed_webhooks_Id_list) or in command restricter list (webhook_commands_restricter_list).
# ⬇⬇⬇



allowed_webhooks_Id_list=['900715738501238431',  ]
blocked_webhooks_Id_list=['901715738501238431',  ]



webhook_commands_restricter_list=[

#(copy starts from here)    
{ 
   #1️⃣ Replace webhook Name
    'webhookName':'Reco Demo Webhook',       # Here you can enter the Webhook name, so you can identify easily in this file. 

   #2️⃣ Replace webhook URL & ID
    'webhookURL':'https://discord.com/api/webhooks/9997157385061238436/ErwFK48uztUeOaXJFeb9LosUwpeVilewoLNH8cRzBchKbY1dQqlAaM3rVY8XT3IqLrCf',
    'webhookId':'999715738501238436',   # You can obtain the "webhook id" by looking at the webhook URL, the number after https://discord.com/api/webhooks/ is the "id" , and the part after that is the token. 

 #3️⃣ Before sharing your Webhook URL to others. you can set permission to each commands as you wish🥳
 # "True"  => means Permission granted to use the command.
 # "False" => means Permission Denied to use the command.

 # For safety and security purposes we have set False as default for all commands and you can override by mentioning command permission down here.

   # ⚠ Powerfull Commands: (All powerfull commands will be "False" by default)
    '!abort':False,
    '!appquitter':False,
    '!cmd':False,
    '!file': False,
    '!hibernate':False,
    '!lock':False,
    '!logoff':False,
    'media_Close&QuitKeys':False,          # !media key-close, !media key-quit 
    '!powershell':False,
    '!restart':False,
    '!shutdown':False,
    '!sleep':False,

   # Moderate Commands:
    '!camera':True,
    '!clip':True,
    '!launch':True,
    '!screenshot':True,              

   # Media Commands: (!media)
    'media_Function_Keys':True,           # next, prev, stop, play, pause
    'media_Volume_Keys':True,             # vol-up, vol-down, vol-mute
    'media_ArrowKeys':True,               # key-up, key-down, key-left, key-right
    'media_Tab,Space&EnterKeys':True,     # key-tab, key-space, key-enter
    'music_Controls_Keys':True,           # key-f, key-shuffle, key-loop
    'other_media_commands':True,          # say-vol, cv

    # Other Commands:
    '!batterylevel':True,
    '!batteryreport':True,
    '!echo':True,
    '!log':True,
    '!music':True,
    '!m':True,
    '!notification':True,
    '!help':True,
    '!processes':True,
    '!search':True,
    '!say':True,
    '!speedtest':True,
    '!systeminfo':True,
    '!url':True, 
    '!version':True, 
    '!whatsapp':True,
    '!wlansignal':True,
    '!youtube':True,
}, #(copy ends here)

# If you have multiple webhooks to set permission. Copy { Everthing including Curly braces }.
# Don't forget to use comma after Curly braces( {}, ) and after entering ID with quotes(' ').
# And paste down here.





]
