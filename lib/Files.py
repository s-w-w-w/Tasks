from pathlib import Path
import os
"""
Files - handle operations on a single file
    Version: 1.0.10
    Methods:
        __init__() - constructor
        __readAll() - read all file contents
        removeOne() - remove line number "index" from file
        writeAll() - write all contents to a file
        append() - append a value to a file
        get() - get file contents
        count() - find number of items
        clear() - clear file contents
        delete() - delete file
"""
class Files(object):

    """
    Constructor
    """
    def __init__(self,aFile):    
        self.__f = aFile
        self.__contents = []  

        # check if parent directory for given file exists 
        if not os.path.isdir(self.__f.parents[0]):
            error = f'parent directory for {aFile} does not exist!'
            raise Exception(error)

        if not self.exists():
            fd = open(self.__f, 'w', encoding='UTF-8').close()
        else:
            self.__readAll()
        
    """
    __readAll() - read all file contents
    """
    def __readAll(self):
        fd = open(self.__f, 'r', encoding='UTF-8')
        self.__contents = fd.readlines()
        fd.close()
        return True                

    """
    count() - find number of items
    """
    def count(self):
        return len(self.__contents)

    """
    Check if file exists
    """    
    def exists(self):
        if self.__f.is_file():
            return True
        return False            
    
    """
    writeAll() - write all contents to a file
    """
    def writeAll(self):
        with open(self.__f, 'w') as f:
            for line in self.__contents:
                line = line.rstrip()
                f.write(f"{line}\n")
        
        return True        
 
    """
    append() - append a value to a file
        input: 
            value - string
        output: 
            Files instance
    """
    def append(self,value):
        fd = open(self.__f, 'a',encoding='UTF-8')
        value = value.rstrip()
        fd.write(f"{value}\n")
        fd.close()           
        
        self.__readAll();
        return self
        
    """
    get() - get file contents
        input: none
        output: array of strings
    """    
    def get(self):
        return self.__contents  
        

    """
    removeOne() - Remove line number "index" from file
        Indexing starts at 0
        Input: index - nonnegative integer
    """
    def removeOne(self,index):
        if 0 <= index < self.count():
            self.__contents.pop(index)
            return self.writeAll()
        else: 
            raise IndexError("Index not in range")
        
        
    """
    clear() - clear file contents
    """    
    def clear(self):
        Path.unlink(self.__f)   
        self.__contents = []             
    
    """
    delete() - delete file
    """    
    def delete(self):
        Path.unlink(self.__f)
        self.__contents = []
