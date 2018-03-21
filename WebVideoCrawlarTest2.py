
# coding: utf-8

# In[ ]:


import BilibiliAid
import os
#import requests
#import math
#from bs4 import BeautifulSoup

import datetime
#import random
#from selenium import webdriver
import time

aidArrayTest = []
Tp = 1

aidArrayTest = BilibiliAid.aid_tget('10330740', Tp)

video_homepage = 'https://www.bilibili.com/video/av'
video_path = '.\\videos\\'

#print('the videos will be saved in the path: ' + 'videos\')

for aid in aidArrayTest:
    command = "lulu -o " + video_path + ' ' + video_homepage + aid
    print("downloading video number: " + str(aid))
    starttime = datetime.datetime.now()
    os.system(command)
    endtime = datetime.datetime.now()
    print('finished videos ' + str(aidArrayTest.index(aid)+1) + '/' + str(len(aidArrayTest)))
    print('time spent: ' + str((endtime - starttime).seconds))
print('done!')
#len(aidArrayTest)

