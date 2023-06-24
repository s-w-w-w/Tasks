from pathlib import Path
import os
"""
Files - handle operations on a single file
    Version: 1.0.13
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

        # check if parent directory for given file exists 
        if not os.path.isdir(self.__f.parents[0]):
            error = f'parent directory for {aFile} does not exist!'
            raise Exception(error)

        if not self.exists():
            open(self.__f, 'w', encoding='UTF-8').close()
        
    """
    Check if file exists
    """    
    def exists(self):
        if self.__f.is_file():
            return True
        return False            

    """
    get() - get file contents
        input: none
        output: array of strings
    """    
    def get(self):
        data = []
        fd = open(self.__f, 'r', encoding='UTF-8')
        data = fd.readlines()
        fd.close()
        return data
    
    """
    writeAll() - write all contents to a file
    """
    def write(self, data):
        with open(self.__f, 'w') as f:
            for line in data:
                line = line.rstrip()
                f.write(f"{line}\n")
        
        return True        
 
    """
    append() - append a value to a file
        input: 
            value - string
        output: 
            Bool - True
    """
    def append(self,value):
        fd = open(self.__f, 'a',encoding='UTF-8')
        value = value.rstrip()
        fd.write(f"{value}\n")
        fd.close()           
       
        return True                

    """
    update() - update string at index index with a new value
        Indexing starts at 0
        Input: 
            index - nonnegative integer
            value - string
    """
    def update(self,index, value):
        data = self.get()
        if 0 <= index < len(data):
            data[index] = value
            return self.write(data)
        else: 
            raise IndexError("Index not in range")
            
    """
    supplement() - append extra value to a string at index index
        Indexing starts at 0
        Input: 
            index - nonnegative integer
            value - string
            
        Output: 
            Bool - True
    """
    def supplement(self,index, value):
        data = self.get()
        if 0 <= index < len(data):
            data[index] = data[index].rstrip() + f" {value}"
            return self.write(data)
        else: 
            raise IndexError("Index not in range")            
        

    """
    removeOne() - Remove line number "index" from file
        Indexing starts at 0
        Input: index - nonnegative integer
    """
    def removeOne(self,index):
        data = self.get()
        if 0 <= index < len(data):
            data.pop(index)
            return self.write(data)
        else: 
            raise IndexError("Index not in range")
        
        
    """
    clear() - clear file contents
    """    
    def clear(self):
        open(self.__f, 'w', encoding='UTF-8').close()
        return True                   
    
    """
    delete() - delete file
    """    
    def delete(self):
        Path.unlink(self.__f)
