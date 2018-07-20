#!/usr/bin/python

import sys
import random
import time
import os
import datetime

# time defined to change IP (reconnect), default 30 minutes
seconds = 30*60

if len(sys.argv) >= 2:
    seconds = int(sys.argv[1])*60

# minimum time to reconnect, 2 minutes
if seconds < 120:
    seconds = 120

# list to get server name and id
lines = tuple(open('expressvpn-americas-list.txt', 'r'))
servers = []
for i in range(len(lines)):
    servers.append(lines[i].rstrip().split("\t"))

# var num used for log count, how many times the IP changed
num = 1
while 1:
  i = random.randint(0,len(servers) - 1)
  exp = "expressvpn connect "+servers[i][0]
  os.system("expressvpn disconnect")
  os.system(exp)
  dateTime = datetime.datetime.now()
  date = dateTime.strftime("%d/%m/%Y")
  hours = dateTime.strftime("%H:%M:%S")
  logexpr = "externalIP=$(curl ipecho.net/plain | tee /dev/tty) > /dev/null; echo \""+str(num)+";"+"$externalIP"+";"+date+";"+hours+";"+servers[i][0]+";"+servers[i][1]+"\" >> LOG.log"
  os.system(logexpr);
  time.sleep(seconds)
  num = num + 1
