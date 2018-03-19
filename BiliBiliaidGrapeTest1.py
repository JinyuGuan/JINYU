
# coding: utf-8

# In[79]:


import requests
import math
from bs4 import BeautifulSoup

import csv
import random
from selenium import webdriver
import time

Tp = 59 #The total page number
i = 2 #The start page number
aidArray = [0 for x in range(2000)] #Define an array for storing aids

path = "C:/Users/guanj/Documents/PythonEx/chromedriver_win32/chromedriver.exe" #Get Chromedriver.exe path
driver = webdriver.Chrome(executable_path=path) #Drive Chrome

while i < Tp + 1 : #
    j = 0
    s = str(i) # The current page
    
    url = "https://space.bilibili.com/10330740?from=search&seid=12264074931239145067#/video?tid=0&page=" + s + "&keyword=&order=pubdate"
    #The homepage link for one upper whose uid is 10330740
    driver.get(url)
    #Load the url
    time.sleep(5)
    #Delay 5s

    while 1 : #Check out HTML entire page source codes for each page
        pageSourceThree = driver.page_source
        PageSourceHtml = BeautifulSoup(pageSourceThree,"html.parser")
        PageSourceBodyHtml = PageSourceHtml.find('ul', attrs={'class': 'list-list'})
        #Find out the information of all videos under lable '<ul> class = 'list-list' 
        if(str(PageSourceBodyHtml) == 'None'): #If that information cannot be obtain, delay 5s, return back and do again.
            time.sleep(5)
        else:
            detial = PageSourceBodyHtml.findAll('li', attrs = {'class':'list-item clearfix fakeDanmu-item'})
            #If got that information, find all videos' detials under lable <li> class = 'list-item clearfix fakeDanmu-item'
            if(str(detial) != '[]'): #If the detial is not empty, break the loop and start next page's work.
                break
            else: #If it is, sleep 5s
                time.sleep(5)

    i = i + 1 #The current page number plus one.
    
    while j < 30 : #Find all 30 aids from each page's HTML source codes
        aidStart = str(detial[j]).find('aid') + 5
        aidEnd = str(detial[j]).find('"><a')
        aid = ''
        index = 0
        while index < (aidEnd - aidStart):
            aid = aid + str(detial[j])[aidStart + index]
            index += 1
        
        aidArray[j+30*(i-3)] = int(aid)
        j = j + 1
    
    time.sleep(random.randrange(9))
#######################################################################

#Get Reply Number
#Create CSV file first
csvFile = open("C:/Users/guanj/Documents/PythonEx/testnetg.csv",'w+', newline = "")
writer = csv.writer(csvFile)

def REPLYG(str):
    DOWNLOAD_URL = 'http://api.bilibili.com/archive_stat/stat?aid=' + str
    data = requests.get(DOWNLOAD_URL).content
    soup = BeautifulSoup(data, "html.parser", from_encoding='utf-8')
    text = soup.get_text()
    num_r = text.find('reply')
    num_f = text.find(',"favorite"')
    index = 0
    replyc = ''
    while index < (num_f - (num_r + 7)) :
        replyc = replyc + text[num_r + 7 + index]
        index += 1
    
    return replyc

i = 0
while i < (Tp - 1)*30 :
    s = str(aidArray[i])
    r = REPLYG(s)
    writer.writerow([aidAray[i], int(r)])
    i = i + 1

