import os
my_file = 'test.pcap'

if os.path.exists(my_file):
    # 删除文件，可使用以下两种方法。
    os.remove(my_file)
else:
    print('不存在test.pcap文件')

with open('data.txt','w') as file:
    file.seek(0)
    file.truncate()  # 清空文件
    print('已清空data.txt文件')
with open('room.txt','w') as file:
    file.seek(0)
    file.truncate()  # 清空文件
    print('已清空room.txt文件')

