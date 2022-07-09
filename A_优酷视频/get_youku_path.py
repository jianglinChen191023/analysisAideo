# coding=utf-8
import sys

reload( sys )
sys.setdefaultencoding( "utf-8" )
# 需要更改的参数
# 重生之门第一集: https://v.youku.com/v_show/id_XNTg2MTAyOTc5Mg==.html?spm=a2hbt.13141534.1_3.1&s=ffdb0f1420364ebf8c69

# 解析地址
analysis_path = 'https://jx.blbo.cc:4433/sb.php?v='
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
referer = 'https://v.youku.com/v_show/id_XNTg2MTAyOTgxMg==.html?spm=a2hbt.13141534.1_3.6&s=ffdb0f1420364ebf8c69'
headers = {
    'user-agent': user_agent,
    'referer': referer,
    'cookie': 'cna=/qyZGk+HEBsCAXjkaAGAbqWA; __ysuid=1650054257728UmL; __ayft=1657324321304; __aysid=1657324321317Hdb; __ayscnt=1; xlly_s=1; youku_history_word=%5B%22%25E9%2587%258D%25E7%2594%259F%25E4%25B9%258B%25E9%2597%25A8%22%2C%22%25E5%25AF%2592%25E6%25AD%25A6%25E7%25BA%25AA%22%2C%22%25E8%2591%25A3%25E5%25AD%2590%25E5%2581%25A5%22%2C%22%25E6%259E%2597%25E9%259B%25A8%25E7%2594%25B3%22%5D; __arycid=dd-3-00; __arcms=dd-3-00; P_F=1; redMarkRead=1; __arpvid=1657341336230P0MVms-1657341336370; __aypstp=12; __ayspstp=12; _m_h5_tk=02664612f0f0f7871e6188df5580daf2_1657345846995; _m_h5_tk_enc=4450f31067e46b23efa49cd9b484fc09; __ayvstp=31; __aysvstp=31; tfstk=cVlCBOGLp0hZ3k_wc7TwLdDOUlNFaafQ7eZiRhE7I92c_ioUXsVfgo_MG4jTazU1.; l=eBxaLKhmLhi71aEQBOfwourza77OSIRAguPzaNbMiOCPOS5k55DfW6A6tP8DC3GVh6VyR3P8n0-9BeYBcQOSnxv9R5IXSFDmn; isg=BAIC8_-v1BTusMhA-UZmAqb4Uw5k0wbtgcDv1kwbLnUgn6IZNGNW_YjfT5vjz36F'
}

# 1. 导入模块
import requests
from bs4 import BeautifulSoup

# 需要解析的视频地址
mp4_items = []

items = [
    {'number': '1',
     'path': 'https://v.youku.com/v_show/id_XNTg2MTAyOTc5Mg==.html?spm=a2hbt.13141534.1_3.1&s=ffdb0f1420364ebf8c69'}
]

# 循环操作
for item in items:
    # 2. 发送请求, 获取响应
    response = requests.get( item['path'], headers=headers )
    # print response.text
    # 3. 获取响应数据
    home_page = response.content.decode()
    # 4. 提取数据
    soup = BeautifulSoup( home_page, 'lxml' )
    tag = soup.find( attrs={'class': 'anthology-content'} )

    tagA = tag.findAll( 'a' )
    for t in tagA:
        attrs = t.attrs

        if t.text == '':
            mp4_items.append(
                {'number': '1', 'path': str( attrs['href'] )} )
        else:
            mp4_items.append(
                {'number': str( t.text ).replace( 'VIP', '' ), 'path': str( attrs['href'] )} )
#
print mp4_items
for item in mp4_items:
    print(item['number'].replace( 'VIP', '' ) + ' ' + item['path'])
