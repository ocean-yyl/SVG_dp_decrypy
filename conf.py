# encoding=utf-8
"""
配置文件
"""
from fake_useragent import UserAgent

schema = 'https://'
decrypt_tags = ['svgmtsi','d','e']

pattern_svgcss = r'//(s3plus.meituan.net.+?)"'
pattern_woff = r',url\("//(.+?\.woff)"'
pattern_address_woff = r'\.address.*url\("//(.+?\.woff)"'

example_shop_url = 'https://www.dianping.com/shop/{shop_id}'

comment_tag_finder = {
    'url-a':('ul',{'id':'reviewlist-wrapper'}),
    'url-a-li':('li',{'class_':'comment-item'}),
    'url-a-p':('p',{'class_':'desc J-desc'}),
    'url-a-address':('span',{'id':'address'}),
    'url-a-phone':('p',{'class_':'expand-info tel'})
}

ua = UserAgent()
request_headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Host':'www.dianping.com',
    'User-Agent':ua.random
}

if __name__ == '__main__':
    print(request_headers)