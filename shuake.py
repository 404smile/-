import pyautogui
import time
import os
import tkinter
from threading import Thread



l2 = os.getcwd()
l = str.replace(l2,"\\","/")


def click(p,confidence=0.9,t=1):
    try:
        time.sleep(t)
        p = pyautogui.locateOnScreen(p, confidence=confidence)
        if p:
            pyautogui.click(p)
            #pyautogui.scroll(-100)
            
            return True
        else:
            return False
    except pyautogui.ImageNotFoundException:
        return False
        
    



def click2(点击图片,精度,输出内容=""):
            try:

               p8 = pyautogui.locateOnScreen(点击图片,confidence=精度)
               if p8:
                   pyautogui.click(p8)
                   print(输出内容)
               else:
                   pass
            except pyautogui.ImageNotFoundException:
               pass   





def scan(识别图片,点击图片,精度1,精度2,滚动量=0,输出内容=""):
        try:
            p2 = pyautogui.locateOnScreen(识别图片,confidence=精度1)
            if p2:
                pyautogui.scroll(滚动量)
                time.sleep(2)
                click(点击图片,confidence=精度2)
                print(输出内容)
            else:
                print("waring!!")
        except pyautogui.ImageNotFoundException:
            pass




def run1():
    def stop():
        r2.destroy()
    #class myway(Thread):
    #def runing():
    
    
    #t = myway()
    #t.start()
    #t.join()
    #time.sleep(3)
    def runing2():
        while True:
            print("start!")
            #if che =="1":
                #r2.destroy()
             #   break
            if click2(f"{l}/nv.png",0.9):
                print("ok")
            else:
                pass
            scan(f"{l}/skip.png",f"{l}/test2.png",0.95,0.9,-2500,"检测到章节检测！！")
            scan(f"{l}/False.png",f"{l}/test.png",0.8,0.9,0,"检测到未完成任务！！")
            scan(f"{l}/True.png",f"{l}/test2.png",0.8,0.9,-750,"检测到已完成任务！！")

            try:
                p4 = pyautogui.locateOnScreen(f"{l}/stop.png",confidence=0.95)
                if p4:
                    pyautogui.click(p4)
                    print("检测到意外暂停！！！")
                else:
                    print("waring!!")
            except pyautogui.ImageNotFoundException:
                pass


            try:
                p6 = pyautogui.locateOnScreen(f"{l}/tip.png",confidence=0.8)
                if p6:
                    click2(f"{l}/test2.png",0.9,"下一节")
                else:
                    pass
            except pyautogui.ImageNotFoundException:
                pass




            try:
                p5 = pyautogui.locateOnScreen(f"{l}/up.png",confidence=0.8)
                print("检测到题！！！！")
                if p5:
                    click2(f"{l}/A.png",0.9,"选择A")
                    time.sleep(2)
                    click2(f"{l}/up2.png",0.9,"提交")
                    try:
                        p7 = pyautogui.locateOnScreen(f"{l}/bad.png",confidence=0.8)
                        time.sleep(2)
                        if p7:
                            click2(f"{l}/B.png",0.9,"选择B")
                            time.sleep(2)
                            click2(f"{l}/up2.png",0.9,"提交")
                            try:
                                p8 = pyautogui.locateOnScreen(f"{l}/bad.png",confidence=0.8)
                                time.sleep(2)
                                if p8:
                                    click2(f"{l}/C.png",0.9,"选择C")
                                    time.sleep(2)
                                    click2(f"{l}/up2.png",0.9,"提交")
                                    try:
                                        p9 = pyautogui.locateOnScreen(f"{l}/bad.png",confidence=0.8)
                                        time.sleep(2)
                                        if p9 :
                                            click2(f"{l}/D.png",0.9,"选择D")
                                            time.sleep(2)
                                            click2(f"{l}/up2.png",0.9,"提交")
                                        else:
                                            pass
                                    except pyautogui.ImageNotFoundException:
                                        pass
                                else:
                                    pass
                            except pyautogui.ImageNotFoundException:
                                pass
                        else:
                            pass
                    except pyautogui.ImageNotFoundException:
                        pass
                else:
                    pass
            except pyautogui.ImageNotFoundException:
                pass
    r.destroy()
    #t1 = Thread(target=runing)
    t2 = Thread(target=runing2)
    t2.setDaemon(True)
    t2.start()
    
    r2 = tkinter.Tk()
    r2.geometry("400x500+700+250")
    r2.iconbitmap(f"{l}/tubiao4.ico")
    r2.title("正在刷课中.....")
    p2 = tkinter.PhotoImage(file=f"{l}/runing.png")
    text2 = tkinter.Label(r2,image=p2,text="正在刷课中....",compound="top")    
    b1 = tkinter.Button(r2,text="关闭",command=stop)
    r2.protocol("WM_DELETE_WINDOW",stop)
    text2.pack()
    b1.pack()
    r2.mainloop()
    #t1.start()



   


r = tkinter.Tk()
r.title("刷客v1.5")
r.resizable(False,False)
r.geometry("323x800+800+120")
r.iconbitmap(f"{l}/tubiao4.ico")
test = tkinter.Canvas(r,width=323,height=400)
test.pack()
text2 = tkinter.Label(r,text="使用方法:\
                     \n1.打开*习通，找到你要刷的课程\
                     \n2.进入学习界面并全屏\
                     \n3.打开刷客，并点击“开始刷课”然后再进入学习通界面\
                     \n (注：1.本脚本只适用于Windows11，所以操作系统不是windowns11的不建议使用【会有不可名状的bug！！！,如果执意使用，后果自负！！！】\
                     2.本脚本运行时要求分辨率为1920x1080下运行，过高或过低都会导致不识别\
                     3.在运行前后不要滚动学习通学习界面，否则会导致不识别或不可名状的bug（所造成的损失均不负责！！！）\
                     4.对脚本及脚本图标和图片有意见的自己退出脚本，有本事来咬我啊！！！\n)\
                     咨询qq:************",\
                     justify="left",\
                     wraplength=300)
p = tkinter.PhotoImage(file=f"{l}/back2.png")
test.create_image(0,0,anchor="nw",image=p)
test.create_text(90,40,text="由“秋裤超人”出品\n联系电话：*************")

botten = tkinter.Button(r,text="开始刷课",compound="top",command=run1)
text2.pack()
botten.pack()
r.mainloop()




                    
        
        
    
    
    