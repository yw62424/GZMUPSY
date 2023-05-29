import requests
import re
import os
import json
os.chdir("C:\\Users\\LENOVO\\Desktop")
requests.packages.urllib3.disable_warnings()
headers={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
    'authority': 'image.so.com',
    # 'authority': 'cn.bing.com',
    # 'x-client-data': 'eyI0IjoiNDM0ODA1NDgxNzM0NjcyNDkzOSIsIjUiOiJcImltTko3WlZ3Ryt2dHc2RU1wMDgyMk5zUUpmQ0JPVE5SWTJrV2lGM2VEeEE9XCIiLCI2Ijoic3RhYmxlIiwiNyI6IjM5MDg0MjAyMzk0NCJ9',
    'cookie': 'MMCA=ID=D6EDC03C2A7F453FB98D41F3E81E84F4; SRCHD=AF=NOFORM; SRCHUID=V=2&GUID=8A6BD79A4F8141579D27E16C10F58D36&dmnchg=1; MUID=15CE56E95C1E61B52D5859525D3060CF; MUIDB=15CE56E95C1E61B52D5859525D3060CF; _tarLang=default=en; _TTSS_OUT=hist=WyJlbiJd; _TTSS_IN=hist=WyJmciIsInpoLUhhbnMiLCJhdXRvLWRldGVjdCJd; SRCHS=PC=U531; ABDEF=V=13&ABDV=11&MRNB=1616309464827&MRB=0; SNRHOP=I=&TS=; SRCHUSR=DOB=20210110&T=1616320815000; ipv6=hit=1616324416484&t=4; _EDGE_S=SID=06BF3BD87E7968733E6C2BD97F576985&mkt=zh-cn&ui=zh-cn; _SS=PC=U531&SID=1E02E52B90E664291092F52A91C8653B&bIm=40:; SRCHHPGUSR=BZA=0&BRW=XW&BRH=M&CW=1536&CH=792&DPR=1.25&UTC=480&DM=0&HV=1616321819&WTS=63751917615&PLTL=642&PLTA=812&PLTN=47&SRCHLANGV2=zh-Hans&EXLTT=31'
            }
download_n=200
sn=130
ps=pc='50'
imgurl=[]
pic_n=0
url='https://image.so.com/j?q=qq&src=hao_360so&sn='+str(sn)+'&ps='+ps+'&pc='+pc
# q

def get_imgurl(name):
    global ps,pc,sn,pic_n
    url='https://image.so.com/j?q='+name+'&src=hao_360so&sn='+str(sn)+'&ps='+ps+'&pc='+pc
    r= requests.get(url,headers=headers,verify=False)
    html_json=r.content.decode("utf-8")
    with open("1.txt","w",encoding='utf-8') as t:
        t.write(html_json) 
    jd=json.loads(html_json)
    ##print(jd)
    list=jd["list"]
    pc=str(jd['pc'])
    ps=str(jd['ps'])
    pic_n=len(list)+pic_n
    print("共采集：{}张,pc:{},ps:{},sn:{}".format(pic_n,pc,ps,sn))
    sn+=50
    if len(list)==0 :
        print(imgurl)
        return imgurl
    for j in list:
        imgurl.append(j["img"])
        if len(imgurl)>download_n :
            print(imgurl)
            return imgurl
    return get_imgurl(name)

def save_img(pic_name):
    img_url=get_imgurl(pic_name)
    x=0
    print(img_url)
    for url in img_url:
        try:
            r= requests.get(url,headers=headers,timeout=5)
            t=r.content
            x+=1
            pic= open("picture/"+pic_name+"/"+str(x)+'.jpg', "wb")
            pic.write(t)
            pic.close()
            print("success download "+str(x)+" pictures")
        except requests.exceptions.ConnectionError:
            print("net error")
        except requests.exceptions.HTTPError:
            print("HTTPError！")
        except requests.exceptions.ReadTimeout:
            print("请求超时！")


if __name__ == "__main__":
    pic_name=input("请输入需要爬取的图片类型    ")
    try:
        os.mkdir("picture/"+pic_name)
    except FileExistsError :
        print("文件夹已存在，无需重复创建")
        pass
    save_img(pic_name)













