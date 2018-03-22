
# coding: utf-8

# In[9]:


#This script shows how to get bili video's statistic information by parsing json data from 
#http://api.bilibili.com/archive_stat/stat?aid=170001

import requests
import json

url = 'http://api.bilibili.com/archive_stat/stat?aid='
aid = '170001'

def GetJsonText(av):
    DOWNLOAD_URL = url + av
    data = requests.get(DOWNLOAD_URL)
    json_text = json.loads(data.text)
    return json_text

def GetReply(av):
    json_text = GetJsonText(av)
    return json_text['data']['reply']

def GetView(av):
    json_text = GetJsonText(av)
    return json_text['data']['view']

def GetDanmuku(av):
    json_text = GetJsonText(av)
    return json_text['data']['danmuku']

def GetFavorite(av):
    json_text = GetJsonText(av)
    return json_text['data']['favorite']

def GetCoin(av):
    json_text = GetJsonText(av)
    return json_text['data']['Coin']

#################################################
    

