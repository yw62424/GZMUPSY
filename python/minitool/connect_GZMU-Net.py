# this easy .py script is used to connect the GZMU or GZMU-Dorm without input account or password！
# Just because i m a lazy man !  Have fun, u will love it!

import requests
import socket  

#### here input u own accounts if u have many #####
# for example:

# users={
#    "1":["校园网学号","密码"],
#    "2":["2023210315","******"],
#    "3":("2019141050","*******")
# }

users={
   "1":["2019141032","****"],
}
##############

headers={
    'Accept':'*/*',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection':'keep-alive',
    'Host':'192.168.12.3:801',
    'Referer':'http://192.168.12.3/',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.57',
    }

def get_local_ip():  
    """  
    获取本机IP地址  
    :return: 返回本机IP地址  
    """  
    try:  
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  
        s.connect(('8.8.8.8', 1))  
        ip = s.getsockname()[0]  
    except:  
        ip = '127.0.0.1'  
    finally:  
        s.close()  
    return ip  

def connect(n):
    acc,psw=users[n]
    ip=get_local_ip()
    url="http://192.168.12.3:801/eportal/portal/login?callback=dr1003&login_method=1&user_account=%2C0%2C"+acc+"&user_password="+psw+"&wlan_user_ip="+ip+"&wlan_user_ipv6=&wlan_user_mac=000000000000&wlan_ac_ip=192.168.13.2&wlan_ac_name=&jsVersion=4.1.3&terminal_type=1&lang=zh-cn&v=1163&lang=zh"
    r=requests.get(url,headers=headers,timeout=5)
    if r:
        print(r.content.decode("utf8"))
    else: 
        print("net error")

# 使用示例  
if __name__ == '__main__':  
##### choose which account u want to connect!
    connect("1")