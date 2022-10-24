import tkinter as tk
import os
import numpy as np
import tkinter.ttk as ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

import matplotlib.pyplot as plt
root = tk.Tk()

root.title("随机生成样例")
root.geometry('300x300+10+10')
#root.iconbitmap('D:\python project\GUI\图标.ico')
root.resizable(0,0)
'''
参数列表：
个数 ： len
最小值：minn
最大值： maxx

是否有重复：repeat

是否为浮点：dott

生成文件的次数 count

存有大小写字母的列表 alp
'''

#初始化参数

alp1=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
      'n','o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alp2=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
      'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
alp = alp1+alp2
len1 = 0
minn1 = 0
maxx1 = 0

count1 = 0
repeat1 = False

dott = False


len_fu = 0
len_zi = 0

count2 = 0
repeat2 = False
diff = False
#导出信息
def chuang(name):
    if(os.path.exists(name)==False):
        file1 = open(name+'.in','w')
        file2 = open(name + '.out', 'w')
        file1.close()
        file2.close()
def sendMsg1():
    global len1 ,minn1,maxx1,count1
    count1+=1
    if(count1>100):
        count1=1
    sendMsg_n = t1_Msg.get('0.0', 'end')
    sendMsg_min = t2_Msg1.get('0.0', 'end')
    sendMsg_max = t2_Msg2.get('0.0', 'end')
    t1_Msg.delete('0.0', "end")
    t2_Msg1.delete('0.0', "end")
    t2_Msg2.delete('0.0', "end")
    len1 = int(sendMsg_n)
    minn1 = int(sendMsg_min)
    maxx1 = int(sendMsg_max)
    #print( sendMsg_n, sendMsg_min, sendMsg_max)
    #print(len1,minn1,maxx1)


def select11():
    global repeat1
    dict = {1:'否',0:'是',3:'否',2:'是'}
    strings = '您选择了' + dict.get(v1.get()) + '，祝您学习愉快'
    if(v1.get()==1):
        repeat1 = True
    else:
        repeat1 = False
    #print(strings)

def select12():
    global dott1
    dict = {1:'否',0:'是',3:'否',2:'是'}
    strings = '您选择了' + dict.get(v2.get()) + '，祝您学习愉快'
    if (v2.get() == 2):
        dott1= True
    else:
        dott1 = False
    #print(strings)

def printf1():
    if(repeat1==False):
        if(dott1== True):
            data = np.around(((np.random.rand(len1)*(maxx1-minn1)+minn1)),3)
        else:
            data = np.random.randint(minn1, maxx1,size=[1,len1])
        name = str(count1)
        if (os.path.exists(name) == False):
            file1 = open(name + '.in', 'w')
            file2 = open(name + '.out', 'w')
            file1.write(str(len1)+'\n')
            #print(data)
            strings = str(data)
            file1.write(strings[2:-2])
            file1.close()
            file2.close()
    else:
        data = []
        if (dott1 == True):
            for i in range(len1):
                temp = np.around(((np.random.rand() * (maxx1 - minn1) + minn1)),3)
                if(np.random.randint(0,len1)>=i and np.random.randint(0,len1)<=3*i):
                    data.append(temp)
                data.append(temp)
        else:
            for i in range(len1):
                temp =np.random.randint(minn1,maxx1)
                if(np.random.randint(0,len1)>=i and np.random.randint(0,len1)<=3*i):
                    data.append(temp)
                data.append(temp)
        name = str(count1)
        data = np.array(data)
        if (os.path.exists(name) == False):
            file1 = open(name + '.in', 'w')
            file2 = open(name + '.out', 'w')
            file1.write(str(len1) + '\n')
            #print(data)
            strings = str(data)
            file1.write(strings[2:-2])
            file1.close()
            file2.close()
    #print("需要的长度为,", len1, "需要的范围为,", minn1, "到", maxx1, "是否需要重复:", repeat1, "是否为浮点数", dott1)

#标签设置

tab_main=ttk.Notebook()#创建分页栏
tab_main.place(relx=0.02, rely=0.02, relwidth=0.887, relheight=0.876)

tab1=tk.Frame(tab_main)#创建第一页框架

tab1.place(x=0,y=30)
tab_main.add(tab1,text='数字样例')#将第一页插入分页栏中

label1 = tk.Label(tab1,text="样例长度：")
label1.place(x=20, y=2)

label2 = tk.Label(tab1,text="最小值：")
label2.place(x=20, y=25)

label3 = tk.Label(tab1,text="最大值：")
label3.place(x=20, y=45)

label4 = tk.Label(tab1,text="是否重复：")
label4.place(x=20, y=65)

label5 = tk.Label(tab1,text="是否是浮点数：")
label5.place(x=20, y=85)

#输入的设置
t1_Msg = tk.Text(tab1,width=5, height=1)
t1_Msg.place(x=80, y=5)

