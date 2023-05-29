# import jieba
from wordcloud import WordCloud 
import matplotlib.pyplot as plt
import os
import jieba
import numpy as np
from PIL import Image


# photo=np.array(Image.open("C:\\Users\\LENOVO\\Desktop\\1.jpg"))
os.chdir("C:\\Users\\LENOVO\\Desktop")

txtls=os.listdir()

def save_pho(file_name,raw_txt):
    text=jieba.lcut(raw_txt)
    text=" ".join(text)
    wc=WordCloud(font_path='C:\\Windows\\Fonts\\simhei.ttf',
                background_color="white",
                # mask=photo,
                stopwords={"的","你","我","他","说","她","我们","是","了","在"}
                )

    wcphoto=wc.generate(text)
    plt.imshow(wcphoto,interpolation="bilinear")
    plt.axis("off")
    plt.savefig(file_name)






f=open("1.txt","r",encoding='utf-8')
text=f.read()
save_pho("C:\\Users\\LENOVO\\Desktop\\1.jpg",text)
f.close()













