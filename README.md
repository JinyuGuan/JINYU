# Web Video Crawlar Testool
2018-3-20

This is a python program for studying how to realize a simple WebCrawler.
Notice that this program now only can be applied in testing and getting data though uppers' all video's aid from their homepage in bilibili.com.
Setting your path of chromedriver is a good start.

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
