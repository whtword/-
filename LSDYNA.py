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
    path2 = input('请输入你想计算的文件的地址：')
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
    # -------------------单独电脑开发，其余电脑须依靠图像识别--
    time.sleep(2)
    pyautogui.click(152, 257)
    pyautogui.click(716, 371)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.hotkey('enter')
    pyautogui.doubleClick(625, 536)
    pyautogui.typewrite('800000000')
    pyautogui.click(411, 534)
    pyautogui.typewrite('8')
    pyautogui.hotkey('enter')
    # answer = input('是否开始运算? y/n：')
    # if answer == 'y':
    #     print('8.** ** ** ** ** 开始运算 ** ** ** ** **')
    #     print('--------------------------------------- ')
    #     os.popen('D:\LSDYNA\manager.exe')
    # else:
    #     print('----------')
    #     print('8.手动运算')
    #     print('新文件夹地址为：', c)
    #     print('-------------------------------------------------------------------------------------------- ')
    # print('8.** ** ** ** ** 开始运算 ** ** ** ** **')
    # print('--------------------------------------- ')
    # os.popen('D:\LSDYNA\manager.exe')





