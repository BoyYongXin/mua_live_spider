import sys
sys.path.append('../')
from utils import tools
import codecs
packets_file_path = 'E:\\www\\mua_live_spider\\test.pcap'

def read_data():
    try:
        datas = codecs.open('data.txt', 'r', encoding='utf-8')
        info = datas.readlines()[-1].strip()
        infos=info.split(',')
        return infos[-1]
    except Exception as err:
        print(err)
        return ''
while True:

    with open(packets_file_path, 'rb') as file:
        streams = file.read()
        # print(streams.decode('gbk', 'ignore'))

        tools.delay_time(2)
        stream_url = tools.get_info(streams.decode('gbk', 'ignore'), 'str_stream_url[a-z](.+?)\n',
                                    allow_repeat=False)
        try:
            print(len(stream_url))
            stream=stream_url[-1]

            url=read_data()
            if stream == url:
                print('数据相同无法存入')
            else:
                f = open('data.txt', 'a', encoding="utf-8")
                f.write(stream + "\n")
                f.close()
                print('已存入链接:  %s'%stream)
        except Exception as err:
            print(err)
            pass
    tools.delay_time(1)