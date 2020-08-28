import urllib.request as ur
import re
from time import sleep
import datetime as dt
import socket as so

from  bs4 import BeautifulSoup as bs
arr= ["https://m.avito.ru/moskva/Var?ARGS", #Here is the e.g. site and it's search options Var?ARGS
      #"https://youla.ru/all/Var?ARGS",
      "https://www.cian.ru/Var?ARGS"]
roy = []
count_cy = 0;
counter =0
reuse = 0
path= 'bd.txt'
fil = open(path, 'a')

serv = "1.1.1.1"
def is_connected(hostname):
    try:
        host = so.gethostbyname(hostname)
        s = so.create_connection((host, 80), 2)
        s.close()
        return True
    except:
        pass
    return False

for i in open(path):
    roy.append(i)
#roy and file is done

while(True):
    ae=[]
    mas = []
    itef=0
    while(itef <len(arr)):
        if(is_connected(serv)):
            h= ur.urlopen(arr[itef])
            sp = bs(h, 'html.parser')
            for j in sp.find_all('a'):
                ae.append(re.search(r'(https://www.site.com?[0-9]*)|(.*/moskva/.*)',
                                    re.sub(r'/moskva/', 'https://site.com/moskva/',
                                           (re.sub(r'/moskva/Var', 'https://m.avito.ru/moskva',
                                                   str(j.get('href')))))))
            itef+=1
        else:
            print("Internet was broken.")
            sleep(30)
            print("Trying to recover connection after 30 sec..")
    ae = list(filter(None, ae))
    for l in ae:
        mas.append(l[0])
    if (count_cy != 0):
        for sor in mas:#mas is ready
            if not any(sor in o for o in roy):
                if (reuse == 0): print(str(dt.datetime.now().isoformat())+"\n\n_________\n___NEW___\n")
                print ("["+str(counter)+"]", sor)
                roy.append(sor)
                fil.write(t+"\n")
                reuse = 1;
                counter+=1
        if (reuse == 1):
            fil.close()
            print("_________")
            reuse = 0
        print("_______________"+str(dt.datetime.now().isoformat())+"_______________")

    else:#first one
        y=0
        #for u in mas:
        #    print("["+str(y)+"] "+u)
        #    y+=1
        #roy = mas;
        for t in mas:
            if not any(t in o for o in roy):
                fil.write(t+"\n")
                roy.append(t)
        fil.close()
        for q in open(path):
            print("["+str(y)+"] "+q)
            y+=1

        print("_______________\n\n")

    sleep(600)
    count_cy+=1