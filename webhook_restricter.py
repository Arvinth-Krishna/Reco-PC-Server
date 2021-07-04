# Everytime you make changes in this file, you have to run Reco again (reco.pyw).

webhook_restricter_list=[

#(copy starts from here)    
{ 
   #1️⃣ Replace webhook Name
    'webhookName':'Temp webhook',       # Here you can enter the Webhook name, so you can identify easily in this file. 

   #2️⃣ Replace webhook URL & ID
    'webhookURL':'https://discord.com/api/webhooks/841227223729700866/aW4XpuFTUfweJIcQAqTSgikXZu6r5r6Q8MK_rOawf6qj_dyAUVQUCzbTm6Is0Bs8bQFG',
    'webhookId':'841227223729700866',   # You can obtain the "webhook id" by looking at the webhook URL, the number after https://discord.com/api/webhooks/ is the "id" , and the part after that is the token. 

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
    'music_Controls_Keys':True,                # key-f, ey-shuffle, key-loop

    # Other Commands:
    '!batterylevel':True,
    '!batteryreport':True,
    '!echo':True,
    '!log':True,
    '!music':True,
    '!m':True,
    '!notification':True,
    '!say':True,
    '!search':True,
    '!systeminfo':True,
    '!url':True, 
    '!version':True, 
    '!whatsapp':True,
    '!wlansignal':True,
    '!youtube':True,
   
}, #(copy ends here)

# If you have multiple webhooks to set permission. Copy { Everthing including Curly braces }.
# And paste down here.







]
