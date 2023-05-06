import os
import shutil
import pyautogui
import time
import pyperclip
# 打包需要用管理员权限打开pycharm*******************************************
for i in range(1):
    path2 = pyautogui.prompt('请输入你想计算的文件的地址：')
    path1=path2.strip('""')
    path = path1.strip('\'\'')
    a, b = os.path.splitext(path)
    a1,b1 = os.path.split(path)
    t = time.strftime('%Y-%m-%d_%H.%M.%S',time.localtime(time.time()))
    c= a+'_r_'+'mktime_'+t
    os.mkdir(c)
    shutil.copy(path,c)
    c1,c2= os.path.split(c)
    c3 = c+'\\'+b1
    pyperclip.copy(c3)
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

