# Module: versionChecker
# Description: Here you can check the current verion of Reco PC Server and it's improvements.
# Usage: !version
# Dependencies: time, os

import os, asyncio, configs,requests
from lib.reco_embeds import recoEmbeds as rm
from lib.reco_command_counter import getUpdateRemainderCount
from lib.helpers import boolConverter



async def version(ctx,client):
     current_running_reco_version=configs.RECO_VERSION_NO
     latest_Version_response = requests.get("https://api.github.com/repos/Arvinth-Krishna/Reco-PC-Server/releases/latest")
     current_version_response2 = requests.get(f"https://api.github.com/repos/Arvinth-Krishna/Reco-PC-Server/releases/tags/v{current_running_reco_version}")
     latest_Version_response_Json,current_version_response2_Json=latest_Version_response.json(),current_version_response2.json()
     updateTxt=""
     if latest_Version_response.status_code==200 :
        if (float(latest_Version_response_Json["tag_name"][1:])>float(current_running_reco_version)and (getUpdateRemainderCount()!=1 or not boolConverter(configs.UPDATE_NOTIFIER)) ):
            updateTxt= f'''```diff\n+{latest_Version_response_Json["name"]} Available✨\n{latest_Version_response_Json["body"]}\n```**[Download]({latest_Version_response_Json["assets"][0]["browser_download_url"]})** ({latest_Version_response_Json["assets"][0]["download_count"]})\n'''
        elif(float(latest_Version_response_Json["tag_name"][1:])==float(configs.RECO_VERSION_NO)):
            updateTxt=f'''```bash\n"You have the latest version of Reco PC Server. [{latest_Version_response_Json["assets"][0]["download_count"]}]" \n```'''
        else:
            updateTxt="\u200B"
     if current_version_response2.status_code==200:
          print(latest_Version_response_Json)
          print("======================")
          print(current_version_response2_Json)
          await rm.recoVersionEmbed(ctx,authorName=f"{configs.BOT_PREFIX}version",authorIcon=client.user.avatar_url,authorURL="https://bit.ly/recoserver",
          txt=updateTxt,
          fieldname1="Current Version:",
          fieldvalue1=f'''```Name              : {current_version_response2_Json['name']}
Tag               : {current_version_response2_Json['tag_name']}
Size              : {current_version_response2_Json["assets"][0]["size"]/1000} KB
Download Count    : {current_version_response2_Json["assets"][0]["download_count"]}
Uploader          : {current_version_response2_Json["assets"][0]["uploader"]["login"]}```''',
          fieldname2=f"Download {current_version_response2_Json['tag_name']} :",
          fieldvalue2=f'[link]({current_version_response2_Json["assets"][0]["browser_download_url"]})',
          fieldname3="Improvements:",
          fieldvalue3=current_version_response2_Json['body'],) 
     else:
           await rm.msg(ctx,'''```fix\n⚠ Under API Rate Limt - Please Try Again Later!\n```''')
     await asyncio.sleep(3)
