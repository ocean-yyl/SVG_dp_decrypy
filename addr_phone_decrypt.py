# encoding=utf-8
"""地址和电话内容解密"""
from conf import *
from woffs import woffs
from WoffChooser import get_addr_num_woff_from_file, parse_and_handle_shop_page
from decrypt import decrypt_woff_tag
from bs4 import BeautifulSoup as bsoup


# 地址和电话内容解密
def get_decrypted_addr_phone(shop_id):
    test_html, svgtextcss = parse_and_handle_shop_page(shop_id)
    # 获取要解密的地址、电话 标签，这里是 标签<span id="address">...</span>以及标签<span class="info-name">...</span>,传进解密函数
    shop_page_soup = bsoup(test_html, 'lxml')
    address_tag = shop_page_soup(comment_tag_finder['url-a-address'][0], **comment_tag_finder['url-a-address'][1])[0]
    phone_tag = shop_page_soup(comment_tag_finder['url-a-phone'][0], **comment_tag_finder['url-a-phone'][1])[0]

    # 读取对应的已下载的woff文件，获取ttg
    TTGlyphs = get_addr_num_woff_from_file()

    d_address = decrypt_woff_tag(address_tag, TTGlyphs, woffs)
    d_phone = decrypt_woff_tag(phone_tag, TTGlyphs, woffs)

    return d_address, d_phone


if __name__ == '__main__':
    get_decrypted_addr_phone('102973511')
