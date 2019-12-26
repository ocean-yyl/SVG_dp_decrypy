# encoding=utf-8
"""
字典

# 制作出解密用对应字体库，具体有两个思路：
# 0x01:
#       a. 可以使用百度FontEditor查看woff字体文件内容，链接：http://fontstore.baidu.com/static/editor/index.html
#       b. 而后预览，后截图，使用腾讯文字识别上传截图识别出所有文字,制作字体库woffs。详细看woffs.py
# 0x02：
#       a. 第四步的 font_a.saveXML(woff_xml_path) 将woff字体文件转为xml文件
#       b. 将字体xml文件中<glyf></glyf>标签中的所有<TTGlyph>标签内的name属性以及字体信息坐标获取出来，使用Matplotlib等绘图工具，根据坐标将字形轮廓绘画出来
#       c. 将绘画结果字形图片利用腾讯文字识别api进行识别，存储对应{name:文字}字典
"""

woff_string = '''
1234567890店中美家馆
小车大市公酒行国品发电金心业商司
超生装园场食有新限天面工服海华水
房饰城乐汽香部利子老艺花专东肉菜
学福饭人百餐茶务通味所山区门药银
农龙停尚安广鑫一容动南具源兴鲜记
时机烤文康信果阳理锅宝达地儿衣特
产西批坊州牛佳化五米修爱北养卖建
材三会鸡室红站德王光名丽油院堂烧
江社合星货型村自科快便日民营和活
童明器烟育宾精屋经居庄石顺林尔县
手厅销用好客火雅盛体旅之鞋辣作粉
包楼校鱼平彩上吧保永万物教吃设医
正造丰健点汤网庆技斯洗料配汇木缘
加麻联卫川泰色世方寓风幼羊烫来高
厂兰阿贝皮全女拉成云维贸道术运都
口博河瑞宏京际路祥青镇厨培力惠连
马鸿钢训影甲助窗布富牌头四多妆吉
苑沙恒隆春干饼氏里二管诚制售嘉长
轩杂副清计黄讯太鸭号街交与叉附近
层旁对巷栋环省桥湖段乡厦府铺内侧
元购前幢滨处向座下臬凤港开关景泉
塘放昌线湾政步宁解白田町溪十八古
双胜本单同九迎第台玉锦底后七斜期
武岭松角纪朝峰六振珠局岗洲横边济
井办汉代临弄团外塔杨铁浦字年岛陵
原梅进荣友虹央桂沿事津凯莲丁秀柳
集紫旗张谷的是不了很还个也这我就
在以可到错没去过感次要比觉看得说
常真们但最喜哈么别位能较境非为欢
然他挺着价那意种想出员两推做排实
分间甜度起满给热完格荐喝等其再几
只现朋候样直而买于般豆量选奶打每
评少算又因情找些份置适什蛋师气你
姐棒试总定啊足级整带虾如态且尝主
话强当更板知己无酸让入啦式笑赞片
酱差像提队走嫩才刚午接重串回晚微
周值费性桌拍跟块调糕'''

woffs = [i for i in woff_string*3 if i!='\n' and i!=' ']

if __name__ == '__main__':
    print(woffs)