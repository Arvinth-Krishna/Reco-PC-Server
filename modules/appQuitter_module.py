# Module: appQuitter
# Description: Quits the application
# Usage: !appquitter "PID/Application Name" or !appquitter "PID/Application Name" minutesToQuit
# Dependencies: os

import os, asyncio, configs,subprocess


async def appquitter(ctx,appName, minutes=0):
    printlist=[]
    application={}

    if appName.isnumeric():
        
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
            await ctx.send("Quitting the **{0}**({1}) app.".format(app.capitalize(),appName))
        else:
            await ctx.send("Terminating the process with PID **{0}**.".format(appName))

    else:
        await ctx.send("Quitting the **{0}** app.".format(appName.capitalize()))
    

    minutes=minutes*60

    if minutes != 0:
        await asyncio.sleep(minutes)

    if configs.operating_sys == "Windows":
        if appName.isnumeric():
            os.system("taskkill /pid {0} /F".format(appName))
        else:
            os.system("taskkill /F /IM {0}.exe".format(appName))
    elif configs.operating_sys == "Linux":
        os.popen("pkill -f {0}".format(appName))
    else:
        await ctx.send("Can't quit the app.")
        await asyncio.sleep(3)
