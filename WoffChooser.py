# coding:utf-8
"""

"""
import re
import requests
from conf import *
from fontTools.ttLib import TTFont
from util import download_and_save


# 获取店铺页面源码
def parse_and_handle_shop_page(shop_id):
    shop_source_html = requests.get(example_shop_url.format(shop_id=shop_id), headers=request_headers)
    shop_html = shop_source_html.text
    # 获取svg 用 css 链接 以及 读取内容 以待获取woff字体下载链接
    svg_url = schema + re.findall(pattern_svgcss, shop_html)[0]
    svg = requests.get(svg_url)
    svgtextcss = svg.text
    return shop_html, svgtextcss


"""
电话地址 的解密woff文件 需要的url是第一个即：
woff_url = schema + re.findall(pattern_woff,svgtextcss)[0]
评论内容的解密woff文件 需要的url是第二个，即：
woff_url = schema + re.findall(pattern_woff,svgtextcss)[1]
"""
# 从网页下载woff文件
def download_woff(svg_css):
    # 存储字符编码
    TTGlyphs = []

    # 去重
    woff_urls = re.findall(pattern_woff, svg_css)
    woff_urls_set = set()
    for url in woff_urls:
        woff_urls_set.add(schema + url)
    # 下载所有的woff文件
    for url in woff_urls_set:
        filename = url.split("/")[-1]
        download_and_save(url, "woff/" + filename)
        # 4. 使用fontTools库解析woff字体文件，获取字体排序列表
        font = TTFont("woff/" + filename)
        # font.saveXML("xml/" + filename.split(".")[0] + ".xml")  # 存储为xml文件
        TTGlyphs.extend(font['cmap'].tables[0].ttFont.getGlyphOrder()[2:])
    return TTGlyphs


"""
有选择的读取woff文件，因为多个文件会有后四位编码重合的字，
所以必须分开读取，而不可以合并。
"""
# 找到仅仅对于地址和电话的woff解密文件
def get_addr_num_woff_from_file():
    TTGlyphs = []
    # 加载地址与电话解密对应的woff文件
    font = TTFont("woff/80eb581a.woff")
    TTGlyphs.extend(font['cmap'].tables[0].ttFont.getGlyphOrder()[2:])
    font = TTFont("woff/907ae099.woff")
    TTGlyphs.extend(font['cmap'].tables[0].ttFont.getGlyphOrder()[2:])
    return TTGlyphs


# 找到仅仅对于评论区的woff解密文件
def get_comment_woff_from_file():
    TTGlyphs = []
    font = TTFont("woff/bcd2a582.woff")  # 评论区解密对应的woff文件,非f3
    TTGlyphs.extend(font['cmap'].tables[0].ttFont.getGlyphOrder()[2:])
    font = TTFont("woff/d2c56b1a.woff")
    TTGlyphs.extend(font['cmap'].tables[0].ttFont.getGlyphOrder()[2:])
    return TTGlyphs


if __name__ == '__main__':
    shop_html, svgtextcss = parse_and_handle_shop_page('125247315')
    ttg = download_woff(svg_css=svgtextcss)
