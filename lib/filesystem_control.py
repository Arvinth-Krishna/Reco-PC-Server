
from lib.memory_management import memory
from pathlib import Path
from lib.reco_embeds import recoEmbeds as rm
import os,configs



class FileSystemControl:



    _CURRENT_PATH = '_current_path'
    
    _current_path = ""
    
    def __init__(self,initial_path=None):
        
        if initial_path:
            path = Path(initial_path)
            
        else:

            path = Path.cwd()
        
        path = self._check_path(path)
             
        self._current_path = path
        print("This the path from path module:  ",path)
    
    def _check_path(self,path):
        
        path = path.resolve()
        
        if not path.exists():
            raise {Exception('Path [{}] does not exists!'.format(path)),
            }      
        return path

    async def _absolute_path_check(self,ctx,path):
        path =path.resolve()
        
        if not path.exists():
            pathBack = Path(*path.parts[:-1])
            if pathBack.exists():
                await rm.msg(ctx,f"**Path**: ~~{path}~~\n\n**Entered Path does not exists!**",color=rm.color('colorforError'))
                return pathBack               
            raise {Exception('Path [{}] does not exists!'.format(path)),
            await rm.msg(ctx,f"**Path**: ~~{path}~~\n\n**Entered Path does not exists!**",color=rm.color('colorforError'))
            }      
        return path 

    def get_current_path(self):
        return self._CURRENT_PATH
    
    @memory
    async def load_path_from_memory(self,memory):
        memory_path = await memory.get(self._CURRENT_PATH)
        if memory_path:
            self._current_path = memory_path
    
    @memory
    async def set_path(self,ctx, path, relative=False,memory=None):
        new_path = Path(path) if not relative else Path(str(self._current_path),path)
        new_path = await self._absolute_path_check(ctx,new_path)
        await memory.set(self._CURRENT_PATH,new_path)
        return new_path
    
    @memory
    async def list_directory(self,ctx,file_path=None,memory=None):
        if file_path!=None:
            dir_path=await FileSystemControl.set_path(self,ctx,file_path,relative=True)
        else:
            dir_path =  self._current_path 
        
        
        if not dir_path.is_dir():
            dir_path = Path(*dir_path.parts[:-1])
            await memory.set(self._CURRENT_PATH,dir_path)
        filesName,path=[x for x in dir_path.iterdir()],dir_path
        
        return [filesName,path]
        
    @memory
    async def retrieve_file(self,ctx, file_name=None,open=False,memory=None):
        path=self._current_path
        
        if (self._current_path.is_file() or open) and file_name==None :
            return self._current_path
        elif self._current_path.is_file() and file_name!=None:
            path = Path(*path.parts[:-1])
            file_path= Path(path,file_name)
            await memory.set(self._CURRENT_PATH,file_path)
            return file_path
        
        else:
            if file_name:
                file_path = Path(self._current_path,file_name)
                if file_path.is_file() or open:
                    return file_path
                
        raise {Exception('No file specified'),
        await rm.msg(ctx,f'**Path**: {f"~~{file_path}~~" if file_name else self._current_path}\n\n{"**Invalid Path!**"if file_name else "**No file specified!**"}',color=rm.color('colorforError'))
        }
        
    
    async def save_file(self,file,file_name,file_path=None):
        if not os.path.isdir('downloads'):
            os.mkdir("./downloads")  
        if not os.path.isdir('downloads/saved_files'):
             os.mkdir("./downloads/saved_files")  
        file_path = file_path if file_path else self._current_path 
        file_path=str(file_path)+"\downloads\saved_files"
        file_path=str(Path(file_path))
        print("this is the save file path by gak: ",file_path)

        path = Path(file_path,file_name)
        path.write_bytes(file)
        return path
    
    async def relative_save_file(self,file,file_name,file_path=None):
        file_path = file_path if file_path else self._current_path 
        path = Path(file_path,file_name)
        path.write_bytes(file)
        return path

    
    
 
 
    
