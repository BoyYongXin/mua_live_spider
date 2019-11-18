import sys
import time
sys.path.append('../')
# from utils import tools
import codecs
while True:
    #mua
    with open(r'\\192.168.90.246\\shareInfo\data\\all_info.txt', 'w') as file:
    #布小星
    #with open(r'\\192.168.90.246\\shareInfo\data\\all_info1.txt', 'w') as file:
        file.seek(0)
        file.truncate()  # 清空文件
        print('已清空all_info.txt文件')
    urls = codecs.open('data.txt', 'r', encoding='utf-8')
    rooms = codecs.open('room.txt', 'r', encoding='utf-8')
    url_list = urls.readlines()
    room_list = rooms.readlines()
    for room,url in zip(room_list,url_list):
        data=room.strip()+","+url.strip()
        print(data)
        #mua直播
        f = open(r'\\192.168.90.246\\shareInfo\data\\all_info.txt', 'a', encoding="utf-8")
        #布小星
        # f = open(r'\\192.168.90.246\\shareInfo\data\\all_info1.txt', 'a', encoding="utf-8")
        # f.seek(0)
        # f.truncate()  # 清空文件
        f.write(data + "\n")
        f.close()
    print('程序正在睡眠，1分钟后再次启动')
    time.sleep(60*1)
    # print('程序正在睡眠，5分钟后再次启动')