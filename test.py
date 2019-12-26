# encoding=utf-8

from addr_phone_decrypt import get_decrypted_addr_phone
from comment_decrypt import  get_decrypted_comment

if __name__ == '__main__':
    shop_id = '125247315'
    addr,phone = get_decrypted_addr_phone(shop_id)
    comment = get_decrypted_comment(shop_id)
    print("地址：",addr)
    print("电话：",phone)
    print("评论1：",comment)