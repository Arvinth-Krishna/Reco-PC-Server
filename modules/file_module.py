# Module: file
# Description: Allows file download, upload and system navigation
# Usage: !file [command] [[path]|[times]]
# Dependencies: filesystem_control, requests

import os,asyncio
from pathlib import Path
import configs, requests, discord
from lib.helpers import savefoldercheck
from lib.reco_embeds import recoEmbeds as rm
from lib.filesystem_control import FileSystemControl

fileListPaths=[]

async def path_getter(ctx,path):
    path1=""
    if len(path)!=0:
            if path[0].isnumeric():
                if  len(fileListPaths)!=0:
                    if int(path[0])<len(fileListPaths):
                        path1=fileListPaths[int(path[0])]
                    else:
                        await rm.msg(ctx,"**❌ Invalid Index!**\n\nTry:\n**!file list**",color=rm.color('colorforError'))
                        return False
                else:
                    await rm.msg(ctx,"**⚠ Index Called Before Indexing!**\n\nUse:\n**!file list**  -> to do indexing",color=rm.color('colorforError'))
                    return False
            else:
                 path1=" ".join(path)
                 
    else:
        path1=""
    print(path1)
    return path1
    
    

async def file(ctx, command, *args):
    
    editMsgBool=False    
    p=configs.BOT_PREFIX
    filesystem_control = FileSystemControl(configs.initial_path)
    await filesystem_control.load_path_from_memory()
    
    async def set_absolute_path(*path):
        path=" ".join(path)
        if path!="":
            if not Path(path).exists():
                await rm.msg(ctx,f"**Path**: ~~{path}~~\n\n**Entered Path does not exists!**",color=rm.color('colorforError'))
            else:
                new_path = await filesystem_control.set_path(ctx,path, False)
                return '**Current location set to** {}'.format(new_path)
        else:
            await rm.msg(ctx,"**Please enter the path!**",color=rm.color('colorforError'))

    async def set_relative_path(*path):
        path=await path_getter(ctx,[i for i in path])
        if path==False:return None
        print("this is the final relative path:  ",path)
        new_path = await filesystem_control.set_path(ctx,path, True)
        return f'**Current location{" set to**" if path!="" else "**:"} {new_path}'

    async def retrive_file(*path):
        path=await path_getter(ctx,[i for i in path])
        if path==False:return None
        file_path = await filesystem_control.retrieve_file(ctx,path)
        upload_size=float(configs.FILE_UPLOAD_SIZE)
        file_size=os.path.getsize(file_path)/1000000
        print(f"Upload Size: {upload_size}\nfile size: {file_size}")
        if file_size<=upload_size:
            msg=await rm.msg(ctx,f"**Retrieving {file_path.name} file.**",color=rm.color('colorforWaitingMsg'))            
            attacha=await rm.msgwithAttachment(ctx,"**Retrieved!**",file= discord.File(file_path))
            print (attacha.attachments[0].url)
            await rm.editMsgwithAttachment(ctx,attacha,f"**Retrieved!**\n\n**Path**: {file_path}\n▸ [share link]({attacha.attachments[0].url})")
            await msg.delete()
        else:
            await rm.msg(ctx,f"**File size is too large!** ({file_size}Mb)\n\n**Path**: {file_path}\n\nFYI, If you are an Nitro User, you can the default file upload size {upload_size}Mb from Reco's env file.",color=rm.color('colorforError'))
       
            
            # Exception as e:


            #     print(f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}")
            #     e=f"Error: at line {e.__traceback__.tb_lineno} of\n{__file__}\n**{e}**"
            #     await rm.msg(ctx,e,color=0xF70000)
        

    
    async def download_file(url, file_path,rsave=False):


        if url == None:
            return 'No direct file URL was provided'

        finalFilepath="\n\n"

        filename = url[url.rfind("/") + 1:]

        r = requests.get(url, allow_redirects=True)
        if r.status_code / 100 != 2:
            raise Exception('Download request from Discord returned {}'.r.status_code)
        file = r.content
        if rsave:
            file_path = await filesystem_control.relative_save_file(file, filename, file_path)
        else:
           file_path = await filesystem_control.save_file(file, filename, file_path)
        finalFilepath=finalFilepath+f"**{filename}**: {file_path}\n▸ [share link]({url})\n\n"
        return 'File Saved on {}'.format(finalFilepath)

    async def save_file(input="",path=configs.RECO_PATH):
        url=input
        if input=="folder":
            savefoldercheck()
            await rm.msg(ctx,f"**Opening saved_files Directory.**\n\n**Path**{configs.RECO_PATH}\\downloads\\saved_files")
            os.startfile("downloads\\saved_files")
            return None

       
        if url.__contains__("https:") and url.split("/")[-1].__contains__('.'):
            url=url.split('?')[0]
            return await download_file(url,configs.RECO_PATH)
            
                
        elif len(ctx.message.attachments)!=0:
            lenght=len(ctx.message.attachments)
            print(ctx.message.attachments," ",len(ctx.message.attachments))
            finalFilepath="\n\n"
            FileName_has_underscore=False
            msg=await rm.msg(ctx,f'**Uploading {"files" if lenght>1 else "file"} to your system.**',color=rm.color('colorforWaitingMsg'))
            for i in range(len(ctx.message.attachments)):
                filename = ctx.message.attachments[i].filename
                if filename.__contains__("_"):
                    FileName_has_underscore=True
                url = ctx.message.attachments[i].url
    
                r = requests.get(url, allow_redirects=True)
                if r.status_code / 100 != 2:
                    raise Exception('Download request from Discord returned {}'.r.status_code)
                file = r.content
                file_path = await filesystem_control.save_file(file, filename, path)
    
                finalFilepath=finalFilepath+f"**{filename}**: {file_path}\n▸ [share link]({url})\n\n"
            if FileName_has_underscore:
                finalFilepath=finalFilepath+"\n\n"+f"⚠ **Share link{'s**' if lenght>1 else '**'} may not work in **Discord Mobile App** if **FileName** has **underscore**(**_**) or **Space** used."
                
            await msg.delete()

            return '**Files Saved on** {}'.format(finalFilepath)
        else:
            await rm.msg(ctx,"**Please add Attachements or paste Discord Attachement URL.**\n\nWhat is **save** command for?\n**save** command helps you to save attachments in **saved_files** directory. Use **!file save folder** command to open the directory.",color=rm.color("colorforError"))
    
    async def relative_save_file(url="",path=None):

       
        if url.__contains__("https:") and url.split("/")[-1].__contains__('.'):
            url=url.split('?')[0]
            return await download_file(url,path,rsave=True)
            
                
        elif len(ctx.message.attachments)!=0:
            lenght=len(ctx.message.attachments)
            print(ctx.message.attachments," ",len(ctx.message.attachments))
            finalFilepath="\n\n"
            msg=await rm.msg(ctx,f'**Uploading {"files" if lenght>1 else "file"} to your system.**',color=rm.color('colorforWaitingMsg'))
            FileName_has_underscore=False
            for i in range(len(ctx.message.attachments)):
                filename = ctx.message.attachments[i].filename
                if filename.__contains__("_"):
                    FileName_has_underscore=True
                url = ctx.message.attachments[i].url
    
                r = requests.get(url, allow_redirects=True)
                if r.status_code / 100 != 2:
                    raise Exception('Download request from Discord returned {}'.r.status_code)
                file = r.content
                file_path = await filesystem_control.relative_save_file(file, filename, path)
    
                finalFilepath=finalFilepath+f"**{filename}**: {file_path}\n▸ [share link]({url})\n\n"
            if FileName_has_underscore:
                finalFilepath=finalFilepath+"\n\n"+f"⚠ **Share link{'s**' if lenght>1 else '**'} may not work in **Discord Mobile App** if **FileName** has **underscore**(**_**) or **Space** used."
     
            await msg.delete()

            return '**Files Saved on** {}'.format(finalFilepath)
        else:
            await rm.msg(ctx,"**Please add Attachements or paste Discord Attachement URL.**\n\nWhat is **rsave** command for?\n**rsave** command helps you to save attachments at relative location.",color=rm.color("colorforError"))


    async def list_directory(*ignore):
        print("Ignores: ",ignore)
        if command=='list':
            if len(args)>0:
                filterName=ctx.message.content[11:]
            else:
                filterName=None
        
        path=None
        if len(ignore)>=1:
            filterName=ctx.message.content[11:]
            if ignore[0].isnumeric():
                path=await path_getter(ctx,[i for i in ignore])
                if len(ignore)>1:
                   filterName=filterName.split(" ",1)[1]
                else:
                    filterName=None            
                print("filtername :  ",filterName)
            elif ignore[0]=="..":
                path=".."
            if path==False:return None
        print("filtername :  ",filterName)



        
        output = await filesystem_control.list_directory(ctx,file_path=path)
        dir_list=output[0]
        path=output[1]
        filtered_dir_list=[]
        addInfo=""
        print(dir_list,path)
        
        if filterName!=None and filterName!="..":
            for i in dir_list:
                f=i.name.lower()
                if f.__contains__(filterName.lower()):
                    filtered_dir_list.append(i)
        if filtered_dir_list!=[] and (filterName!=None and filterName!="..") :
            dir_list=filtered_dir_list
            addInfo=f"**Searched Keyword:** {filterName}\n\n"
        elif filterName!=None and filterName!="..":
            dir_list=f"**Searched Keyword:** {filterName}\n\n**No files found!**"
        
        
        if (filterName==None or filterName=="..") or (len(args)>0 and filtered_dir_list!=[]):
            fileListPaths.clear()
            result = f"**Path:** {path}\n\n**Files Count:** {len(dir_list)}\n\n{addInfo}**Directory items:**\n\n"
            for n,item in enumerate(dir_list):
               filename=item.name.replace("_","\_")
               result += f"{n} ⪧ {filename}\n"
            
            fileListPaths.extend(dir_list)
            await rm.extendableMsg(ctx,result)
            
        else:
            await rm.msg(ctx,dir_list,color=rm.color("colorforError"))

    async def open_path(*path):
        path=await path_getter(ctx,[i for i in path])
        if path==False:return None
        elif path=="":path=None

        print("This is open module: ",path)
        file_path =await filesystem_control.retrieve_file(ctx,path,open=True)
        embedMsg=""
        if file_path.exists():
            if file_path.is_file():
                embedMsg=f"**Opening File**: **{file_path.name}**"
            elif file_path.is_dir():
                embedMsg=f"**Opening Directory**: **{file_path.name}**"
        if embedMsg!="":
           await rm.msg(ctx,embedMsg)  
           os.startfile(file_path)   
        else:
            await rm.msg(ctx,f'**Path**: ~~{file_path}~~\n\n**Invalid Path!**',color=rm.color('colorforError'))
        

        return None


    switcher = {
        'absolute': set_absolute_path,
        'relative': set_relative_path,
        'list': list_directory,
        'retrieve': retrive_file,
        'save': save_file,
        'rsave': relative_save_file,
        'open': open_path,
        
    }
    if command in switcher.keys() and len(args) > 0:
        message = await switcher[command](*args)
    elif command in switcher.keys():
        message = await switcher[command]()
    else:
        await rm.msg(ctx,
        txt=f'''**Help - {p}file**

**Commands:**
```{p}file absolute <PATH>
{p}file relative <PATH>
{p}file list     <Filter>
{p}file retrieve <PATH>
{p}file save     <Discord Attachments>/<URL>
{p}file save     folder
{p}file rsave    <Discord Attachments>/<URL> 
{p}file open     <PATH>```
                
[for more information](https://github.com/Arvinth-Krishna/Reco-PC-Server#-file--)'''
        )
    if command in switcher.keys() and command !='list':
        if message:
            message=message.replace("_","\_")
            await rm.msg(ctx,message)
