抓取mua主播直播信息说明：

文件说明：
    img   存取对主播直播间的某一状态进行截屏操作
    data   存取直播间主播信息和直播流信息进行存储
    log    日志存储
    utile   对一些工具的封装


驱动程序：
    （1）抓取直播流这里用的是wireshark,这里把他封装成bat文件

        /tsahrk启动/xxx.bat
    （2）mua_live_spider_end.py   开起appium操作手机app一系列操作，获取数据



    （3）zip_data_all_info1.py  对获取到的直播信息和直播流  进行对应整合，写入到data文件里


如果有问题，可以联系本人

1426866609@qq.com   qq同号