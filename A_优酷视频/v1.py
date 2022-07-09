# coding=utf-8
import sys

# 需要更改的参数
# 重生之门第一集: https://v.youku.com/v_show/id_XNTg2MTAyOTc5Mg==.html?spm=a2hbt.13141534.1_3.1&s=ffdb0f1420364ebf8c69
# 视频cid
data_cid = 'mzc00200moikwsy'
data_vid = 'k0042hf004f'
data_vid_params = '.html?ptag=iqiyi'

#解析地址
analysis_path='https://jx.blbo.cc:4433/sb.php?v='
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'

reload( sys )
sys.setdefaultencoding( "utf-8" )

# 1. 导入模块
# pip install requests
# pip install bs4
# pip install lxml
import requests
from bs4 import BeautifulSoup

download_path = '${DOWNLOAD_PATH}/'
# 需要解析的视频地址
mp4_items = []

items = [
    {'number': '1', 'path': 'https://v.qq.com/x/cover/' + data_cid + '/' + data_vid + data_vid_params}
]

# 循环操作
for item in items:
    # 2. 发送请求, 获取响应
    response = requests.get( item['path'] )
    # 3. 获取响应数据
    home_page = response.content.decode()
    # 4. 提取数据
    soup = BeautifulSoup( home_page, 'lxml' )
    # tag = soup.findAll( attrs={'data-cid': 'yl6lapwmmx5ivew'}, limit='3')
    tag = soup.findAll( attrs={'data-cid': data_cid, 'class': 'episode-item-rect'} )
    # print (tag)

    for t in tag:
        attrs = t.attrs
        # 获取集数
        # print(t.text + '集: https://v.qq.com/x/cover/yl6lapwmmx5ivew/' + attrs['data-vid'])

        # print("{'number': '" + t.text + "', 'path': 'https://v.qq.com/x/cover/yl6lapwmmx5ivew/" + attrs[
        #     'data-vid'] + ".html'},")

        mp4_items.append(
            {'number': str( t.text ), 'path': 'https://v.qq.com/x/cover/' + data_cid + '/' + attrs[
                'data-vid'] + data_vid_params} )

for item in mp4_items:
    print(item['number'] + ' ' + item['path'])
# 循环操作
for item in mp4_items:
    numbers = [
    ]

    is_number = 'false'
    for number in numbers:
        if number == item['number']:
            is_number = 'true'
            break

    if is_number == 'true':
        continue
    try:
        # 2. 发送请求, 获取响应
        # time.sleep( 1 )
        headers = {
            'User-Agent': user_agent
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
