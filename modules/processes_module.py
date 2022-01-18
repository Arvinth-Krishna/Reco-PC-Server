# Module: processes
# Description: Shows all running process which may be useful for !appquitter feature.
# Usage: !processes
# Dependencies: asyncio, configs,subprocess,discord


import asyncio, configs,subprocess,discord,time
import socket
from psutil import users

async def processes(ctx):
    await ctx.send(f"> Gathering information from **💻 {socket.gethostname().capitalize()}**...",delete_after=1.5)
    printlist=[]
            
    cmd = 'powershell "gps | where {$_.MainWindowTitle } | select Id,ProcessName'
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    print(proc)
    for line in proc.stdout:
        if not line.decode()[0].isspace():
            printlist.append(line.decode().rstrip())
    
    if configs.operating_sys == "Windows":
        p="```PID    ::: Application Name\n\n"
        pidlist=" "
        applicationNlist=" "
        for i in printlist:
            j=i.split(" ")
            pidlist=pidlist+j[0]+"\n "
            applicationNlist=applicationNlist+j[1]+"\n "
            p=p+j[0]+"  ::: "+j[1]+"\n"
        p=p+"\n```"
        embed=discord.Embed( color=int(configs.EMBEDS_COLOR,0))
        embed.set_author(name="!processes", url="https://bit.ly/RecoCommands", icon_url="https://user-images.githubusercontent.com/49812701/123842966-f9f15d80-d92e-11eb-9db0-087202e92f7b.png")
        embed.add_field(name="Foreground Apps:",value=p,inline=False)
        embed.add_field(name="Pro Tip:",value="```\nTry!\n!appquitter PID/Application_Name\nor\n!appquitter PID/Application_Name minutes```",inline=False)
        embed.add_field(name='FYI',value="```fix\nThe PID will change every time you restart your Application.\n```")
        await ctx.send(embed=embed)        
        print(printlist)
        
        

    else:
        await ctx.send("In Reco, Processes feature is currently not available for this platform.")
        await asyncio.sleep(3)



# listOfProcessNames = list()
# # Iterate over all running processes
#     for proc in psutil.process_iter():
#    # Get process detail as dictionary
#         pInfoDict = proc.as_dict(attrs=['pid', 'name', 'cpu_percent','username'])
#    # Append dict of process detail in list
#         if (pInfoDict['username']!=None ): 
#             listOfProcessNames.append(pInfoDict)
            
#             print(pInfoDict['name'] ,' ::: ', pInfoDict['pid'], ' ::: ', pInfoDict['cpu_percent'])
#     if configs.operating_sys == "Windows":
#         print("Processesss")
#         await ctx.send(listOfProcessNames)