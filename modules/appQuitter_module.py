# Module: Processes
# Description: 
# Usage: !appquitter "PID/Application Name" or !appquitter "PID/Application Name" minutesToQuit
# Dependencies: os, asyncio, subprocess

import os, asyncio, configs,subprocess
from turtle import color
from lib.reco_embeds import recoEmbeds as rm
from modules import notification_module


async def appquitter(ctx,client,appName, minutes=0):
    p=configs.BOT_PREFIX
    minutesInt=minutes
    printlist=[]
    application={}
    minutesTxt=""
    app=""
    color=rm.color('colorforCommonMsg')
    if minutesInt!=0:
        color=rm.color('colorforWaitingMsg')
        minutesTxt=f" in {minutesInt} minutes"
    minutes=minutes*60

    if appName==None:
            await rm.msg(ctx,f'**Help - {p}appquitter**\n\n**Commands:**\n```{p}appquitter  PID/Application_Name\n{p}appquitter  PID/Application_Name  minutes```\n**eg:**\n{p}appquitter chrome\n{p}appquitter chrome 6\n{p}appquitter 2250\n\n**FYI**,\nTo get **PID** try:\n**{p}processes**\n\n')

    elif appName.isnumeric():
        
        cmd = 'powershell "gps | where {$_.MainWindowTitle } | select Id,ProcessName'
        proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        for line in proc.stdout:
            if not line.decode()[0].isspace():
                printlist.append(line.decode().rstrip())
        for i in printlist:
            j=i.split(" ")
            application[j[0]]=j[1]

        app=application.get(appName)

        
        
        
        if app!=None:
            if minutesInt!=0:
                 text= app.capitalize()+" will close in "+str(minutesInt)+" minutes"
            await rm.msg(ctx,"Quitting the **{0}**({1}) app{2}.".format(app.capitalize(),appName,minutesTxt),color=color)
        else:
            if minutesInt!=0:
                 text= f"Terminating the process with PID {appName} in"+str(minutesInt)+" minutes"
            await rm.msg(ctx,"Terminating the process with PID **{0}**{1}.".format(appName,minutesTxt),color=color)
            

    elif appName!=None:
        if minutesInt!=0:
                 text= str(appName).capitalize()+" will close in "+str(minutesInt)+" minutes" 
        await rm.msg(ctx,"Quitting the **{0}** app{1}.".format(appName.capitalize(),minutesTxt),color=color)

    

    if minutes != 0:
        await notification_module.notification(ctx,client,text,noti=False) 
        await asyncio.sleep(minutes)

    if configs.operating_sys == "Windows":
        if appName==None:
            pass
        elif appName.isnumeric():
            if minutesInt!=0:
                await rm.msg(ctx,f"Terminating **{app.capitalize() if app!=None else appName}** process. (**Time is up! - {minutesInt} mins**)")
            os.system("taskkill /pid {0} /F".format(appName))
        elif appName!=None:
            if minutesInt!=0:
                await rm.msg(ctx,f"Terminating **{appName.capitalize()}** process. (**Time is up! - {minutesInt} mins**)")
            os.system("taskkill /F /IM {0}.exe".format(appName))

    elif configs.operating_sys == "Linux":
        os.popen("pkill -f {0}".format(appName))
    else:
        await ctx.send("Can't quit the app.")
        await asyncio.sleep(3)
