# -*- coding: utf-8 -*-
import re
import os
file_dir = r'D:\work\text-classification-cnn-rnn\hetong'
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
    all_function_necessary = re.findall(r"1、功能需求描述(.*)2、业务处理流程",s.replace(' ',''),re.S)
    all_service = re.findall(r"3、 业务规则(.*)4、界面处理", s.replace(' ',''),re.S)
    all_logic = re.findall(r"6、处理逻辑(.*)7、性能需求", s.replace(' ',''),re.S)
    # for i in all_function_necessary:
    #     print(txt,'---->',i)
    # for i in all_service:
    #     print(txt,'---->',i)
    # for i in all_logic:
    #     print(txt,'---->',i)


    '''
    findall()方法：返回string中所有与pattern相匹配的全部字串，返回形式为数组
    re.S:使用re.S参数以后，正则表达式会将这个字符串作为一个整体，在整体中进行匹配。
    '''
    with open(r'D:\work\text-classification-cnn-rnn\self_code\re.txt','a+',encoding='utf-8') as f:
        for i in all_function_necessary:
            #f.write("<<"+txt+">>"+":"+i)
            f.write(i)
        for i in all_service:
            #f.write("<<"+txt+">>"+":"+i)
            f.write(i)
        for i in all_logic:
            #f.write("<<"+txt+">>"+":"+i)
            f.write(i)

'''
re处理过的数据，--->句子的格式。(标题和下面的解释的句子合在一起)
'''
'''
re.txt：
(1)小括号的内容这是一句话；
1.这些是和下面的内容在一起的；
一.这些是无用的内容。
'''
# all = []
# num = []
# with open('re.txt','r',encoding='utf-8') as file:
#     for i in file:
#         if i.strip() != '':
#             all.append(i.strip())
# for i in range(len(all)):
#     if all[i][0].isdigit():
#         num.append(all[i])
# # print(len(all))   #1316
# flag = False
# a = 0
# for i in range(len(all)):
#     for k in range(i+1,len(all)):
#         s = ''
#         for j in range(len(num)-1):
#             if all[i][0].isdigit() and all[i] == num[j] and all[k] == num[j+1]:
#                 for z in range(i,k):
#                     s += all[z]
#                 print(s)
#                 i = k
#             else:
#                 pass
#                 # print("k的值是:::::",k)


# for i in range(1,len(all)):
#     if all[i][0].isdigit() == False and all[i][0] != "（":
#         print(all[i])

