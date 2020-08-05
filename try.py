import tkinter as tk
from tkinter import StringVar, IntVar
from tkinter import filedialog
import tkinter.messagebox
import random
import os
import glob
import matplotlib.pyplot as plt
from PIL import Image, ImageTk


import pygame
pygame.mixer.init()
pygame.mixer.music.set_volume(1.0)


#音效函式

_sound_library = {}
def play_sound(path):
    global _sound_library
    sound = _sound_library.get(path)
    if sound is None:
        temp = path.replace('/', os.sep).replace('\\', os.sep)
        sound = pygame.mixer.Sound(temp)
        sound.set_volume(0.2)
        _sound_library[path] = sound
    sound.play()




#背景音樂
pygame.mixer.music.load("test5.wav")
#音量
pygame.mixer.music.set_volume(0.1)
#循環播放
pygame.mixer.music.play(-1, 0)

window = tk.Tk()
window.title('台南知識王(win1)')
window.resizable(False, False)
window.geometry('{}x{}'.format(600, 200))


def cancel():
    window.destroy()

pic_path=''
fp = open('question1.txt', "r", encoding='UTF-8')

def ok():
    global num,fp,pic_path
    Q=num.get()

    # 獲取picture文件夾的絕對路徑
    pathdir = os.path.abspath('.') 
    #從question.txt讀取題目，解答和相關圖片名稱
    if Q=='1':
        fp = open('question1.txt', "r", encoding='UTF-8')
        path_p = 'pic1'
        pic_path = os.path.join(pathdir, path_p)
        
    elif Q=='2':
        fp = open('question2.txt', "r", encoding='UTF-8')
        path_p = 'pic2'
        pic_path = os.path.join(pathdir, path_p)
        
    elif Q=='3':
        fp = open('question3.txt', "r", encoding='UTF-8')
        path_p = 'pic3'
        pic_path = os.path.join(pathdir, path_p)
        
    elif Q=='4':
        fp = open('question4.txt', "r", encoding='UTF-8')
        path_p = 'pic4'
        pic_path = os.path.join(pathdir, path_p)
        
    elif Q=='5':
        fp = open('question5.txt', "r", encoding='UTF-8')
        path_p = 'pic5'
        pic_path = os.path.join(pathdir, path_p)
     
    else:
        fp = open('question6.txt', "r", encoding='UTF-8')
        path_p = 'pic6'
        pic_path = os.path.join(pathdir, path_p)
        
    lines=fp.readlines()

    for i in range(len(lines)):
        if i%4==0:
            question.append(lines[i])
        elif i%4==1:
            choose.append(lines[i])
        elif i%4==2:
            answer.append(lines[i])
        else:
            lines[i].rstrip()
            picture.append(os.path.join(pic_path,lines[i]))
    fp.close()


    whole=[question,choose,picture]
    new_dialog(whole)


    
question=[]
choose=[]
answer=[]
picture=[]    


reply=0
correct=0
no=0
num=0

record=[]
for i in range(11):
    record.append(0)

tk.Label(window,text='選擇類別\n1：民俗文化 2：美食 3：景點 4：名人名言 5：文學 6：藝術', font=("標楷體"), width=60).pack()
num=tk.StringVar()
tk.Entry(window, textvariable=num, width=30).pack() #Entry:文字輸入欄
tk.Button(window, text="確定", command=ok).pack()
tk.Button(window, text="取消", command=cancel).pack()


win2_timer=None
score=0     
def button_countdown(i,label,window2,correct):
    global reply, win2_timer,score
    if(reply==1 or reply==2 or reply==3):
        if(reply==int(correct)):
            print('2222')
            if(i>5):
                score=score+5
            elif(3<=i<=5):
                score=score+3
            else:
                score=score+1
        if win2_timer is not None:
            window2.after_cancel(win2_timer)
            win2_timer = None
    if i > 0:
        i=i-1
        label.set(i)
        win2_timer = window2.after(1000, lambda:button_countdown(i,label,window2,correct))
    else:
        ans4()


