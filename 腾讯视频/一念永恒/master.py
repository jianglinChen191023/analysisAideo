# coding=utf-8
import sys

# 需要更改的参数
# 一念永恒第一集: https://v.qq.com/x/cover/ww18u675tfmhas6/y0034p3yuwk.html
# 视频cid
data_cid = 'ww18u675tfmhas6'
data_vid = 'y0034p3yuwk.html'
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'

reload( sys )
sys.setdefaultencoding( "utf-8" )

# 1. 导入模块
import requests
from bs4 import BeautifulSoup

download_path = '${DOWNLOAD_PATH}/'
# 需要解析的视频地址
mp4_items = []

items = [
    {'number': '1', 'path': 'https://v.qq.com/x/cover/' + data_cid + '/' + data_vid}
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

        mp4_items.append( {'number': str( t.text ), 'path': 'https://v.qq.com/x/cover/yl6lapwmmx5ivew/' + attrs[
            'data-vid'] + '.html'} )

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

        response = requests.get( 'https://jx.blbo.cc:4433/analysis.php?v=' + item['path'], headers=headers )
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
