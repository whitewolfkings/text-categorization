# -*- coding: utf-8 -*-
import re
import os
file_dir = r'D:\工作\光大银行\样本数据\样本数据\pkdata\业务申请单txt'
os.chdir(file_dir)
article = []
for root, dirs, files in os.walk(file_dir):
    # print(root)  # 当前目录路径
    # print(dirs)  # 当前路径下所有子目录
    article += files   # 当前路径下所有非目录子文件
for txt in article:
    with open(txt,encoding='gbk') as file:
        s = ''
        for i in file:
            s += i
    # print(s)
    all_function_necessary = re.findall(r"背景及目标(.*)业务规则",s.replace(' ',''),re.S)
    #for i in all_function_necessary:
        #print(txt,'---->',i)
    # for i in all_service:
    #     print(txt,'---->',i)
    # for i in all_logic:
    #     print(txt,'---->',i)


    '''
    findall()方法：返回string中所有与pattern相匹配的全部字串，返回形式为数组
    re.S:使用re.S参数以后，正则表达式会将这个字符串作为一个整体，在整体中进行匹配。
    '''
    with open(r'D:\work\text-classification-cnn-rnn\apply.txt','a+',encoding='utf-8') as f:
        for i in all_function_necessary:
            #f.write("<<"+txt+">>"+":"+i)
            f.write(i)
        # for i in all_service:
        #     #f.write("<<"+txt+">>"+":"+i)
        #     f.write(i)
        # for i in all_logic:
        #     #f.write("<<"+txt+">>"+":"+i)
        #     f.write(i)
