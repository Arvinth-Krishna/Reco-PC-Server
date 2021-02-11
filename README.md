# Reco-PC-Server
<p align="center">
  <img  width="160" height="160" src="https://user-images.githubusercontent.com/49812701/107212940-b18fdc80-6a2d-11eb-929c-d3d9d1ca5e53.png">
</p>

# 
**Reco PC Server** is a cross platform PC Controller Discord Bot which is modified version of Chimera for Reco-Discord PC Remote Controller app & it's written in Python discord.py.


Using Reco you can easily control your computer remotely and have it do from simple tasks such as shutdown, sleep, lock and to open a website from your computer or executing powershell commands.

Reco PC Server is a self hosted bot, which means that you have to run the bot on your computer - the machine you want to control via discord commands.

Installing Reco is an easy 3 minute process - you can check the instructions bellow to see how to do it.

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

## Features List:
* appquitter
* camera
* cmd
* clip
* echo
* file
* helpme
* hibernate
* launch
* lock
* log
* logoff
* media
* notification
* powershell
* restart
* say
* screenshot
* shutdown
* sleep
* url



## Features Documentation:

* !appquitter *Application_Name* or !appquitter *Application_Name* *minutes*
	> quits the specified application immediately or with a time delay in minutes, 

              e.g: !appquitter chrome 30

* !camera *command* or !camera *command* *time*
	> controls computer camera for taking photo or filming for a given *time* in seconds (default is 5 seconds), 

              e.g: !camera video 10
	       list of commands:
	       - video time
	       - photo

* !cmd "*command*"
	> executes *command* in cmd.exe

* !clip *text*
	> copy the message to your PC's Clipboard

             e.g: !clip Copy this text to PC's Clipboard

* !echo *status*
	> turns on or off !cmd and !powershell command echo in chat. When turned on, the command return will be sent to chat, 

              e.g: !echo on (or) !echo off

* !file *command* or !file *command* *path*
	> browses, saves and retrieves files from or to your computer, 

                e.g: !file relative ..
		list of commands:
		- absolute => sets an absolute path
		- relative => sets a relative path
		- list => lists current path
		- retrieve => uploads a file to the chat
		- save => saves a file to the HD from the chat
		- download => saves a file from a direct url to the HD

* !helpme or !helpme *command*
	> shows Chimera help, listing commands of shows help for a specific command, 

                e.g: !helpme screenshot

* !hibernate or !hibernate *seconds*
	> hibernates your computer immediately or with a time delay in minutes, 

                e.g: !hibernate 30

* !launch *shortcut*
    > launches a custom shortcut you placed in the shortcuts folder.

                e.g: !launch Application_Name_in_Shortcut_Folder

* !lock or !lock *seconds*
	> locks your computer immediately or with a time delay in minutes, 

                e.g: !lock 30

* !log *param* or !log *param* *date*
	> turns on or off chat logging or show log for given date (defaults to today), 

                e.g: !log show 2021-02-08

* !logoff or !logoff *seconds*
	> logs off your user immediately or with a time delay in minutes, 

                e.g: !logoff 30

* !media *command* or !media *command* *repeat_n_times*
	> controls computer media playback and volume once or repeatedly, e.g: !media prev 2
	
		list of commands:
		- vol-up
		- vol-down
		- vol-mute
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


* !notification "*message*"
    > sends a notification to the computer

                e.g: !notification who are you?

* !powershell "*command*"
	> executes *command* in Powershell

* !restart or !restart *seconds*
	> restarts your computer immediately or with a time delay in minutes, 

                e.g: !restart 30

* !say "*text*"
	> uses powershell commands and a TTS engine to make your computer say something
     
                e.g: !say Reco

* !screenshot or !screenshot *seconds*
	> takes a screenshot of your computer and sends it back to you 

                e.g: !screenshot 1

* !shutdown or !shutdown *seconds*
	> shuts down your computer immediately or with a time delay in minutes, 

                e.g: !shutdown 30

* !sleep or !sleep *seconds*
	> sleeps your computer immediately or with a time delay in minutes, 

                e.g: !sleep 30

* !url *website*
	> Opens the website in your browser

                e.g: !url www.google.com

Note: Some commands may require elevated privileges on Linux.


## Installation:

### Text Instructions:
1. Download & Install Python -> https://www.python.org/downloads/
2. Create a bot and get its token and then get your channel ID by following these instructions: https://github.com/Chikachi/DiscordIntegration/wiki/How-to-get-a-token-and-channel-ID-for-Discord
3. [Download](https://github.com/Arvinth-Krishna/Reco-PC-Server/archive/main.zip) the Reco PC Server Repository, run setup.bat on Windows or setup.sh on Linux and put your Bot Token in the newly created .env file. 
4. Get Webhook URL from your Channel and add it in your Weebhook tab in your Reco mobile App.
5. Launch reco.pyw, right click on the system tray icon and hit Connect to invite Reco Pc Server to your Discord server.
6. Enjoy!

### Video tutorial:

[![Video Tutorial](https://j.gifs.com/l5m85j.gif)](https://www.youtube.com/watch?v=JXqS3WaTOB4)

The above video is an instruction for installing Chimera and this process is same for Reco too.



## Contributing:
Reco was written to be modular so one can easily modify the code and enhance it. I welcome and greatly appreciate anyone who wishes to contribute a module of their own.
Here's how to create a Reco module:

1. Create your *_module.py under the modules directory. See lock_module.py for a good example on how to structure yours
2. Create an entry for your modules in reco.pyw. The file is full of examples.
3. Test Reco PC Server with your changes and make a pull request if everything works well.
4. Update the README.md file to include your new module and your github profile under Contributors


## Credits:

* [CedArctic](https://github.com/CedArctic) for creating [Chimera](https://github.com/CedArctic/Chimera) which is modified and now act as a server(PC controller) for Reco-Discord PC Remote Controller app.


## Contributors:
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

