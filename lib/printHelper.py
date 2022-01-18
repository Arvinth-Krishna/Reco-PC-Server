


import os,configs,win32api,win32print

import requests
from glob import glob
from lib.reco_embeds import recoEmbeds as rm
from pathlib import Path



printer_number=configs.CURRENT_PRINTER_NUMBER
current_Printer= int(printer_number) if printer_number.isnumeric() else None
no_of_copies=configs.NO_OF_COPIES
color_Mode=configs.COLOR_MODE            # 1=Black, 2=Color
orinetation=configs.ORIENTATION          # 1=Potariat, 2=Landscape
startRange=None
endRange=None

path = configs.RECO_PATH

def colorConverter(input):
    if input=="b":
        return 1
    elif input=="c":
        return 2
    else:
        return 1

def orinetationConverter(input):
    if input=="p":
        return 1
    elif input=="l":
        return 2
    else:
        return 1

def  print_Folders_Checker():
    if not os.path.isdir('printer'):
        os.mkdir("./printer")  
    if not os.path.isdir('printer/temp_print'):
        os.mkdir("./printer/temp_print")  
    if not os.path.isdir('printer/uploaded_files'):
        os.mkdir("./printer/uploaded_files")


async def recoPrint(ctx,allPrinterTxt,printerName,rpcolor_Mode,rpno_of_copies,rporinetation,files_dir,pathfile=False):
           if  current_Printer==None:
                await rm.msg(ctx,allPrinterTxt+"\n To change Current Printer: **!printer setcurrentprinter NUM**")
           try:
                PRINTER_DEFAULTS = {"DesiredAccess":win32print.PRINTER_ALL_ACCESS}  
                pHandle = win32print.OpenPrinter(printerName,PRINTER_DEFAULTS) 
                properties = win32print.GetPrinter(pHandle, 2)  
                properties["pDevMode"].Color =rpcolor_Mode
                properties["pDevMode"].Copies = rpno_of_copies
                properties["pDevMode"].Orientation = rporinetation
                pDevModeObj= properties["pDevMode"]
                
                win32print.SetPrinter(pHandle,2,properties,0) 
             
                devmode=pDevModeObj  
                for n in dir(devmode):  
                     print (f"{n} :{getattr(devmode,n)}")  
                filesCount=0
                if pathfile==False:
                    for f in glob(files_dir, recursive=False):
                        print(f)
                        filesCount+=1
                        win32api.ShellExecute(0, "print", f, None,  ".",  0)
                elif pathfile==True:
                    print("Inside pathfile true:  ",files_dir)
                    filesCount+=1
                    win32api.ShellExecute(0, "print", files_dir, None,  ".",  0)

                   
                win32print.ClosePrinter(pHandle)
                await rm.msg(ctx,f"Current Printing Printer: **{printerName}**\n\n| Files: **{filesCount}** | Color: **{'Black' if rpcolor_Mode==1 else 'Color'}** | Copies: **{rpno_of_copies}** | Orientation: **{'Portrait' if rporinetation==1 else 'Landscape'}** |\n\n**Sending Print Job...**")
           except Exception as e:
                print(f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}")
                e=f"Error: at line {e.__traceback__.tb_lineno} of\n{__file__}\n**{e}**\n\n**Printer Name:** {printerName}"
                await rm.msg(ctx,e,color=0xF70000)

async def reco_print_file_save(file,file_name,custom_path):
        file_path=configs.RECO_PATH+custom_path
        file_path=str(Path(file_path))
        path = Path(file_path,file_name)
        path.write_bytes(file)
        return path


async def print_file_getter(ctx,path):
            print_Folders_Checker()

            finalFilepath="\n\n"

            for i in range(len(ctx.message.attachments)):
                filename = ctx.message.attachments[i].filename
                url = ctx.message.attachments[i].url

                r = requests.get(url, allow_redirects=True)
                if r.status_code / 100 != 2:
                    raise Exception('Download request from Discord returned {}'.r.status_code)
                file = r.content
    
                file_path = await reco_print_file_save(file, filename, path)

                finalFilepath=finalFilepath+f"**{filename}**: {file_path}\n\n"

            return finalFilepath

    