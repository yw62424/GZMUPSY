import turtle
import math
import random

turtle.screensize(800,800, "#a9fdf4")
random.seed(0)
color_list=["#f28e0d","#25211d","#a1e00b","#2f1e88","#e96194","#f5f741"]
balls_list=["#f74710","#1130ee","#ebde11","#d507ee"]

def y1(x):
    return 150+50*math.sqrt(3)-abs(math.sqrt(3)*x)

def y2(x):
    return 150+10*math.sqrt(3)-abs(x)

def y3(x):
    return 150+10*math.sqrt(3)-abs(4/3*x)

turtle.speed(9)
turtle.delay(0)


def steam():
    turtle.goto(-50,-50)
    turtle.seth(0)
    turtle.begin_fill()
    turtle.color("#6b3e05")
    turtle.pendown()
    for i in "1111":
        turtle.fd(100)
        turtle.right(90)
    turtle.end_fill()
    turtle.penup()

def leaf(size=6,color="green"):
    turtle.pensize(3)
    turtle.pendown()
    turtle.right(90)
    turtle.color(color)
    for i in "111":
        turtle.fd(size)
        turtle.right(180)
        turtle.fd(size)
        turtle.right(60)
    turtle.hideturtle()
    turtle.penup()

def layer():       
    for i in range(100):
        x=random.randint(-1*50,50)
        turtle.goto(x,random.randint(math.floor(y1(50)),math.floor(y1(x))))
        leaf()

    for i in range(250):
        x=random.randint(-1*100,100)
        turtle.goto(x,random.randint(math.floor(10*math.sqrt(3)+50),math.floor(y2(x) if math.floor(y2(x))<150 else 150)))
        leaf()

    for i in range(400):
        x=random.randint(-1*150,150)
        turtle.goto(x,random.randint(-50,math.floor(y3(x) if math.floor(y3(x))<10*math.sqrt(3)+50 else 10*math.sqrt(3)+50)))
        leaf()

def soil():
    turtle.pensize(1)
    for i in range(180):
        turtle.goto(random.randint(-200,200),random.randint(-200,-150))
        turtle.pendown()
        turtle.pencolor(random.choice(color_list))
        turtle.circle(random.randint(1,6),360)
        turtle.penup()

def star():
    turtle.penup()
    turtle.fillcolor("yellow") 
    turtle.begin_fill()         
    turtle.goto(-25,250)     
    count = 1                        
    while count <= 5:                
        turtle.forward(50) 
        turtle.right(144)
        count += 1                  
    turtle.end_fill()               

def tree():
    layer()
    steam()

def fun_1(x):
    return math.floor( math.sin(0.05*x)*100*math.exp(-0.006*x))

def belt(s=-137,e=127):
    turtle.penup()
    x_int,y_int=fun_1(s),s+102
    turtle.goto(x_int,y_int)
    turtle.pendown()
    turtle.pensize(5)
    turtle.color("yellow")
    for x in range (s,e):
        y=fun_1(x)
        turtle.goto(y,x+102)
        
def ball():
    random.seed(6)
    turtle.penup()
    for i in range(15):
        x,y=random.randint(-150,150),random.randint(-100,200)
        turtle.goto(x,y)
        turtle.pencolor(random.choice(balls_list))
        turtle.pendown()
        turtle.dot(20)
        turtle.penup()

def words():
    turtle.pu() # 抬笔
    turtle.color("red") # 设置画笔颜色
    
    text='Merry' # 设置文本内容
    x=len(text) # 文本字数
    turtle.goto(150,200) # 定位
    for i in text:
        turtle.write(i, font=("隶书", 25, "normal")) # 逐个输出文字
        # turtle.rt(360/x) # 右转
        turtle.fd(20) # 前进
    
    text='Christmas!' # 设置文本内容
    x=len(text) # 文本字数
    turtle.goto(110,160) # 定位
    for i in text:
        turtle.write(i, font=("隶书", 25, "normal")) # 逐个输出文字
        # turtle.rt(360/x) # 右转
        turtle.fd(20) # 前进
    
    text='---- Yang' # 设置文本内容
    x=len(text) # 文本字数
    turtle.goto(120,-240) # 定位
    turtle.pencolor("black")
    for i in text:
        turtle.write(i, font=("黑体", 25, "normal")) # 逐个输出文字
        # turtle.rt(360/x) # 右转
        turtle.fd(20) # 前进

    text='2021-12-25' # 设置文本内容
    x=len(text) # 文本字数
    turtle.goto(110,-280) # 定位
    for i in text:
        turtle.write(i, font=("黑体", 25, "normal")) # 逐个输出文字
        # turtle.rt(360/x) # 右转
        turtle.fd(20) # 前进


def main():
    star()
    tree()
    soil()
    belt()
    ball()
    words()
    turtle.hideturtle()
    window = turtle.Screen()
    window.exitonclick()


if __name__ == '__main__':
    main()

