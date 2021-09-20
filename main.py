import os
import sys
from colorama import Fore, Back
import base64, pyperclip
from time import sleep
from tqdm import tqdm, trange


os.system("title yin")
os.system('cls||clear')
if sys.version_info[0] < 3:
	pyversion = python_version()
	print("Alert! Your python version is %s. Use python version 3> to run this code" %(pyversion))
	exit(1)
print(f"""
{Fore.MAGENTA}
    
                                ▓██   ██  ██  ███▄    █ 
                                 ▒██  ██  ██  ██ ▀█   █
                                  ▒██ ██  ██  ██  ▀█ ██▒
                                  ░ ▐██▓░░██░ ██▒  ▐███▒
                                  ░ ██▒▓░░██░▒██░    ██░
                                   ██▒▒▒ ░▓  ░ ▒░   ▒ ▒  
                                 ▓██░▒░  ▒ ░░ ░░   ░ ▒░
                                 ▒ ▒ ░░   ▒ ░   ░   ░ ░ 
                                 ░ ░      ░           ░ 
                                 ░ ░ 
                                 
                                 
                                       {Fore.WHITE}          Loading...
""")
print(Fore.MAGENTA)
progress = tqdm([2,4,6,8,10])
for item in progress:
    sleep(0.3)
    progress.set_description(' Loading: ')
os.system('cls||clear')
print(f"""
{Fore.MAGENTA}
                                ▓██   ██  ██  ███▄    █ 
                                 ▒██  ██  ██  ██ ▀█   █
                                  ▒██ ██  ██  ██  ▀█ ██▒
                                  ░ ▐██▓░░██░ ██▒  ▐███▒
                                  ░ ██▒▓░░██░▒██░    ██░
                                   ██▒▒▒ ░▓  ░ ▒░   ▒ ▒  
                                 ▓██░▒░  ▒ ░░ ░░   ░ ▒░
                                 ▒ ▒ ░░   ▒ ░   ░   ░ ░ 
                                 ░ ░      ░           ░ 
                                 ░ ░ 


                                    {Fore.WHITE}        User ID
""")
os.system("title yin")
id = input(Fore.MAGENTA+" root" + Fore.WHITE+"@" + Fore.MAGENTA +"yin" + Fore.WHITE+":" + Fore.CYAN+"~" + Fore.WHITE+" ")

try:
    check = int(id) #checking if its number
    print('')
    print(f'{Fore.MAGENTA} [{Fore.WHITE}+{Fore.MAGENTA}] Success!')
    data = f'{id}'
    encodedBytes = base64.b64encode(data.encode("utf-8"))#encoding to base64 
    encodedStr = str(encodedBytes, "utf-8")
    print('')
    print(f'{Fore.MAGENTA} [{Fore.WHITE}+{Fore.MAGENTA}] {encodedStr}')
    print('')
    pyperclip.copy(encodedStr)
    print(f'{Fore.MAGENTA} [{Fore.WHITE}+{Fore.MAGENTA}] Text Copied!')
    print('')
    print(f'{Fore.MAGENTA} [{Fore.WHITE}+{Fore.MAGENTA}] Press enter to Exit')
    input()
except ValueError:
    print('')
    print(f'{Fore.MAGENTA} [{Fore.WHITE}+{Fore.MAGENTA}] Invalid ID!')
    print('')
    print(f'{Fore.MAGENTA} [{Fore.WHITE}+{Fore.MAGENTA}] Press enter to Exit')
    input()
    
 #credits to the idea and design https://github.com/xKenyh/Discord-Token-Finder
 #discord id is half of the token encoded in base64
 #more of the token is timestamp at which token was generated 
 #last letters of the token are HMAC cryptographic component used for the actual authorization for discord 