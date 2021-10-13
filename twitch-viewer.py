from selenium import webdriver
import threading
import time
from multiprocessing import Pool
chrome_options = webdriver.ChromeOptions()



##chrome_options.add_argument("start-maximized")
##chrome_options.add_argument("disable-infobars")
##chrome_options.add_argument("--disable-extensions")
##chrome_options.add_argument('--no-sandbox')
##chrome_options.add_argument('--disable-application-cache')
##chrome_options.add_argument('--disable-gpu')
##chrome_options.add_argument("--disable-dev-shm-usage")
##chrome_options.add_argument("--headless")


##username=str(input('pls enter correct user name '))
##np=int(input('pls eneter number of bots,considering your ram '))
##
PROXY=''


proxyListFromFile=[]

f=open('proxy.txt','r')

line=f.readlines()

for i in line:
    proxyListFromFile.append(i.replace('\n',''))



    
def proxySurfing(url,PROXY):
    
    global chrome_options


    chrome_options.add_argument('--proxy-server=%s' % PROXY)
    chrome = webdriver.Chrome(options=chrome_options)

    chrome.get(url)
    while True:
        time.sleep(10)
        chrome.refresh()


def multip():
    global np
    global proxyListFromFile,url
 
    pool = Pool(processes=np)
    for i in range(np):  
        pool.apply_async(proxySurfing, args={url,proxyListFromFile[i]})
        print(proxyListFromFile[i])
    pool.close()
    pool.join()
##

if __name__ == "__main__":
    username=str(input('pls enter correct user name '))
    url = 'https://www.twitch.tv/'+str(username)
    np=int(input('pls eneter number of bots,considering your ram '))
    multip()

  

print ('Test completed!')
##time.sleep(50)