t2_Msg1 = tk.Text(tab1,width=5, height=1)
t2_Msg1.tag_config('green', foreground='#008C00')
t2_Msg1.place(x=80, y=30)

t2_Msg2 = tk.Text(tab1,width=5, height=1)
t2_Msg2.tag_config('green', foreground='#008C00')
t2_Msg2.place(x=80, y=50)


# IntVar() 用于处理整数类型的变量
v1 = tk.IntVar()
# 是否包含重复值
radio_button1 = tk.Radiobutton(tab1,text = "否", variable = v1,value =0,command=select11)
radio_button2 = tk.Radiobutton(tab1,text = "是", variable = v1,value =1,command=select11)
radio_button1.place(x=100, y=65)
radio_button2.place(x=150, y=65)

#是否是浮点数
v2= tk.IntVar()
radio_button3 = tk.Radiobutton(tab1,text = "是", variable = v2,value =2,command=select12)
radio_button4 = tk.Radiobutton(tab1,text = "否", variable = v2,value =3,command=select12)
radio_button3.place(x=100, y=85)
radio_button4.place(x=145, y=85)

#获取信息的按钮
button1 = tk.Button(tab1,text='生成',command=sendMsg1)
button1.place(x=20, y=110)

#结束的按钮
button2 = tk.Button(tab1,text='关闭窗口',command=root.quit)
button2.place(x=75, y=110)

button2 = tk.Button(tab1,text='输出',command=printf1)
button2.place(x=150, y=110)


'''========================================================================================================='''
def sendMsg2():
    global len_fu ,len_zi,count2
    count2+=1
    if(count2>100):
        count2=1
    sendMsg_n = t3_Msg.get('0.0', 'end')
    sendMsg_min = t4_Msg1.get('0.0', 'end')
    t3_Msg.delete('0.0', "end")
    t4_Msg1.delete('0.0', "end")
    len_fu = int(sendMsg_n)
    len_zi = int(sendMsg_min)
    #print( sendMsg_n, sendMsg_min, sendMsg_max)
    #print(len,minn,maxx)


def select22():
    global diff
    dict = {3:'是',2:'否'}
    strings = '您选择了' + dict.get(v4.get()) + '，祝您学习愉快'
    if (v4.get() == 3):
        diff = True
    else:
        diff = False
    #print(strings)


def printf2():
    data_fu = ""
    data_zi =""
    name = str(count2)
    if(diff==True):
        for i in range(len_fu):
            idx = np.random.choice(alp1)
            data_fu+=idx
        r = np.random.randint(0,len_fu-len_zi)
        data_zi = data_fu[r:r+len_zi]
    else:
        for i in range(len_fu):
            idx = np.random.choice(alp)
            data_fu+=idx
        r = np.random.randint(0,len_fu-len_zi)
        data_zi = data_fu[r:r+len_zi]
    if (os.path.exists(name) == False):
        file1 = open(name + '.in', 'w')
        file2 = open(name + '.out', 'w')
        file1.write(str(len_fu) + ' '+str(len_zi)+'\n')
        #print(data_fu)
        file1.write(data_fu+'\n')
        file1.write(data_zi + '\n')
        file1.close()
        file2.close()
    #print(data_fu,data_zi)
    #print("父串的长度：",len_fu,"子串的长度:",len_zi,"是否需要大小写字母：",diff)


#第二个界面，字符界面
tab2=tk.Frame(tab_main)
tab2.place(x=100,y=30)

tab_main.add(tab2,text='字母样例')

label1 = tk.Label(tab2,text="父串长度：")
label1.place(x=20, y=2)

label2 = tk.Label(tab2,text="子串长度：")
label2.place(x=20, y=25)


label4 = tk.Label(tab2,text="是否只有大(小)写字母：")
label4.place(x=20, y=60)


#输入的设置
t3_Msg = tk.Text(tab2,width=5, height=1)
t3_Msg.place(x=80, y=2)

t4_Msg1 = tk.Text(tab2,width=5, height=1)
t4_Msg1.place(x=80, y=25)
'''
t2_Msg2 = tk.Text(tab2,width=5, height=1)
t2_Msg2.tag_config('green', foreground='#008C00')
t2_Msg2.place(x=80, y=45)
'''


v4 = tk.IntVar()
radio_button1 = tk.Radiobutton(tab2,text = "否", variable = v4,value =2,command=select22)
radio_button2 = tk.Radiobutton(tab2,text = "是", variable = v4,value =3,command=select22)
radio_button1.place(x=150, y=60)
radio_button2.place(x=200, y=60)
#获取信息的按钮
button1 = tk.Button(tab2,text='生成',command=sendMsg2)
button1.place(x=20, y=110)

#结束的按钮
button2 = tk.Button(tab2,text='关闭窗口',command=root.quit)
button2.place(x=75, y=110)

button2 = tk.Button(tab2,text='输出',command=printf2)
button2.place(x=150, y=110)

root.mainloop()
