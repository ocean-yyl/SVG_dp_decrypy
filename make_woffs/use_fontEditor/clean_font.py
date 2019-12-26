# encoding=utf-8

with open("font.txt",encoding="utf-8") as f1:
    lines = f1.readlines()

# 只取基数行，识别的文字内容
with open("font2.txt","w",encoding="utf-8") as f2:
    for i in range(len(lines)):
        if i % 2 == 0:
            f2.write(lines[i])
        else:
            continue