# Module: echo
# Description: Turns command output display to discord chat on and off (works for !cmd and !powershell)
# Usage: !echo off or !echo on
# Dependencies: None


import os
import configs
from lib.reco_embeds import recoEmbeds as rm
from lib.filesystem_control import FileSystemControl
from lib import printHelper
import win32api,requests
from pathlib import Path
import win32print 
from glob import glob
import shutil



async def printer(ctx,mode, *inputs):
    printHelper.print_Folders_Checker()
    if len(inputs)==0:
        inputs=['None','None']
    all_printers = [printer[2] for printer in win32print.EnumPrinters(2)]
    allPrinterTxt="To choose a printer:\n\n"+"\n".join([f"**{n}** **{p}**" for n, p in enumerate(all_printers)])+"\n"
    print(inputs)
    rpCurrentJobPrinterNumber=rpno_of_copies=rpcolor_Mode=rporinetation=rpstartRange=rpendRange=printer=""
    print(rpno_of_copies,rpcolor_Mode,rporinetation,rpstartRange,rpendRange)
    for i in inputs:
        print(i[:1]," ",i[1:])
        if i[:1]=="n"and i[1:].isnumeric():
            rpno_of_copies=int(i[1:])
        elif i[:1]=="p" and i[1:].isnumeric():
            if int(i[1:])<len(all_printers):
               rpCurrentJobPrinterNumber=int(i[1:]) 
        elif i[:1]=="c" and i[1:] in('b','c'):
            rpcolor_Mode=i[1:]
        elif i[:1]=="o" and i[1:] in('p','l'):
            rporinetation=i[1:] 
        elif i[:1]=="r"and i.__contains__('-'):
            rangeSeperator=i[1:].split('-')
            rpstartRange=int(rangeSeperator[0])
            rpendRange=int(rangeSeperator[1])

    rpCurrentJobPrinterNumber = rpCurrentJobPrinterNumber if rpCurrentJobPrinterNumber!="" else  int(printHelper.current_Printer) if (printHelper.current_Printer!=None) else all_printers.index(win32print.GetDefaultPrinterW())
    rpno_of_copies=rpno_of_copies or int(printHelper.no_of_copies)
    rpcolor_Mode=printHelper.colorConverter(rpcolor_Mode or printHelper.color_Mode) 
    rporinetation=printHelper.orinetationConverter(rporinetation or printHelper.orinetation)
    rpstartRange=rpstartRange or printHelper.startRange
    rpendRange=rpendRange or printHelper.endRange

    printerName=all_printers[rpCurrentJobPrinterNumber]
    print(rpCurrentJobPrinterNumber)
    print(printerName)
        
    print(f"Mode: {mode}\nrpCurrentJobPrinterNumber: {rpCurrentJobPrinterNumber}\nrpcopies: {rpno_of_copies}\nrpcolor: {rpcolor_Mode}\nrporientation: {rporinetation}\nrprangestar :{rpstartRange}\nrpendrange :{rpendRange}")

    print(f"Mode: {mode}\ncopies: {printHelper.no_of_copies}\ncolor: {printHelper.color_Mode}\norientation: {printHelper.orinetation}\nrangestar :{printHelper.startRange}\nendrange :{printHelper.endRange}")
        

    path=configs.RECO_PATH
    print("Current Reco PC Server Path:",path)

    print_Uploaded_files_dir = str(path) + "/printer/uploaded_files/*"
    quick_Print_files_dir = str(path) + "/printer/temp_print/*"
    print("Printer Upload Folder Path:",print_Uploaded_files_dir)


    if mode in ("showprinters","showprinter","showp"):
        await rm.msg(ctx,allPrinterTxt+"\n To set Current printer: **!printer setcurrentprinter NUM**")

    elif mode in ("showcurrentprinter","showcp"):
        if printHelper.current_Printer!=None:
            await rm.msg(ctx,f"☑ Current Printer : **{all_printers[printHelper.current_Printer]}**")
        else:
            await rm.msg(ctx,"**No Current Printer assigned.**\n\nFYI, In Reco !printer\n **p__NUM__ > Current Printer > Default Printer**")
    elif mode in ("showdefaultprinter","showdp"):
        await rm.msg(ctx,f"☑ Current Default Printer in your system : **{win32print.GetDefaultPrinterW()}**")


    elif mode in("setcurrentprinter","setcp"):
        if  inputs[0].isnumeric():
            if int(inputs[0])<len(all_printers):
               printHelper.current_Printer=int(inputs[0])
               await rm.msg(ctx,f"✅ Current Printer : **{all_printers[printHelper.current_Printer]}**\n\n\n**FYI**, In Reco !printer\n p__NUM__ > Current Printer > Default Printer")
            else:
                await rm.msg(ctx,f"❌ **Invalid Printer Number**\n\nTry:\n**!printer showprinters**",color=rm.color('colorforError'))
        elif inputs[0].lower() in ('reset','none'):
            printHelper.current_Printer=None
            await rm.msg(ctx,'✅ Current Printer : **None**\n\n\n**FYI**, In Reco !printer\n p__NUM__ > Current Printer > Default Printer')
        else:
                await rm.msg(ctx,f"❌ **Invalid Printer Command.**\n\nTry:\n**!printer**    -> for help",color=rm.color('colorforError'))
        
    elif mode in ("setdefaultprinter","setdp") and inputs[0].isnumeric() :
        if int(inputs[0])<len(all_printers):
            win32print.SetDefaultPrinter(all_printers[int(inputs[0])])
            await rm.msg(ctx,f"✅ Default Printer : **{win32print.GetDefaultPrinterW()}**\n\n\n**FYI**, In Reco !printer\n p__NUM__ > Current Printer > Default Printer")
        else:
            await rm.msg(ctx,f"❌ **Invalid Printer Number**\n\nTry:\n**!printer showprinters**",color=rm.color('colorforError'))


    elif mode =='upload' or  (mode=='folder'and inputs[0] =='upload'):
        bool_attachments=False
        if len(ctx.message.attachments)!=0:
           bool_attachments=True
           print(ctx.message.attachments," ",len(ctx.message.attachments))
           finalFilepath=await printHelper.print_file_getter(ctx,"\printer\\uploaded_files")
           await rm.msg(ctx,f"**Uploaded Files:** {finalFilepath}\nTo all Uploaded Files:\n**!printer folder show**")
        else:
            if not bool_attachments:
               await rm.msg(ctx,"**Please Add Attachments**(files) **to upload.**",color=rm.color('colorforError'))
    
    elif mode=="folder" and "delete" == inputs[0]:
        files = glob(print_Uploaded_files_dir)
        if len(inputs)>1 and len(files)!=0:
            if inputs[1].isnumeric():
                if int(inputs[1])<=len(files)-1:
                    await rm.msg(ctx,f"Successfully Deleted - **{files[int(inputs[1])].split(chr(92))[-1]}")
                    os.remove(files[int(inputs[1])])
                else:
                    await rm.msg(ctx,f"**❌ Invalid File Number!**.\n\nTry\n**!printer folder show**",color=rm.color('colorforError'))
        else:            
           if len(files)!=0:
               for f in files:
                 os.remove(f)
               await rm.msg(ctx,f"Files Count: **{len(files)}**\n\n**All Files Deleted**.\n\n**Directory Path**: {print_Uploaded_files_dir[:-2]}")
           else:
               await rm.msg(ctx,f"**Directory is Empty!**\n\n**Folder Path**: {print_Uploaded_files_dir[:-2]}")
    

    elif mode=="folder" and inputs[0] in ('None','show','list'):
        
        files = glob(print_Uploaded_files_dir)
        filenames=f"Files Count: **{len(files)}** \n\n"+"\n".join([f"**{n}** - **{f.split(chr(92))[-1]}**" for n, f in enumerate(files)])+"\n\nTo delete files:\n**!printer folder delete**\nor\n**!printer folder delete __FileNumber__**"
        
        if len(files)!=0:
            await rm.msg(ctx,f"{filenames}")
        else:
            await rm.msg(ctx,f"**No Files to show.**\n\n**Directory is Empty!**")
    elif mode=="folder" and inputs[0]=="open":
        
        await rm.msg(ctx,"**Opening Uploaded_files Directory.**")
        os.startfile("printer\\uploaded_files")


    elif mode=="folder" and inputs[0]=="print" :
           filesCount=len([name for name in os.listdir(print_Uploaded_files_dir[:-2]) if os.path.isfile(os.path.join(print_Uploaded_files_dir[:-2], name))])
           if filesCount!=0:
                await printHelper.recoPrint(ctx,allPrinterTxt,printerName,rpcolor_Mode,rpno_of_copies,rporinetation,print_Uploaded_files_dir)
           else:
                await rm.msg(ctx,"**Oops!, No files to print.**\n\nTry:\n**!printer upload**",color=rm.color('colorforError'))

    elif mode=="print":          
        bool_attachments=False
        temp_print_checker=False  
        path_file_print_bool=False
        print(ctx.message.attachments," ",len(ctx.message.attachments))
        try:
            shutil.rmtree(quick_Print_files_dir[:-2])
            temp_print_checker=True
        except:
            print("Can't able to delete all files from the temp_print folder. Because some files may be being used by another applictaion")
        
        if inputs[0]!=None:
            if os.path.exists(inputs[0]):
                path_file_print_bool=True
                await printHelper.recoPrint(ctx,allPrinterTxt,printerName,rpcolor_Mode,rpno_of_copies,rporinetation,str(Path(inputs[0])),pathfile=True)

            


        if len(ctx.message.attachments)!=0:
            bool_attachments=True

        if temp_print_checker and bool_attachments:
            
            finalFilepath=await printHelper.print_file_getter(ctx,"\printer\\temp_print")
            await rm.msg(ctx,f"**Printing Files:** {finalFilepath}")
            await printHelper.recoPrint(ctx,allPrinterTxt,printerName,rpcolor_Mode,rpno_of_copies,rporinetation,quick_Print_files_dir)
        
        else:
            if not bool_attachments and path_file_print_bool!=True:
               await rm.msg(ctx,"**Please Add Attachments**(files) or **File Path to print.**",color=rm.color('colorforError'))
            if not temp_print_checker and path_file_print_bool!=True:
               await rm.msg(ctx,f"**Something went wrong!.** Please, close all temp_print's files opened.\n\n**temp_print** folder is not empty.\n\n**Path**: {quick_Print_files_dir[:-2]}",color=rm.color('colorforError'))
  
  
    elif mode=="jobs":
            print("inside show print jobs")
            jobs = []
            printjobNames=""
            
            count=0
            
            for p in win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL,None, 1):
                flags, desc, name, comment = p
            
                phandle = win32print.OpenPrinter(name)
                print_jobs = win32print.EnumJobs(phandle, 0, -1, 1)
                
                
                if len(print_jobs)!=0:
                   print("inside job counterrr")
                   jobs.extend(list(print_jobs))

                namep=f'**{name}:** \n\n' if len(print_jobs)!=0 else ''
                   
                printjobNames=printjobNames+f"{namep}"+"\n".join([f"**{n}** - **{f['pDocument']}**" for n, f in enumerate(print_jobs,count) ])
                count=len(jobs)

                win32print.ClosePrinter(phandle)
            print(jobs)
            if inputs[0] in ('None','show','list') and len(jobs)!=0:
                await rm.msg(ctx,printjobNames)

            elif inputs[0]=="delete" and len(jobs)!=0:
                if len(inputs)>1:
                    if inputs[1].isnumeric():
                        if  int(inputs[1])<len(jobs):
                           deleteJobNumber=int(inputs[1])
                           phandle = win32print.OpenPrinter(jobs[deleteJobNumber]["pPrinterName"])
                           win32print.SetJob(phandle, jobs[deleteJobNumber]["JobId"], 0, None, win32print.JOB_CONTROL_DELETE)
                           await rm.msg(ctx, f"**Successfully Cancelled!**\n\n**{deleteJobNumber}: {jobs[deleteJobNumber]['pDocument']}**({jobs[deleteJobNumber]['JobId']})")
                        else:
                           await rm.msg(ctx,f"❌ **Invalid Job Number**\n\nTry:\n**!printer jobs**",color=rm.color('colorforError'))
                else:
                        for i in range(len(jobs)):
                            phandle = win32print.OpenPrinter(jobs[i]["pPrinterName"])
                            win32print.SetJob(phandle, jobs[i]["JobId"], 0, None, win32print.JOB_CONTROL_DELETE)
                        await rm.msg(ctx, f"**Successfull Deleted all Print Jobs!**")
            elif len(jobs)==0:
                await rm.msg(ctx, f"**No Print Jobs to Show/Delete.**\n")
                
    elif mode in (None,"reco"):
        prefix=configs.BOT_PREFIX
        allPrinterTxt="\n".join([f"{n} {p}" for n, p in enumerate(all_printers)])+"\n"
        pembed=await rm.printConfigEmbed(ctx,
        txt=f'''```fix\nCurrent Printer: {printerName}\n```''',
        fieldname1="Printer Configs:",
        fieldvalue1=f'''```Printer No   (p) : {configs.CURRENT_PRINTER_NUMBER}
No of Copies (n) : {configs.NO_OF_COPIES}
Color Mode   (c) : {"Black" if printHelper.colorConverter(configs.COLOR_MODE)==1 else "Color"}
Orientation  (o) : {"Portrait" if printHelper.orinetationConverter(configs.ORIENTATION)==1 else "Landscape"}```''',
        fieldname2="Available Printers:",
        fieldvalue2=f'''```{allPrinterTxt}```''',
        fieldname3=f"{prefix}printer Commands:",
        fieldvalue3=f'''```!printer showprinters           or showp
{prefix}printer showcurrentprinter     or showcp
{prefix}printer showdefaultprinter     or showdp
{prefix}printer setcurrentprinter NUM  or setcp NUM
{prefix}printer setcp  reset           or setcp none
{prefix}printer setdefaultprinter NUM  or setdp NUM
{prefix}printer folder list            or folder   
{prefix}printer folder open
{prefix}printer folder upload          or upload
{prefix}printer folder delete
{prefix}printer folder delete NUM
{prefix}printer jobs   list            or jobs
{prefix}printer jobs   delete
{prefix}printer jobs   delete Num
{prefix}printer folder print (optional Attributes: p_ n_ c_ o_)
{prefix}printer print        (optional Attributes: p_ n_ c_ o_)
{prefix}printer print "FILE_PATH-WITH DOUBLE QUOTES"  (optional Attributes: p_ n_ c_ o_)```''',
        fieldname4="FYI 😉:",
        fieldvalue4=f'''```🔸 Optional Attributes can be used with print parameters.
🔸 All Optional Attributes are optional.
🔸 Remember:
   p(NUM) > Current Printer > Default Printer
🔸 Optional Attributes -> p(NUM) n(NUM) c(b/c) o(p/l)
   Explanations:
      p(Num) -> p1 -> Printer Number
      n(NUM) -> n1 -> No of Copies
      c(b/c) -> cb -> Color Mode 
                 b -> Black & White
                 c -> Color
      o(p/l) -> op -> Orientation
                 p -> Potrait
                 l -> Landscape 
eg: 
   Read 1st point in FYI.
   {prefix}printer folder print n2 cc
   {prefix}printer folder print p3 n2 op
   {prefix}printer print n5 ol
   {prefix}printer print \"C:\\Users\\krish\\Desktop\\print test.txt\" n2```''',
       fieldname5= "reco" if mode=="reco" else None
  
   ),
    else:
        await rm.msg(ctx,"**❌ Invalid Printer Command.**\n\nTry:\n**!printer**    -> for help",color=rm.color('colorforError'))

    