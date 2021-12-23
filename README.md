<div align="center">
<h1>Reco PC Server</h1>

<p align="center">

<a  href="https://github.com/Arvinth-Krishna/Reco-PC-Server#installation--" ><img  width="265" height="250" alt="Reco PC Server" title="Reco PC Server" src="https://user-images.githubusercontent.com/49812701/123842966-f9f15d80-d92e-11eb-9db0-087202e92f7b.png"></a>

</p>

 
</div>

# 
**Reco PC Server** is a cross platform PC Controller Discord Bot which is a modified and improved version of Chimera for Reco-Discord PC Remote Controller app & it's written in Python discord.py.

Using Reco you can easily control your computer remotely and have it do from simple tasks such as shutdown, sleep, and lock to opening a website or executing powershell commands.

Reco PC Server is a self hosted bot, which means that you have to run the bot on your computer - the machine you want to control via discord commands.


Installing Reco PC Server is an easy 3 minute process. [🎬 YouTube - Reco Playlist](https://www.youtube.com/playlist?list=PLwfmXAeVRyvkiFj_kyodNsd2uUa-0yrAG)




## Quick Jumps

* **[Reco-Mobile App](https://github.com/Arvinth-Krishna/Reco-PC-Server#reco---mobile-app--)**
* **[🔸Commands List](https://github.com/Arvinth-Krishna/Reco-PC-Server#features-list--)**
* **[Commands Documentation](https://github.com/Arvinth-Krishna/Reco-PC-Server#features-documentation--)**
* **[🔸Installation Process](https://github.com/Arvinth-Krishna/Reco-PC-Server#installation--)**
* **[Installation Error-Help](https://github.com/Arvinth-Krishna/Reco-PC-Server#to-deal-with-any-error-during-installation--)**
* Restricters
     * **[User Restricter](https://github.com/Arvinth-Krishna/Reco-PC-Server#user-restricter--)**
     * **[Webhook Restricter](https://github.com/Arvinth-Krishna/Reco-PC-Server#webhook-restricter--)**
* **[Setting up Task Scheduler for Reco-Startup](https://github.com/Arvinth-Krishna/Reco-PC-Server#setting-up-task-scheduler-for-reco-startup--)**
* **[For Contributing](https://github.com/Arvinth-Krishna/Reco-PC-Server#contributing--)**
* **[Donate](https://github.com/Arvinth-Krishna/Reco-PC-Server#donate--)**
* **[Credits](https://github.com/Arvinth-Krishna/Reco-PC-Server#credits--)**
* **[Contributors](https://github.com/Arvinth-Krishna/Reco-PC-Server#contributors--)**


## Reco - Mobile App  [↟](https://github.com/Arvinth-Krishna/Reco-PC-Server#quick-jumps) 
**[Reco: Discord PC Remote Controller](https://play.google.com/store/apps/details?id=com.gak.reco)**-Mobile App is now available on Play Store✌. 

[🎬 YouTube - How to install and use Reco - Mobile App](https://youtu.be/YJXfgRL4aK4)

[<img src="https://play.google.com/intl/en_us/badges/images/generic/en-play-badge-border.png" height="60" alt="Get Reco: Discord PC Remote Controller on Google Play" />](https://play.google.com/store/apps/details?id=com.gak.reco "Get Reco: Discord PC Remote Controller on Google Play")



* Reco-Mobile App contain 4 tabs 
  - Home Screen
  - Media Screen
  - Command Screen
  - Webhook Screen
  


### Screenshots:
<p align="center">
  <img  width="210" height="385" src="https://user-images.githubusercontent.com/49812701/107601722-8257b600-6c4d-11eb-87c2-9f9036382745.jpg">
  <img  width="210" height="385" src="https://user-images.githubusercontent.com/49812701/107601747-8e437800-6c4d-11eb-9c14-49080bd84cfa.jpg">
  <img  width="210" height="385" src="https://user-images.githubusercontent.com/49812701/107601773-9d2a2a80-6c4d-11eb-8ed0-958e136eff84.jpg">
  <img  width="210" height="385" src="https://user-images.githubusercontent.com/49812701/107601780-a3200b80-6c4d-11eb-9bcb-24b5e5adac96.jpg">
  <img  width="210" height="385" src="https://user-images.githubusercontent.com/49812701/107601788-a7e4bf80-6c4d-11eb-8f64-bd4c2fe6c7e3.jpg">
  <img  width="210" height="385" src="https://user-images.githubusercontent.com/49812701/107601794-ad420a00-6c4d-11eb-91f0-d9d35f7505c8.jpg">
  <img  width="210" height="385" src="https://user-images.githubusercontent.com/49812701/107601806-b29f5480-6c4d-11eb-95a9-043bc57e5d6d.jpg">
  <img  width="210" height="385" src="https://user-images.githubusercontent.com/49812701/107602896-0b242100-6c51-11eb-8fc8-4473af17c846.jpg">
</p>



## Requirements:
* Python 3
* discord.py
* mss
* opencv-python
* pynput
* requests
* python-dotenv
* pystray
* Pillow
* plyer
* pytube
* pycaw
* speedtest-cli


## Features List:  [↟](https://github.com/Arvinth-Krishna/Reco-PC-Server#quick-jumps) 
* **[Abort](https://github.com/Arvinth-Krishna/Reco-PC-Server#-abort--)**
* **[App Quitter](https://github.com/Arvinth-Krishna/Reco-PC-Server#-appquitter--)**
* **[Battery Level](https://github.com/Arvinth-Krishna/Reco-PC-Server#-battery-level--)**
* **[Battery Report Generator](https://github.com/Arvinth-Krishna/Reco-PC-Server#-battery-report-generator--)**
* **[Camera](https://github.com/Arvinth-Krishna/Reco-PC-Server#-camera--)**
* **[Cmd](https://github.com/Arvinth-Krishna/Reco-PC-Server#-cmd--)**
* **[Clip](https://github.com/Arvinth-Krishna/Reco-PC-Server#-clip--)**
* **[Echo](https://github.com/Arvinth-Krishna/Reco-PC-Server#-echo--)**
* **[File](https://github.com/Arvinth-Krishna/Reco-PC-Server#-file--)**
* **[Help](https://github.com/Arvinth-Krishna/Reco-PC-Server#-help--)**
* **[Hibernate](https://github.com/Arvinth-Krishna/Reco-PC-Server#-hibernate--)**
* **[Launch](https://github.com/Arvinth-Krishna/Reco-PC-Server#-launch--)**
* **[Lock](https://github.com/Arvinth-Krishna/Reco-PC-Server#-lock--)**
* **[Log](https://github.com/Arvinth-Krishna/Reco-PC-Server#-log--)**
* **[Logoff](https://github.com/Arvinth-Krishna/Reco-PC-Server#-logoff--)**
* **[Media](https://github.com/Arvinth-Krishna/Reco-PC-Server#-media--)**
* **[Music](https://github.com/Arvinth-Krishna/Reco-PC-Server#-music--)**
* **[Notification](https://github.com/Arvinth-Krishna/Reco-PC-Server#-notification--)**
* **[Powershell](https://github.com/Arvinth-Krishna/Reco-PC-Server#-powershell--)**
* **[Processes](https://github.com/Arvinth-Krishna/Reco-PC-Server#-processes--)**
* **[Restart](https://github.com/Arvinth-Krishna/Reco-PC-Server#-restart--)**
* **[Say](https://github.com/Arvinth-Krishna/Reco-PC-Server#-say--)**
* **[Screenshot](https://github.com/Arvinth-Krishna/Reco-PC-Server#-screenshot--)**
* **[Search (Google)](https://github.com/Arvinth-Krishna/Reco-PC-Server#-google-search--)**
* **[Shutdown](https://github.com/Arvinth-Krishna/Reco-PC-Server#-shutdown--)**
* **[Sleep (may act as hibernate)](https://github.com/Arvinth-Krishna/Reco-PC-Server#-sleep--)**
* **[Speedtest](https://github.com/Arvinth-Krishna/Reco-PC-Server#-speedtest--)**
* **[System Info](https://github.com/Arvinth-Krishna/Reco-PC-Server#-system-info--)**
* **[URL Launcher](https://github.com/Arvinth-Krishna/Reco-PC-Server#-url-launcher--)**
* **[Version Checker](https://github.com/Arvinth-Krishna/Reco-PC-Server#-version-checker--)**
* **[Wlan Signal](https://github.com/Arvinth-Krishna/Reco-PC-Server#-Wlan-Signal--)**
* **[WhatsApp (click to chat)](https://github.com/Arvinth-Krishna/Reco-PC-Server#-whatsapp--)**
* **[YouTube (search)](https://github.com/Arvinth-Krishna/Reco-PC-Server#-youtube-search--)**



## Features Documentation:  [↟](https://github.com/Arvinth-Krishna/Reco-PC-Server#quick-jumps) 

### ★ Abort  [⇪](https://github.com/Arvinth-Krishna/Reco-PC-Server#features-list--)

* !abort
	> Aborts the Shutdown or Restart schedule.

		e.g: !abort

### ★ AppQuitter  [⇪](https://github.com/Arvinth-Krishna/Reco-PC-Server#features-list--)

* !appquitter *PID/Application_Name* or !appquitter *PID/Application_Name* *minutes*
	> Quits the specified application immediately or with a time delay in minutes.

		e.g: !appquitter chrome 30

### ★ Battery Level  [⇪](https://github.com/Arvinth-Krishna/Reco-PC-Server#features-list--) 

* !batterylevel
	> To check the estimated battery charge remaining.

		e.g: !batterylevel

### ★ Battery Report Generator  [⇪](https://github.com/Arvinth-Krishna/Reco-PC-Server#features-list--) 

* !batteryreport
	> Generates a detailed battery report for your PC. [Screenshots](https://github.com/Arvinth-Krishna/Battery_Report/blob/master/README.md#screenshots)

		e.g: !batteryreport

### ★ Camera  [⇪](https://github.com/Arvinth-Krishna/Reco-PC-Server#features-list--) 

* !camera *command* or !camera *command* *time*
	> Controls computer camera for taking photo or filming for a given *time* in seconds (default is 5 seconds).

		e.g: !camera video 10
		list of commands:
		- video time
		- photo

### ★ Cmd  [⇪](https://github.com/Arvinth-Krishna/Reco-PC-Server#features-list--) 

* !cmd "*command*"
	> Executes *command* in cmd.exe.

		e.g: !cmd shutdown -a

### ★ Clip  [⇪](https://github.com/Arvinth-Krishna/Reco-PC-Server#features-list--) 

* !clip *text*
	> Copy the message to your PC's Clipboard.

		e.g: !clip Copy this text to PC's Clipboard

### ★ Echo  [⇪](https://github.com/Arvinth-Krishna/Reco-PC-Server#features-list--) 

* !echo *status*
	> Turns on or off !cmd and !powershell command echo in chat. When turned on, the command return will be sent to chat.

		e.g: !echo on (or) !echo off

### ★ File  [⇪](https://github.com/Arvinth-Krishna/Reco-PC-Server#features-list--) 

* !file *command* or !file *command* *path*
	> Browses, saves and retrieves files from or to your computer.

		e.g: !file relative ..
		list of commands:
		- absolute => sets an absolute path
		- relative => sets a relative path
		- list => lists current path
		- retrieve => uploads a file to the chat
		- save => saves a file to the HD from the chat
		- download => saves a file from a direct url to the HD

### ★ Help  [⇪](https://github.com/Arvinth-Krishna/Reco-PC-Server#features-list--) 

* !help or !help *command*
	> Shows Reco help, listing commands of shows help for a specific command.
	
		e.g: !help screenshot

### ★ Hibernate  [⇪](https://github.com/Arvinth-Krishna/Reco-PC-Server#features-list--) 

* !hibernate or !hibernate *minutes*
	> Hibernates your computer immediately or with a time delay in minutes. 

		e.g: !hibernate 30

### ★ Launch  [⇪](https://github.com/Arvinth-Krishna/Reco-PC-Server#features-list--) 

* !launch *shortcut*
    > Launches a custom shortcut you placed in the shortcuts folder.


    > [🎬 YouTube - How to use App Launcher](https://youtu.be/-b-7-8oK1tI)

		e.g: !launch Application_Name_in_Shortcut_Folder

### ★ Lock  [⇪](https://github.com/Arvinth-Krishna/Reco-PC-Server#features-list--) 

* !lock or !lock *minutes*
	> Locks your computer immediately or with a time delay in minutes.

		e.g: !lock 30

### ★ Log  [⇪](https://github.com/Arvinth-Krishna/Reco-PC-Server#features-list--) 

* !log *param* or !log *param* *date*
	> turns on or off chat logging or show log for given date (defaults to today).

		e.g: !log show 2021-02-08

### ★ LogOff  [⇪](https://github.com/Arvinth-Krishna/Reco-PC-Server#features-list--) 

* !logoff or !logoff *minutes*
	> Logs off your user immediately or with a time delay in minutes.

		e.g: !logoff 30

### ★ Media  [⇪](https://github.com/Arvinth-Krishna/Reco-PC-Server#features-list--) 

* !media *command* or !media *command* *repeat_n_times or delay_n_minutes*
	> Controls computer media playback and volume once or repeatedly.
	> 
	> For Play, Pause, and Stop commands have delay_n_minutes feature.
		
		e.g: !media prev 2
		list of commands:
		- vol-up
		- vol-down
		- vol-mute
		- say-vol
		- cv
		- next
		- prev
		- stop
		- play
		- pause
		- key-tab
		- key-space
		- key-enter
		- key-up
		- key-down
		- key-left
		- key-right
		- key-close
		- key-quit	


### ★ Music  [⇪](https://github.com/Arvinth-Krishna/Reco-PC-Server#features-list--) 

* !music "*query*" or !m "*query*"
    > "*query*" can be a song name or video link or playlist link
    > 
    > Plays video music from YouTube in VLC Player. 
    > 
    > ⚠ To use this command you need to add VLC to the Path (Environmental Variables)
    > 
    > Default path: C:\Program Files\VideoLAN\VLC
    
    
    

    > **Trouble in Playing Music in VLC?**
    > 
    > If VLC shows some error while trying to play a song.
    > 
    > ⚠ Try *Replacing* **[youtube.lua](https://drive.google.com/uc?export=download&id=1NnZmyOJ-khgxP6eCFUCCxFUko-_ZfjIV)** file from VLC.
    > 
    > Default path: C:\Program Files\VideoLAN\VLC\lua\playlist

		e.g: !music The Nights 
		          or
	         !m The Nights
		     
		     !m quit      - Quits the VLC Player.
		     !m play      - Play the paused song.
		     !m pause     - Pause the current playing song.
		     !m stop      - Stops the song.
		     !m next      - Play the next song if you have any queued song.
		     !m prev      - Play the previous song if you have any queued song.
		     
    > Advanced Music commands:
    > 
    > ⚠ You can even download any video from YouTube using Reco into .mp3 or .mp4 file.
    > 
    > ⚠⚠IMPORTANT: Sometimes Download feature won't work, maybe it's because of some changes made on YouTube's API and it will take time to get new some new update from Pytube package✌.
    
		e.g: !music dm The Nights
		          or
	         !m dm The Nights
		     
		     !m dm *query*      - Downloads music files.
		     !m dv *query*      - Downloads videos files.
		     !m df              - Shows Download folder.
		     

### ★ Notification  [⇪](https://github.com/Arvinth-Krishna/Reco-PC-Server#features-list--) 

* !notification "*message*"
    > Sends a notification to the computer.

		e.g: !notification who are you?

### ★ Powershell  [⇪](https://github.com/Arvinth-Krishna/Reco-PC-Server#features-list--) 

* !powershell "*command*"
	> Executes *command* in Powershell.

		e.g: !powershell shutdown -s -t 300

### ★ Processes  [⇪](https://github.com/Arvinth-Krishna/Reco-PC-Server#features-list--) 

* !processes
	> Shows the current Foreground Apps with PID.

		e.g: !processes


### ★ Restart  [⇪](https://github.com/Arvinth-Krishna/Reco-PC-Server#features-list--) 

* !restart or !restart *minutes*
	> Restarts your computer immediately or with a time delay in minutes.

		e.g: !restart 30

### ★ Say  [⇪](https://github.com/Arvinth-Krishna/Reco-PC-Server#features-list--) 

* !say "*text*"
	> Uses powershell commands and a TTS engine to make your computer say something.
     
		e.g: !say Reco

### ★ ScreenShot  [⇪](https://github.com/Arvinth-Krishna/Reco-PC-Server#features-list--) 

* !screenshot or !screenshot *seconds*
	> Takes a screenshot of your computer and sends it back to you.

		e.g: !screenshot 1

### ★ Google Search  [⇪](https://github.com/Arvinth-Krishna/Reco-PC-Server#features-list--) 

* !search or !search *query*
	> Helps you to search your query in Google very easily.

		e.g: !search Reco Discord PC Remote Controller

### ★ Shutdown  [⇪](https://github.com/Arvinth-Krishna/Reco-PC-Server#features-list--) 

* !shutdown or !shutdown *minutes*
	> Shuts down your computer immediately or with a time delay in minutes.

		e.g: !shutdown 30

### ★ Sleep  [⇪](https://github.com/Arvinth-Krishna/Reco-PC-Server#features-list--) 

* !sleep or !sleep *minutes*
	> ⚠ Warning: Sleep command may act as hibernate. (Please create a pull request if you know to fix this issue. [sleep_module.py](https://github.com/Arvinth-Krishna/Reco-PC-Server/blob/main/modules/sleep_module.py))
	> 
	> Sleeps your computer immediately or with a time delay in minutes. 

		e.g: !sleep 30

### ★ Speedtest  [⇪](https://github.com/Arvinth-Krishna/Reco-PC-Server#features-list--) 

* !speedtest 
	> Shows your internet speed. 

		e.g: !speedtest

### ★ System Info  [⇪](https://github.com/Arvinth-Krishna/Reco-PC-Server#features-list--) 

* !systeminfo
	> Shows your System Information. 

		e.g: !systeminfo

### ★ URL Launcher  [⇪](https://github.com/Arvinth-Krishna/Reco-PC-Server#features-list--)

* !url *website*
	> Opens the website in your browser.

		e.g: !url www.google.com

### ★ Version Checker  [⇪](https://github.com/Arvinth-Krishna/Reco-PC-Server#features-list--)

* !version
	> Shows the current version of Reco PC Server.

		e.g: !version

### ★ Wlan Signal  [⇪](https://github.com/Arvinth-Krishna/Reco-PC-Server#features-list--)

* !wlansignal
	> To check the signal strength of a Wi-Fi Connection.

		e.g: !wlansignal

### ★ Whatsapp  [⇪](https://github.com/Arvinth-Krishna/Reco-PC-Server#features-list--) 

* !whatsapp *countryCode_MobileNumber*
	> Opens chat screen for entered mobile number (Click to Chat feature).

		e.g: !whatsapp 911234567890

### ★ YouTube Search  [⇪](https://github.com/Arvinth-Krishna/Reco-PC-Server#features-list--) 

* !youtube or !youtube *search*
	> Shows search result on YouTube.

		e.g: !youtube Avicii - The Nights

Note: 
* All above commands works best on Windows and some commands may not work on other platforms.
* And some commands may require elevated privileges on Linux.


## Installation:  [↟](https://github.com/Arvinth-Krishna/Reco-PC-Server#quick-jumps) 

### Text Instructions:
1. **Download & Install Python** - Remember: Tick the Add to path checkBox during installation.
   -> https://www.python.org/   (Python Version - [3.9.8](https://www.python.org/downloads/release/python-398/) recommended)
2. Create a bot and get its **token** by following these instructions: https://youtu.be/-m-Z7Wav-fM
3. [Download](https://github.com/Arvinth-Krishna/Reco-PC-Server/archive/main.zip) the Reco PC Server Repository, **run setup.bat on Windows** or **setup.sh on Linux** and put your Bot Token in the newly created **.env file**. 
4. Get **Webhook URL** from your Channel and add it in your Webhook tab in your [Reco](https://play.google.com/store/apps/details?id=com.gak.reco) mobile App. https://www.youtube.com/watch?v=2Fcvg-Bh7Oo&t=1s
5. Launch **reco.pyw**, right click on the system tray icon and hit Connect to invite Reco Pc Server to your Discord server.
6. Enjoy!🥳

### Video tutorial:
Click below GIF to see the video.
[![Video Tutorial](https://j.gifs.com/J8qwWg.gif)](https://www.youtube.com/watch?v=HbqW0zCIZYg)


## To Deal with any Error during Installation:  [↟](https://github.com/Arvinth-Krishna/Reco-PC-Server#quick-jumps) 

### Error 1: Building wheel for multidict (PEP 517) ... error

     error: Microsoft Visual C++ 14.0 or greater is required. Get it with "Microsoft C++ Build Tools": https://visualstudio.microsoft.com/visual-cpp-build-tools/
     ----------------------------------------
     ERROR: Failed building wheel for multidict
     Failed to build yarl multidict
     ERROR: Could not build wheels for yarl, multidict which use PEP 517 and cannot be installed directly```

* Its an simple error and can easily solved by following below instrustion:
   - We will Just Install and then Uninstall - Visual Studio C++ Build Tools.
   - Now, just **install [Visual Studio Installer](https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=BuildTools&rel=16)** and **then install Build Tools**.
   - And now try again to **run setup.bat on Windows** or **setup.sh on Linux** from Downloaded Reco Folder.
   - After successfully installed Reco setup, Paste your Bot Token in the newly created **.env file** & continue following the [instuction from the 4th Step](https://github.com/Arvinth-Krishna/Reco-PC-Server#text-instructions)
   - And, now you can uninstall Visual Studio Installer from Controll Panel

### Error 2: WARNING: The script chardetect.exe is installed in ........ which is not on PATH.

* To solve this issue **just copy and paste the path which is given in the error in The Environmental variable.**
   - eg:   
   
         WARNING: The script chardetect.exe is installed in 'C:\Users\USER_NAME\AppData\Roaming\Python\Python39\Scripts' which is not on PATH.
	 
    - If you get above given error in the **console** while running **setup.bat** or **setup.sh**. Then follow below given instruction.
    - **Copy the Path from the error** given in the setup.bat console **or change the username in this path and try it:**
        C:\Users\ **USER_NAME**\AppData\Roaming\Python\Python39\Scripts
    - Now go to Start Menu and Type: **Edit environment variables for your account**
    - In that **click Path** and **then add the copied path in that field** and click OK.
    - And now try again to **run setup.bat on Windows** or **setup.sh on Linux** from Downloaded Reco Folder.
    - After successfully installed Reco setup, Paste your Bot Token in the newly created **.env file** & continue following the [instuction from the 4th Step](https://github.com/Arvinth-Krishna/Reco-PC-Server#text-instructions)



## User Restricter:  [↟](https://github.com/Arvinth-Krishna/Reco-PC-Server#quick-jumps) 

* Using this feature you can easily restrict commands permission by adding **User's Id** in **user_restricter.py** file.
* Follow the commented instruction in that file.

	> Synatx for webhook restricter:

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
		},




## Webhook Restricter:  [↟](https://github.com/Arvinth-Krishna/Reco-PC-Server#quick-jumps) 

[🎬 YouTube - How to use Webhook Restricter](https://youtu.be/JpJQW7IAKj0)

* Using **[Reco mobile app](https://play.google.com/store/apps/details?id=com.gak.reco)** you can easily control your PC using webhook. And if you want to share your webhooks with others and you want to restrict some commands.
* You can restrict so easily by adding that **webhook** in **webhook_restricter.py** file.
* Follow the commented instruction in that file.

	> Synatx for webhook restricter:

		{ 
		
                #1️⃣ Replace webhook Name
                'webhookName':'Demo webhook',       # Here you can enter the Webhook name, so you can identify easily in this file. 

                #2️⃣ Replace webhook URL & ID
                'webhookURL':'https://discord.com/api/webhooks/841227223729700866/aW4XpuFTUfweJIcQAqTSgikXZu6r5r6Q8MK_rOawf6qj_dyAUVQUCzbTm6Is0Bs8bQFG',
                'webhookId':'841227223729700866',   # You can obtain the "webhook id" by looking at the webhook URL, the number after https://discord.com/api/webhooks/ is the "id" , and the part after that is the token. 

                 #3️⃣ Before sharing your Webhook URL to others. you can set permission to each commands as you wish🥳
                 # "True"  => means Permission granted to use the command.
                 # "False" => means Permission Denied to use the command.

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
		},




## Setting up Task Scheduler for Reco-Startup:  [↟](https://github.com/Arvinth-Krishna/Reco-PC-Server#quick-jumps) 
These instruction will help you to setup Reco to startup automatically when we start your PC.
It looks like lenghty but its so easy to setup, just follow the steps. so chill, do and have fun...

[🎬 YouTube - How to set up Reco Startup using Task Scheduler](https://youtu.be/gAic5Gv9FcQ)

1. Open **Task Scheduler** by typing it inside the start menu.
2. click **Create Task**
3. Enter the Name as **Reco Startup**
4. And now **check(✔) the _Run with highest privileges_ checkBox**
5. And then, go to **Triggers tab** and click **New**
6. And set _Begin the task:_ **At log on** and also set _Delay task for:_ **8 seconds** and then click **OK**
7. And again click **New** and set _Begin the task:_ **On Workstation Unlock - Any user** and also set _Delay task for:_ **8 seconds** and then click **OK**
8. And now go to **Actions tab** and click **New**
9. Now set
    - **Action:** Start a Program
    - **Program/script:** C:\Users\USERNAME\AppData\Local\Programs\Python\Python39\pythonw.exe (change the USERNAME in this path to your username)
    - **Add arguments(optional):** reco.pyw
    - **Start in (optional):** C:\Users\USERNAME\Downloads\Reco-PC-Server-main (change the USERNAME in this path to your username or paste the downloaded RecoPCServer Repository path)
    - And click **OK**
10. And now go to **Conditions tab** and **uncheck all the checkBox** and **Check(✔) ONLY Network CheckBox** -> (Start only if following network connection avaliable: Any Connection)
11. And now **Click OK**
12.  Next time when you turn on your PC - Reco will Start Automatically🥳.

## Contributing:  [↟](https://github.com/Arvinth-Krishna/Reco-PC-Server#quick-jumps) 
Reco was written to be modular so one can easily modify the code and enhance it. I welcome and greatly appreciate anyone who wishes to contribute a module of their own.
Here's how to create a Reco module:

1. Create your *_module.py under the modules directory. See lock_module.py for a good example on how to structure yours.
2. Create an entry for your modules in reco.pyw. The file is full of examples.
3. Test Reco PC Server with your changes and make a pull request if everything works well.
4. Update the README.md file to include your new module and your github profile under Contributors


## Donate  [↟](https://github.com/Arvinth-Krishna/Reco-PC-Server#quick-jumps) 
If you found this project helpful and want to thank me, consider buying me a cup of ☕


<a href="https://www.paypal.com/paypalme/gak15"><img width="240" src="https://github.com/everdrone/coolbadge/blob/master/badges/Paypal/Coffee/Dark/Big.png?raw=true"></a>


<a href="https://www.buymeacoffee.com/ArvinthKrishna"><img width="240"  src="https://github.com/appcraftstudio/buymeacoffee/raw/master/Images/snapshot-bmc-button.png"></a>



## Credits:  [↟](https://github.com/Arvinth-Krishna/Reco-PC-Server#quick-jumps) 

* [CedArctic](https://github.com/CedArctic) and all contributors for creating [Chimera](https://github.com/CedArctic/Chimera) which is modified and improved. And now it act as a server(PC controller) for Reco-Discord PC Remote Controller app.


## Contributors:  [↟](https://github.com/Arvinth-Krishna/Reco-PC-Server#quick-jumps) 
* [CedArctic](https://github.com/CedArctic)
* [Zachman61](https://github.com/Zachman61)
* [vfcoelho](https://github.com/vfcoelho)
* [DragosPopse](https://github.com/DragosPopse)
* [TGlide](https://github.com/TGlide)
* [vlad4him](https://github.com/vlad4him)
* [sn0wmanmj](https://github.com/sn0wmanmj)
* [cominixo01](https://github.com/cominixo01)
* [medusalix](https://github.com/medusalix)
* [kostino](https://github.com/kostino)
* [Big Flubba](https://github.com/TheHunter1234)


## ❤️ Found this project useful?
If you found this project useful, then please consider giving it a **⭐ on Github and sharing it with your friends via social media**.


### [⟰ Jump to the top](https://github.com/Arvinth-Krishna/Reco-PC-Server#reco-pc-server)
