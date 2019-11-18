# !-*-coding:utf-8-*-
import cx_Oracle
import codecs
import os
import sys
sys.path.append('../')
from utils import tools
import codecs
# os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
# ip = "192.168.80.30"
# port = 1521
# db = 'orcl'
# user_name = 'ipos_user'
# user_pass = 'speech'

with open('data/all_info.txt', 'w') as file:
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
    '''
    将数据压缩到txt文本中
    '''
    # f = open('data/all_info.txt', 'a', encoding="utf-8")
    # # f.seek(0)
    # # f.truncate()  # 清空文件
    # f.write(data + "\n")
    # f.close()
# def info_main():
#     conn = cx_Oracle.connect(user_name, user_pass, '%s:%d/%s' % (ip, port, db))
#     cr = conn.cursor()
#     data = codecs.open('test.txt', 'r', encoding='utf-8')
#     for index, info in enumerate(data.readlines()):
#         try:
#             if info:
#                 title = info.strip().encode('utf-8')
#                 id = 210348 + index
#                 # insert_sql = "insert into TAB_IOPM_SITE (id，name,POSITION ,classify) values(%s，'%s',%s,%s)" % (id,title,1,2)
#                 insert_sql = "insert into TAB_IPOS_SITE  (id，name,POSITION ,classify) values({},'{}',{},{})".format(
#                     id, title.decode('utf-8'), 1, 2)
#                 print(insert_sql)
#                 cr.execute(insert_sql)
#                 cr.close()
#                 conn.commit()
#         except Exception as err:
#             # print(err)
#             raise err
