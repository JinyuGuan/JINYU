
# coding: utf-8

# In[ ]:


import requests
import re
import os
import sys
import json
import time

aid_list = []

info_list = []
def getAVListPageInfo(mid):
    n = 10000
    url = "http://space.bilibili.com/ajax/member/getSubmitVideos?mid=" +         str(mid) + "&pagesize=30" + "&page=" + str(n)
        
    data = requests.get(url)
    json_text = json.loads(data.text)
    page = json_text["data"]["pages"]
    
    return int(page)

def getAVListCountInfo(mid):
    n = 10000
    url = "http://space.bilibili.com/ajax/member/getSubmitVideos?mid=" +         str(mid) + "&pagesize=30" + "&page=" + str(n)
        
    data = requests.get(url)
    json_text = json.loads(data.text)
    count = json_text["data"]["count"]
    return int(count)


def getAVJsonText(mid):
    n = 1
    json_text_page = []
    while True :
        url = "http://space.bilibili.com/ajax/member/getSubmitVideos?mid=" +             str(mid) + "&pagesize=100" + "&page=" + str(n)
            
        data = requests.get(url)
        json_text = json.loads(data.text)
        json_text_page.append(json_text)
        if(json_text["data"]["vlist"] == []):
            break
        else:
            n = n + 1
    
    return json_text_page

def getAllAVList(mid):
    json_text_page = getAVJsonText(mid)
    i = 0
    while True:
        try:
            for item in json_text_page[i]["data"]["vlist"]:
                aid_list.append(item["aid"])
            i = i + 1
        except:
            break
    return aid_list

#def getAVList(mid, size, page):
    
#    url = "http://space.bilibili.com/ajax/member/getSubmitVideos?mid=" + \
#        str(mid) + "&pagesize=" + str(size) + "&page=" + str(n)
            
#    data = requests.get(url)
#    json_text = json.loads(data.text)
    
#    item = json_text["data"]["vlist"]
#    aid = item[0]["aid"]
    
    #return aid_list

def getAllAVinfo(mid):
    json_text_page = getAVJsonText(mid)
    play = []
    comment = []
    created = []
    date = []
    video_review = []
    length = []
    favorites = []
    i = 0
    while True:
        try:
            for item in json_text_page[i]["data"]["vlist"]:
                play.append(item["play"])
                comment.append(item["comment"])
            
                #date_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(item["created"])))
                created.append(item["created"])
                #date.append(data_str)
            
                video_review.append(item["video_review"])
                length.append(item["length"])
                favorites.append(item["favorites"])
            i = i + 1
        except:
            break
            
    return play, comment, created, video_review, length, favorites
        
    
    
#Test Script
#aid_listTest = getAVJsonText('10330740')
#mid = '10330740'
#json_text_page = []
#json_text_page = getAVJsonText(mid)
#aid_list = getAllAVList(mid)
#out = getAllAVinfo(mid)
#print(len(aid_list))
#print(len(out[2]))

