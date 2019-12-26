# encoding=utf-8
"""评论内容解密"""
from conf import *
from woffs import woffs
from WoffChooser import get_comment_woff_from_file, parse_and_handle_shop_page
from decrypt import decrypt_woff_tag
from bs4 import BeautifulSoup as bsoup

# 评论内容解密
def get_decrypted_comment(shop_id):
    test_html, svgtextcss = parse_and_handle_shop_page(shop_id)
    # 获取要解密的评论标签，这里是 标签<p></p>,传进解密函数
    shop_page_soup = bsoup(test_html, 'lxml')
    comment_list_ul_tag = shop_page_soup(comment_tag_finder['url-a'][0], **comment_tag_finder['url-a'][1])[0]
    comment_list_li_tags = comment_list_ul_tag(comment_tag_finder['url-a-li'][0], **comment_tag_finder['url-a-li'][1])

    # 取当前页面的第一个评论作为示例
    example_comment_li_tag = comment_list_li_tags[0]
    comment_p = example_comment_li_tag(comment_tag_finder['url-a-p'][0], **comment_tag_finder['url-a-p'][1])[0]

    # 读取对应的已下载的woff文件，获取ttg
    TTGlyphs = get_comment_woff_from_file()

    comment = decrypt_woff_tag(comment_p, TTGlyphs, woffs)
    return comment


if __name__ == '__main__':
    get_decrypted_comment('102973511')
