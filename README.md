# Web Video Crawlar Testool
2018-3-20

This is a python program for studying how to realize a simple WebCrawler.
Notice that this program now only can be applied in testing and getting data though uppers' all video's aid from their homepage in bilibili.com.
Setting your path of chromedriver is a good start.

2018-3-24
The most recent eidtion of script of capturing upper's videos' information is BiliBiliAVListInfo.py. If you are going to using that script, the content below starting from 'Installation' can be igored. Please read very carefully following explanation about BiliBiliAVListInfo.py.

## BiliBiliAVListInfo.py

This script includes several functions to obtain all videos' information for a certain upper of bilibili.com. Before using it, you must have the upper's uid. Remember that, and all following functions' input is uid.

**getAVListPageInfo(uid)
**getAVListCountInfo(uid)
**getAVJsonText(uid)

This three functions are internally private function, so you don't have to call them in your script.

**getALLAVList(uid)

The return value is a list of all videos' aid. You can capture other information by entering api of each video or you can call following function.

**getAllAVInfo(uid)

## Installation
### Prerequisites

The following dependencies are required.

* **[Python 3.0+](https://www.python.org/downloads/)** **( [Anaconda](https://www.anaconda.com/download/) is strongly recommended)**
* **[Lulu](https://github.com/iawia002/Lulu)**
* **[selenium](https://www.seleniumhq.org/)**

### Denpendencies Installation via pip

    $ pip install lulu
    
    $ pip install selenium
    
upgrade:
    
    $ pip install -U lulu


## BiliBiliAid.py
BiliBiliAid.py includes a funciton called aid_getfuid(uid, Tp).
Here, uid is one special code for each upper on bilibili.com.
Tp is the total page number of html source codes that you prepere to parse.

Recently, more functions using aid-get will be added in BilibiliAid.py.

## BiliGetStat.py
This script shows how to get bili video's statistic information by parsing json objects of api of bilibili.com.

* [Stat av170001](http://api.bilibili.com/archive_stat/stat?aid=170001)


