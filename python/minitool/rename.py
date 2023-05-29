import os
path='C:/Users/LENOVO/Desktop/4000-new/'
T=[]

##选择一个文件夹，将该文件夹中的多个子文件夹中的文件重命名，（用于合并压缩包。）

def change(path,m):
    #获取该目录下所有文件，存入列表中
    f=os.listdir(path)
    n=0
    for i in f: 
        #设置旧文件名（就是路径+文件名）
        oldname=path+"/"+f[n]
        
        #设置新文件名
        newname=path+'/'+str(m)+'__'+str(n+1)+'.png'
        
        #用os模块中的rename方法对文件改名
        os.rename(oldname,newname)
        print(oldname,'======>',newname)
        
        n+=1
s=os.listdir(path)
m=0
for a in s :
    m+=1
    T=path+a
    print(T)
    change(T,m)








