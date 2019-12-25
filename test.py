#coding:utf-8

from addr_phone_decrypt import get_decrypted_addr_phone
from comment_decrypt import  get_decrypted_comment

if __name__ == '__main__':
    shop_id = '125247315'
    get_decrypted_addr_phone(shop_id)
    get_decrypted_comment(shop_id)