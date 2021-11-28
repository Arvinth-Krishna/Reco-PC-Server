# Module: speedtest
# Description: Checks internet download and upload speed.
# Usage: !speedtest
# Dependencies: speedtest


import asyncio, configs,subprocess,json
from logging import root


async def speedtest(ctx):
    printlist=[]
    speedtestMSG=await ctx.send("🌐 Finding optimal server...")
    await asyncio.sleep(1.2)
    await speedtestMSG.edit(content="⚡ Checking your Network speed...")
    await asyncio.sleep(1.2)
    await speedtestMSG.edit(content="Testing **⏬ Download** and **⏫ Upload** speed...")
    await asyncio.sleep(0.8)
    await speedtestMSG.edit(content="Testing **⏬ Download** and **⏫ Upload** speed ⏳\n\n**.....**                                                 🎯")

    cmd = "powershell speedtest.exe --share --json"
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,)
    await speedtestMSG.edit(content="Testing **⏬ Download** and **⏫ Upload** speed ⏳\n\n**........**                                              🎯")
    await asyncio.sleep(0.5)
    await speedtestMSG.edit(content="Testing **⏬ Download** and **⏫ Upload** speed ⏳\n\n**.............**                                         🎯")
    psout=proc.stdout
    count=0
    await speedtestMSG.edit(content="Testing **⏬ Download** and **⏫ Upload** speed ⏳\n\n**....................**                                  🎯")

    for line in psout:
        count=count+1
        await speedtestMSG.edit(content=f"Testing **⏬ Download** and **⏫ Upload** speed ⏳\n\n**..............................**                        🎯")
        if count>3:
            await speedtestMSG.edit(content=f"Testing **⏬ Download** and **⏫ Upload** speed ⏳\n\n**.................................................** ❌", delete_after=1.5)
            break

        if not line.decode()[0].isspace():
            printlist.append(line.decode().rstrip())

            await speedtestMSG.edit(content=f"Testing **⏬ Download** and **⏫ Upload** speed ⏳\n\n**.....................................**                 🎯")
            await asyncio.sleep(0.5)
            await speedtestMSG.edit(content=f"Testing **⏬ Download** and **⏫ Upload** speed ⏳\n\n**.................................................** ✅")
            if count==0 or count>3:
                await speedtestMSG.edit(content=f"Testing **⏬ Download** and **⏫ Upload** speed ⏳\n\n**.................................................** ❌", delete_after=1.5)
                break


    if count!=0 and count<3:
       await asyncio.sleep(1.5)
       await speedtestMSG.edit(content="😎 Results are almost ready!", delete_after=1.5)
    

    print("count: ",count)
    await asyncio.sleep(1)
    

  
    if configs.operating_sys == "Windows":   
        if count>3 or count==0:
            await ctx.send("❌ Error Occurred:\n🔸 Try Running Reco - **setup.bat** file again.\n🔸 Make sure you have added **Python Scripts path** in your environmental variables.\n\nAdd below given two paths in your Environmental variables's **Paths** section:") 
            await ctx.send("C:/Users/**gak**/AppData/Roaming/Python/Python39/Scripts\nC:/Users/**gak**/AppData/Local/Programs/Python/Python39/Scripts\nReplace **gak** with your username. \n\n**How to add in Environmental variables?**\n**StartMenu**-> search '**Environmental variables**'-> click '**Enviro__n__mental variables...**'-> click '**Paths**'-> click '**New**'and add both paths one by one-> click '**Ok**'")    
        else:
            d=printlist[0]
            res = json.loads(d)
            print(res)
            await ctx.send(res['share'])
    elif configs.operating_sys == "Linux":  
        d=printlist[0]
        res = json.loads(d)  
        await ctx.send(res['share'])
    else:
        await ctx.send("In Reco, Speedtest feature is currently not available for this platform.")
        await asyncio.sleep(3)
