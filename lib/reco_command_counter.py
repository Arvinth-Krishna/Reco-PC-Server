import json
import os,requests
from  lib import reco_embeds as rm
from lib.helpers import boolConverter
import configs



async def addcount(ctx=None):
    updateInterval=int(configs.UPDATE_NOTIFIER_INTERVAL)
    #Check the File.
    if not os.path.isfile("rcc.txt"):
        with open("rcc.txt","w") as f:
            f.write("{}\n{}".format("0","0"))
            f.close()    
    if not os.path.isfile("gitreco.txt"):
        with open("gitreco.txt","w") as f:
            f.write("{}".format("0"))
            f.close()    

    # Reads the rcc.txt file            
    # os.system( "attrib -h rcc.txt" )
    with open("rcc.txt") as f: 
        rd=f.readlines()
        f.close()
    addCount=int(rd[0])+1
    updateRemainderCounter=int(rd[1])+1
    print(f"Current Update Notifier Count: {updateRemainderCounter}")
    
    if updateRemainderCounter<=1 and boolConverter(configs.UPDATE_NOTIFIER):
        response = requests.get("https://api.github.com/repos/Arvinth-Krishna/Reco-PC-Server/releases/latest")
        recoGitData=response.json()
        if response.status_code == 200:
            with open("gitreco.txt","w",encoding="utf8") as f:
                f.write("{}".format(recoGitData["tag_name"][1:]))
                f.close()
        print(f"Reco Git Status Code: {response.status_code}")
        if response.status_code!=200:
            with open("gitreco.txt") as f: 
               gitrecofile=f.readlines()
               gitrecofileV=float(gitrecofile[0])
               f.close()       
            print("Error : Code 403")
    

    with open("rcc.txt","w") as f:
        f.write("{}\n{}".format(addCount,"0" if updateRemainderCounter>updateInterval else updateRemainderCounter))
        f.close()
        # os.system( "attrib +h rcc.txt" )



    if updateRemainderCounter<=1 and boolConverter(configs.UPDATE_NOTIFIER):
        if response.status_code==200:
            if ((float(recoGitData["tag_name"][1:])>float(configs.RECO_VERSION_NO ))):
                updateTxt= f'''```diff\n+{recoGitData["name"]} Available✨\n{recoGitData["body"]}\n```**[Download]({recoGitData["assets"][0]["browser_download_url"]})** ({recoGitData["assets"][0]["download_count"]})\n'''
                await rm.recoEmbeds.msg(ctx,updateTxt)
    
        elif gitrecofileV> float(configs.RECO_VERSION_NO) and response.status_code==403:
            updateTxt='''```fix\n⚠ Update Notifier Under API Rate Limt!\n```'''
            await ctx.send(updateTxt)
        

    
    
def getCommandCount():
    # os.system( "attrib -h rcc.txt" )
    with open("rcc.txt") as f: 
        rd=f.readlines()
        f.close()
        # os.system( "attrib +h rcc.txt" )
    return rd[0]

def getUpdateRemainderCount():
    # os.system( "attrib -h rcc.txt" )
    with open("rcc.txt") as f: 
        rd=f.readlines()
        f.close()
        # os.system( "attrib +h rcc.txt" )
    return int(rd[1])

