import sys
import os
import re
from requests_html import HTMLSession
import random

pages = 0
print("Loaded Auto keys.lol ethereum CMD VERSION 1.4")
# threadCount = input('How many threads to run: ')
print("Started search...")


def run():
    try:
        while 5 > 1:
            #webUrl = urllib.request.urlopen('https://keys.lol/ethereum/1')
            pageNum = random.randrange(1,904625697166532776746648320380374280100293470930272690489102837043110636675)
            fullurl = 'https://keys.lol/ethereum/'+str(pageNum)
            session = HTMLSession()
            webUrl = session.get(fullurl)
            #time.sleep(10)
            webUrl.html.render()
            #html = webUrl.content
            data = webUrl.html.html
            result = re.findall("[+-]?\d+\.\d+", str(data))
            for i in result:
                if str(i) + " eth" in str(data):
                    if float(i) > 0:
                        with open('ValidWalletsETH.txt', 'a') as appendFile:
                            appendFile.write('{} eth\n'.format(str(i)))
                            appendFile.write('{}\n'.format(fullurl))
            global pages
            pages = pages + 1
            sys.stdout.write("\rPages read: {}".format(str(pages)))
            sys.stdout.flush()
            session.close()
            webUrl.close()
    except:
        run()


# for i in range(int(threadCount)):
#     thread = threading.Thread(target=run)
#     thread.start()
run()