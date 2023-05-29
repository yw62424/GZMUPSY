import os
import json
 
dirPath = 'D:\\b站视频缓存\\37256346'
dir="D:\\b站视频缓存\\37256346"

def isnumeric(s):
  '''returns True if string s is numeric'''
  return all(c in "0123456789.+-c_" for c in s)
 
def getdir(path):
    files = os.listdir(path)          ###获取全部文件夹
    for f in files:                  #######遍历每一个小文件夹
        if not os.path.isfile(f):     ###########不选中文件，找到文件夹
            readJson(path + '/'+ f)

            # if isnumeric(f):   #  bili客户端拷贝出来的是数字目录
            #     if len(f) > 4 :               ##直到找到小于4个文件的目录
            #         getdir(path+'/'+f)
            #     else:
            #         readJson(path + '/'+ f)

                
def readJson(path):
    ################   路径为每个小视频
    os.chdir(path)
    if os.path.exists("entry.json"):
        f = open( "entry.json", encoding='utf-8')
        setting = json.load(f)
        title = setting['title'].replace('\\','').replace('/','').replace(' ','').replace('|','')  #出现空格，ffmpeg执行会出错，出现|，创建目录失败
        titlepath = 'D:/b站视频缓存/' + title
        try:
            if not os.path.exists(titlepath):      # 没有，创建目录
                os.makedirs(titlepath)
        except Exception as e:
            pass
        filename = setting['page_data']['part'].replace(' ','').replace('-','').replace('&','') #获取文件的名字，去掉空格和-字符
        filepath = path        + '/'+str(setting['prefered_video_quality'])
        filepath1 = filepath  + '/' + 'video.m4s'
        filepath2 = filepath  + '/' + 'audio.m4s'
        if os.path.exists(filepath1) and os.path.exists(filepath2) and not os.path.exists(titlepath + '/' + filename +'.mp4'):
            executecmd(filepath1,filepath2,titlepath + '/' + filename +'.mp4')  #文件名字固定
        else:
            print('not need exchange files.')
    else:
        print("视频解析错误！！")
 
'''
第一个参数是输入文件video.m4s的路径
第二个参数是输入文件audio.m4s的路径
第三个参数是输出的文件路径
'''
def executecmd(f1,f2,f3):
    if not os.path.exists(f3):
        r = os.popen('ffmpeg' + ' -i ' + f1 + ' -i ' + f2 + ' -codec copy ' + f3)
        r.close()
        # print(r.read())
    # else:
    #     print('file exists!')
7 
 
if __name__ == "__main__":

    getdir(dirPath)
    print("完成")