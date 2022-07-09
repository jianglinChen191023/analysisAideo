# coding=utf-8
import sys

# 需要更改的参数
# 重生之门第一集: https://v.youku.com/v_show/id_XNTg2MTAyOTc5Mg==.html?spm=a2hbt.13141534.1_3.1&s=ffdb0f1420364ebf8c69

# 防盗链
referer = 'https://m3u8.okjx.cc:3389/13jx.php?url=https://v.youku.com/v_show/id_XNTg2MTAyOTgxNg==.html?s=ffdb0f1420364ebf8c69'
#
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'

reload( sys )
sys.setdefaultencoding( "utf-8" )

# 1. 导入模块
import requests
from bs4 import BeautifulSoup

# 2. 发送请求, 获取响应
headers = {
    'User-Agent': user_agent,
    'referer': referer
}

response = requests.get( 'https://m3u8.okjx.cc:3389/m13.php?url=https://v.youku.com/v_show/id_XNTg2MTAyOTgxNg==.html?s=ffdb0f1420364ebf8c69', headers=headers )
# 3. 获取响应数据
home_page = response.content.decode()
# 4. 提取数据
soup = BeautifulSoup( home_page, 'lxml' )

# script = soup.find( id='video' )
# attrs = script.attrs
# 搭配 shell.sh 文件使用
print(soup)

# 批量杀死进程
# ps -ef | grep wget | grep -v grep | awk '{print $2}' | xargs kill -9
