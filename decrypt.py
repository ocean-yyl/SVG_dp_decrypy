# encoding=utf-8
"""
woff解密器
"""
from util import dec
from conf import decrypt_tags
from bs4.element import Tag

def decrypt_woff_tag(tag,TTGlyphs,d_list):
    contents = tag.contents
    _ = []
    # print(TTGlyphs)
    while contents:
        i = contents.pop(0)
        if isinstance(i, Tag):
            if i.name in decrypt_tags:
                text = dec(i.text)
                for index,name in enumerate(TTGlyphs):
                    if text in name:
                        # print("1:", text)
                        i = d_list[index]
                        break
            else:
                continue
        if not isinstance(i, str):
            continue
        _.append(i)
    return ''.join(_)
