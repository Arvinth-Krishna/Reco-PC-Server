# Everytime you make changes in this file, you have to restart the Reco client (reco.pyw).


# ⚠ All Id entries should be in quotes(' ') and followed by comma (,)

# True -> Allows all users. 
# False -> only allow - allowed users (in allowed_users_Id_list) or in command restricter list (user_commands_restricter_list).
# ⬇⬇⬇
allow_all_users=True  


allowed_users_Id_list=['111595095059988111', ]
blocked_users_Id_list=['111595095059988111', ]


user_commands_restricter_list=[

#(copy starts from here)    
{ 
   #1️⃣ Replace User Name
    'userName':'Demo(GAK)',         # Here you can enter the User name, so you can identify easily in this file. 

   #2️⃣ Replace User ID
   'userId':'113595095059988521',   # Watch this video if you don't know how to get User ID - https://youtu.be/OS2rp7wHVTI

 #3️⃣ Before sharing your Reco with others. you can set permission to each commands as you wish🥳
 # "True"  => means Permission granted to use the command.
 # "False" => means Permission Denied to use the command.

 # For safety and security purposes we have set False as default for all commands and you can override by mentioning commands permission down here.

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
    'music_Controls_Keys':True,           # key-f, ey-shuffle, key-loop
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
    '!search':True,
    '!say':True,
    '!systeminfo':True,
    '!url':True, 
    '!version':False, 
    '!whatsapp':True,
    '!wlansignal':True,
    '!youtube':True,
   
}, #(copy ends here)

# If you have multiple users to set permission. Copy { Everthing including Curly braces }.
# Don't forget to use comma after Curly braces( {}, ) and after entering ID with quotes(' ').
# And paste down here. 







]
