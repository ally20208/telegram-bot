import os,time
file="/var/log/ipmi/idrac.log"
current=os.open(file,os.O_RDONLY)
tt=os.fstat(current).st_ino
a=os.stat(file).st_ino
print (current)
print tt
print (a)