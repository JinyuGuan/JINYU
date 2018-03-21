
# coding: utf-8

#import os
import requests
import math
from bs4 import BeautifulSoup

import datetime
import random
from selenium import webdriver
import time

#upper_id = '10330740'
def aid_tget(upper_id, Tp):
    #aidArray is used to stroe aids
    #Tp = 2
    aidArray = []

    #you can download other upper's video by changing this parameter
    path = "./chromedriver.exe" #Get Chromedriver.exe path
    driver = webdriver.Chrome(executable_path=path) #Drive Chrome
    #print('stage 1: obtain aids')
    print('opening the chrmodriver...')


    for page in range(1, Tp + 1) : #
        page_video = 0 #video index in current page
        print('opening page: ' + str(page))
        url = "https://space.bilibili.com/" + upper_id + "?from=search&seid=12264074931239145067#/video?tid=0&page=" + str(page) + "&keyword=&order=pubdate"
        #The homepage link for one upper whose uid is 10330740
        driver.get(url)
        #Load the url
        time.sleep(5)
        #Delay 5s

        while True : #Check out HTML entire page source codes for each page
            pageSourceThree = driver.page_source
            PageSourceHtml = BeautifulSoup(pageSourceThree,"html.parser")
            PageSourceBodyHtml = PageSourceHtml.find('ul', attrs={'class': 'list-list'})
            #Find out the information of all videos under lable '<ul> class = 'list-list' 
            if(str(PageSourceBodyHtml) == 'None'): #If that information cannot be obtain, delay 0.5s, return back and do again.
                time.sleep(0.5)
            else:
                #If got that information, find all videos' detials under lable <li> class = 'list-item clearfix fakeDanmu-item'
                detial_old = PageSourceBodyHtml.findAll('li', attrs = {'class':'list-item clearfix fakeDanmu-item'})
                detial = PageSourceBodyHtml.findAll('li', attrs = {'class':'list-item clearfix fakeDanmu-item new'})
                #Add videos under lable <new>
                detial = detial + detial_old
                if(str(detial) != '[]'): #If the detial is not empty, break the loop and start next page's work.
                    break
                else: #If it is, sleep 0.5s
                    time.sleep(0.5)
        
        print('Finished Page:' + str(page))
    
        while True:
            try : #Find all aids from each page's HTML source codes
                aidStart = str(detial[page_video]).find('aid') + 5
                aidEnd = str(detial[page_video]).find('"><a') 
            
                #find the aid of this video
                aid = str(detial[page_video])[aidStart : aidEnd]
                aidArray.append(str(detial[page_video])[aidStart : aidEnd])
                #print('found video number: ' + aid)
                page_video = page_video + 1
                #time.sleep(0.5)
            except:
                #if all the video aids are already found, break and go to the next page
                break
    return aidArray

