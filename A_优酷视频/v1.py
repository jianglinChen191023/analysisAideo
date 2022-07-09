# coding=utf-8
import sys

reload( sys )
sys.setdefaultencoding( "utf-8" )
# 1. 导入模块
import requests
from bs4 import BeautifulSoup
analysis_path='https://jx.blbo.cc:4433/1.php?v='
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'

download_path = '${DOWNLOAD_PATH}/'
# 需要解析的视频地址
mp4_items = [{'path': 'https://v.youku.com/v_show/id_XNTg2MTAyOTc5Mg==.html?s=ffdb0f1420364ebf8c69', 'number': '1'},
             {'path': 'https://v.youku.com/v_show/id_XNTg2MTAyOTgwMA==.html?s=ffdb0f1420364ebf8c69', 'number': '2'},
             {'path': 'https://v.youku.com/v_show/id_XNTg2MTAyOTc5Ng==.html?s=ffdb0f1420364ebf8c69', 'number': '3'},
             {'path': 'https://v.youku.com/v_show/id_XNTg2MTAyOTgwOA==.html?s=ffdb0f1420364ebf8c69', 'number': '4'},
             {'path': 'https://v.youku.com/v_show/id_XNTg2MTAyOTgwNA==.html?s=ffdb0f1420364ebf8c69', 'number': '5'},
             {'path': 'https://v.youku.com/v_show/id_XNTg2MTAyOTgxMg==.html?s=ffdb0f1420364ebf8c69', 'number': '6'},
             {'path': 'https://v.youku.com/v_show/id_XNTg2MTAyOTgxNg==.html?s=ffdb0f1420364ebf8c69', 'number': '7'},
             {'path': 'https://v.youku.com/v_show/id_XNTg2MTAyOTgyMA==.html?s=ffdb0f1420364ebf8c69', 'number': '8'},
             {'path': 'https://v.youku.com/v_show/id_XNTg2MTAyOTgyNA==.html?s=ffdb0f1420364ebf8c69', 'number': '9'},
             {'path': 'https://v.youku.com/v_show/id_XNTg2MTAyOTgyOA==.html?s=ffdb0f1420364ebf8c69', 'number': '10'},
             {'path': 'https://v.youku.com/v_show/id_XNTg2MTYwMjgzNg==.html?s=ffdb0f1420364ebf8c69', 'number': '11'},
             {'path': 'https://v.youku.com/v_show/id_XNTg2MDk5MjE0NA==.html?s=ffdb0f1420364ebf8c69', 'number': '12'},
             {'path': 'https://v.youku.com/v_show/id_XNTg2MTYwMjg0MA==.html?s=ffdb0f1420364ebf8c69', 'number': '13'},
             {'path': 'https://v.youku.com/v_show/id_XNTg2MTYwNDMxMg==.html?s=ffdb0f1420364ebf8c69', 'number': '14'},
             {'path': 'https://v.youku.com/v_show/id_XNTg2MDk5MjE1Mg==.html?s=ffdb0f1420364ebf8c69', 'number': '15'},
             {'path': 'https://v.youku.com/v_show/id_XNTg2MDk5MjE0OA==.html?s=ffdb0f1420364ebf8c69', 'number': '16'},
             {'path': 'https://v.youku.com/v_show/id_XNTg2MTYwNDMxNg==.html?s=ffdb0f1420364ebf8c69', 'number': '17'},
             {'path': 'https://v.youku.com/v_show/id_XNTg2MTYwNDMyMA==.html?s=ffdb0f1420364ebf8c69', 'number': '18'},
             {'path': 'https://v.youku.com/v_show/id_XNTg2MTYwNDMyNA==.html?s=ffdb0f1420364ebf8c69', 'number': '19'},
             {'path': 'https://v.youku.com/v_show/id_XNTg2MTYwMjg0NA==.html?s=ffdb0f1420364ebf8c69', 'number': '20'},
             {'path': 'https://v.youku.com/v_show/id_XNTg2MTY0NDgzNg==.html?s=ffdb0f1420364ebf8c69', 'number': '21'},
             {'path': 'https://v.youku.com/v_show/id_XNTg2MTY0NDgzMg==.html?s=ffdb0f1420364ebf8c69', 'number': '22'},
             {'path': 'https://v.youku.com/v_show/id_XNTg2MTY0NDg0MA==.html?s=ffdb0f1420364ebf8c69', 'number': '23'},
             {'path': 'https://v.youku.com/v_show/id_XNTg2MTY0Mzc0OA==.html?s=ffdb0f1420364ebf8c69', 'number': '24'},
             {'path': 'https://v.youku.com/v_show/id_XNTg2MTY0Mzc1Ng==.html?s=ffdb0f1420364ebf8c69', 'number': '25'},
             {'path': 'https://v.youku.com/v_show/id_XNTg2MTY0Mzc1Mg==.html?s=ffdb0f1420364ebf8c69', 'number': '26'}]

# 循环操作
for item in mp4_items:
    try:
        # 2. 发送请求, 获取响应
        headers = {
            'user_agent': user_agent
        }

        response = requests.get( analysis_path + item['path'], headers=headers )
        # 3. 获取响应数据
        home_page = response.content.decode()
        # 4. 提取数据
        soup = BeautifulSoup( home_page, 'lxml' )

        script = soup.find( id='video' )
        attrs = script.attrs
        # 搭配 shell.sh 文件使用
        print('wget -U \'' + user_agent + '\' --limit-rate=1m -b -t 0 -o wget-log.' + item['number'] + ' -c ' + attrs[
            'src'] + ' -O ' + download_path + item['number'] + '.mp4')
    except:
        mp4_items.append( {'number': item['number'], 'path': item['path']} )

# 批量杀死进程
# ps -ef | grep wget | grep -v grep | awk '{print $2}' | xargs kill -9
