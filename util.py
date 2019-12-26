# encoding=utf-8
"""
下载器和解析器
"""
import requests


# 文件下载url并保存
def download_and_save(url, save_path, mode='wb', **request_kwargs):
    with open(save_path, mode) as f:
        response = requests.get(url, **request_kwargs)
        content = response.content
        f.write(content)


# 异化字符转为编码
def dec(a):
    # print(a)  # a = '',''
    c = str(a.strip().encode('raw_unicode_escape').replace(b'\\u', b''), 'utf-8')
    # print(c)  # c = 'e892','f344'
    return c
