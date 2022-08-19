import os,time
import telepot

def error_log(log):
        token = open('auth.txt','r').read().strip()
        receiver_id = open('chat_id.txt','r').read().strip()

        bot = telepot.Bot(token)
        keyword = ['iDRAC','Severity','Category','MessageID','Message:']
        temp = str(log).replace(',','')
        for i in keyword:
                text = temp
                index =temp.find(i)
                text = temp[:index] + '\n' + temp[index:]
                temp = text

        bot.sendMessage(receiver_id, text)



logpath = '/var/log/ipmi/idrac.log'
current = open(logpath, "r")
current.seek(0, os.SEEK_END)
cur_ino = os.fstat(current.fileno()).st_ino
while True:
    while True:
        where = current.tell()
        line = current.readline()
        if not line:
            time.sleep(1)
            current.seek(where)
        else:
            error_log(line)
        try:
            if os.stat(logpath).st_ino != cur_ino:
                new = open(logpath, "r")
                current.close()
                current = new
                cur_ino = os.fstat(current.fileno()).st_ino
            continue
        except:
            pass
        time.sleep(1)