question_text= StringVar()
choose_text= StringVar()
no_text= StringVar()
correct_text= StringVar()
button_label = tkinter.StringVar()
window2=''
def new_dialog(whole):
    global no,correct,label_img,window2,button_label
    window2=tk.Toplevel()
    window2.title('台南知識王(win2)')
    window2.resizable(False, False)
    window2.geometry('{}x{}'.format(1200, 800))
    counter = 10
    button_label.set(counter)
    tkinter.Label(window2, textvariable=button_label,font=("標楷體", 16)).pack()
    button_countdown(counter,button_label,window2, 0)
    question_text.set(whole[0][no])
    choose_text.set(whole[1][no])
    no_text.set("第"+str(no+1)+"題")
    correct_text.set("答對"+str(correct)+"/"+str(no)+"題     共"+str(score)+'分')
    tk.Label(window2, text='歡迎參加台南知識王', font=("標楷體", 16)).pack()
    print(whole[2][no])

    img = Image.open(whole[2][no].rstrip())
    img = img.resize((200, 200), Image.ANTIALIAS)
    print(img.format,img.size)
    img_gif=ImageTk.PhotoImage(image=img)
    label_img = tk.Label(window2, image = img_gif, width = 300,height=300)
    label_img.pack()
    tk.Label(window2, textvariable=no_text, font=("標楷體", 20)).pack()
    tk.Label(window2, textvariable=correct_text, font=("標楷體", 20)).pack()
    tk.Label(window2, textvariable=question_text, font=("標楷體", 12)).pack()
    tk.Label(window2, textvariable=choose_text, font=("標楷體", 20)).pack()
    tk.Button(window2, text = '選擇1', command = ans1, width = 100,height=1).pack()
    tk.Button(window2, text = '選擇2', command = ans2, width = 100,height=1).pack()
    tk.Button(window2, text = '選擇3', command = ans3, width = 100,height=1).pack()
    
    #inputDialog =  MyDialog()
    #window.wait_window(inputDialog)
    window2.mainloop()

#檢查答案
def checkans(replyy):
    global reply,question,choose,answer,no,correct,img_gif,label_img,record, window2,button_label
    if replyy==int(answer[no]) and no<10:
        correct=correct+1
        record[no]=1
        play_sound("test.wav")
    else:
        record[no]=0
        play_sound("test2.wav")
    counter = 10
    button_label.set(counter)
    button_countdown(counter,button_label,window2, answer[no])
    reply=0
    if no<9:
        no=no+1
        no_text.set("第"+str(no+1)+"題")
        question_text.set(question[no])
        choose_text.set(choose[no])
        correct_text.set("答對"+str(correct)+"/"+str(no)+"題     共"+str(score)+'分')
        img = Image.open(picture[no].rstrip())
        img = img.resize((200, 200), Image.ANTIALIAS)
        img_gif = ImageTk.PhotoImage(image=img)
        label_img.configure(image=img_gif, width = 200,height=200)

    elif no==9: 
        #答到最後一題需要按“再來一局”才可以重玩，不然就停在最後一題的畫面
        no_text.set("第10題")
        question_text.set(question[9])
        choose_text.set(choose[9])
        correct_text.set("答對"+str(correct)+"/10題")
        img = Image.open(picture[no].rstrip())
        img = img.resize((200, 200), Image.ANTIALIAS)
        img_gif = ImageTk.PhotoImage(image=img)
        label_img.configure(image=img_gif, width = 200,height=200)
        no=0
        play_sound("test4.wav") 

        #匯出每題對錯的直方圖
        plt.figure(1)
        x=[1,2,3,4,5,6,7,8,9,10]
        plt.xlabel("question no")
        plt.ylabel("true or false")
        plt.yticks(range(10))
        plt.bar(x,record[0:10])

        #匯出對錯率的圓餅圖
        plt.figure(2)
        labels=['correct','wrong']
        percent=[correct/10,(10-correct)/10]
        out=(0,0.1)
        plt.pie(percent,						# 數值
            labels = labels,					# 標籤
            autopct = "%1.1f%%",				# 將數值百分比並留到小數點一位
            explode = out,						# 設定分隔的區塊位置
            pctdistance = 0.6,					# 設定分隔的區塊位置
            textprops = {"fontsize" : 12},		# 文字大小
            shadow=True)   						# 設定陰影					
        plt.show()

def ans1():
    global reply
    reply=1
    checkans(reply)

def ans2():
    global reply
    reply=2
    checkans(reply)

def ans3():
    global reply
    reply=3
    checkans(reply)

def ans4():
    global reply
    reply=4
    checkans(reply)


window.mainloop()
 



































