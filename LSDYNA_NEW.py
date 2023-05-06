import os
import shutil
import pyautogui
# import osssssssssss.path as op
import time
import pyperclip
# 打包需要用管理员权限打开pycharm*******************************************
# times = input('请输入创建文件夹数量：')
# times1=int(times)
times1 = 1
for i in range(1,times1+1):
    print('**第',i,'次','创建')
    path2 = pyautogui.prompt('请输入你想计算的文件的地址：')
    # pyautogui.hotkey('ctrl','v')
    # pyautogui.hotkey('enter')
    path1=path2.strip('""')#strip自动删除字符串末尾或者开头的字符""
    path = path1.strip('\'\'')#转义字符让解释器知道''是普通字符
    print(path)
    print('----------------------------------------------')
    print('1.你的文件地址为：',path)
    print('--------------------------------------------')
    print('2.在此文件地址创建根据时间命名的新结果文件夹')
    print('------------------------------------------- ')
    a, b = os.path.splitext(path)
    a1,b1 = os.path.split(path)
    # print(a1)
    # print(b1)
    t = time.strftime('%Y-%m-%d_%H.%M.%S',time.localtime(time.time()))
    # t1=str(t)
    c= a+'_r_'+'mktime_'+t
    os.mkdir(c)
    print('3.文件格式为：',b)
    print('--------------- ')
    shutil.copy(path,c)
    print('4.已创建',i,'个文件夹','还剩余',times1-i,'个文件夹可创建','已将源文件复制进入新文件夹可开始计算')
    print('-------------------------------------------------------------------------------------------- ')
    print('5.新文件夹地址为：',c)
    print('-------------------------------------------------------------------------------------------- ')
    c1,c2= os.path.split(c)
    c3 = c+'\\'+b1
    print('6.新文件地址为：',c3)
    print('-------------------------------------------------------------------------------------------- ')
    pyperclip.copy(c3)
    print('7.新文件地址已复制到剪切板')
    print('------------------------- ')
    # os.startfile(c1)#打开目录文件
    # os.startfile(c)#打开文件所在地
os.popen('D:\LSDYNA\manager.exe')
def mouseclic(img):
    while True:
        location = pyautogui.locateCenterOnScreen(img, confidence=0.9)
        if location is not None:
            pyautogui.click(location.x, location.y, clicks=1, interval=0.2, duration=0, button='left')
            break
        print("未找到匹配图片,0.1秒后重试")
        time.sleep(0.1)
def mouseclic1(img):
    while True:
        location = pyautogui.locateCenterOnScreen(img, confidence=0.9)
        if location is not None:
            pyautogui.click(location.x, location.y, clicks=2, interval=0.1, duration=0, button='left')
            break
        print("未找到匹配图片,0.1秒后重试")
        time.sleep(0.1)
def mouseclic2(img):
    while True:
        location = pyautogui.locateCenterOnScreen(img, confidence=0.9)
        if location is not None:
            pyautogui.click(location.x, location.y, clicks=2, interval=0.1, duration=0, button='left')
            break
        print("未找到匹配图片,0.1秒后重试")
        time.sleep(0.1)
# def testing(img):
#     time.sleep(1)
#     for i in range(3):
#         location = pyautogui.locateCenterOnScreen(img, confidence=0.9)
#         if location is not None:
#             print('出错啦')
#             while True:
#                 location = pyautogui.locateCenterOnScreen("D:\guii\step6.png", confidence=0.9)
#                 if location is not None:
#                     pyautogui.click(location.x, location.y, clicks=2, interval=0.1, duration=0, button='left')
#                     time.sleep(2)
#                     pyautogui.typewrite( 'it_is_going_wrong')
#                     pyautogui.hotkey('enter')
#                     pyautogui.hotkey('enter')
#                     break
#                 print("未找到匹配图片,0.1秒后重试")
#                 time.sleep(0.1)
#             break
#         print("正在监视错误，目前未出错,3小时后重新检测")
#         time.sleep(10800)
if __name__ == '__main__':
    imgs = ["D:\guii\step1.png","D:\guii\step2.png"]
    for img in imgs :
        print(img)
        mouseclic(img)
    pyautogui.hotkey('ctrl','v')
    pyautogui.hotkey('enter')
    imgs1="D:\guii\step3.png"
    print(imgs1)
    mouseclic1(imgs1)
    pyautogui.typewrite('8')
    imgs2 = "D:\guii\step4.png"
    mouseclic2(imgs2)
    pyautogui.typewrite('800000000')
    pyautogui.hotkey('enter')
    # ___________________________________________________________
    # imgs3 = "D:\guii\step5.png"
    # testing(imgs3)


