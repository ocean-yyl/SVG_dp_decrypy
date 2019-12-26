# encoding=utf-8

with open("test_contour",encoding="utf-8") as f1:
    lines = f1.readlines()

# 只取x,y
with open("contour.txt","w",encoding="utf-8") as f2:
    for line in lines:
        parts = line.split('"')
        x = parts[1]
        y = parts[3]
        f2.write("({},{})\n".format(x,y))