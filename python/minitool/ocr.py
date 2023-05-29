import numpy as np
import pandas as pd
import csv
import os
from paddleocr import PaddleOCR
import re
os.chdir('D:\\研究生生活\\悲惨世界\\打工\\20230331\\1')
exl=[]
no_FP=[]
n=0
num=r'[\u4e00-\u9fa5]'
real=r'^\d{1,}(\.\d{1,2})?$|\d{4}-\d{2}-\d{2}|^\d{7,}'

pic_list = os.listdir('D:\\研究生生活\\悲惨世界\\打工\\20230331\\1')

ocr = PaddleOCR(use_angle_cls=False, lang="ch",use_gpu=True)

def write_txt(a):
    with open("1.txt",'w') as f:
        for a in exl:
            try :
                if a:
                    f.writelines(a+'\n')
            except :

                pass

def selsct_model(x):


    return x


def fil(txt):
    for s in txt:
        wash_txt=selsct_model(s)
        exl.append(wash_txt)
    


for pic in pic_list:
    result=ocr.ocr(pic,cls=False)
    All_text=[]
    P=[]
    for i in result:          ##########################每张图片
        # print(i)
        for a in i:
            print(a)
            All_text.append(a[1][0])
    n+=1
    print(All_text)
    fil(All_text)
    


write_txt(exl)
# pd.DataFrame(exl).to_csv('1.csv')
print("无效发票：{}张：\n".format(len(no_FP)))
for i in no_FP: 
    print("{}".format(i))
# os.chdir('C:\\Users\\LENOVO\\Desktop\\第二批')

# out = open('1.csv', 'w', newline='')  # 要转成的.csv文件，先创建一个LF1big.csv文件
# csv_writer = csv.writer(out, dialect='excel')

# f = open("白菜100.txt", "r")
# for line in f.readlines():
#     line = line.replace(',', '\t')  # 将每行的逗号替换成空格
#     list = line.split()  # 将字符串转为列表，从而可以按单元格写入csv
#     csv_writer.writerow(list)
