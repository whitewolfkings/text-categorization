# -*- coding: utf-8 -*-
import re
import os

def reExtractAnalysisSheet():   #分析单
    file_dir = r'C:\Users\Wangc\Desktop\业务分析单txt'
    file_out = r'D:\python_code\text-classification-cnn-rnn-master\data\reMatchAnalysisData.txt'

    os.chdir(file_dir)
    article = []
    for root, dirs, files in os.walk(file_dir):
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
        '''
        findall()方法：返回string中所有与pattern相匹配的全部字串，返回形式为数组
        re.S:使用re.S参数以后，正则表达式会将这个字符串作为一个整体，在整体中进行匹配。
        '''
        with open(file_out,'a+',encoding='utf-8') as f:
            for i in all_function_necessary:
                f.write(i)
            for i in all_service:
                f.write(i)
            for i in all_logic:
                f.write(i)

def reExtractApplySheet():  #申请单
    file_dir = r'C:\Users\Wangc\Desktop\业务申请单txt'
    file_out = r'D:\python_code\text-classification-cnn-rnn-master\data\reMatchApplyData.txt'
    os.chdir(file_dir)
    article = []
    for root, dirs, files in os.walk(file_dir):
        article += files  # 当前路径下所有非目录子文件
    for txt in article:
        with open(txt, encoding='gbk') as file:
            s = ''
            for i in file:
                s += i
            # print(s)
            all_backgroundAndGoal = re.findall(r"背景及目标(.*)业务规则",s.replace(' ',''),re.S)


        with open(file_out, 'a+', encoding='utf-8') as f:
            for i in all_backgroundAndGoal:
                f.write(i)
    # return file_out

def reExtractExplainSheet():
    file_dir = r'C:\Users\Wangc\Desktop\业务需求说明书txxt'
    file_out = r'D:\python_code\text-classification-cnn-rnn-master\data\reMatchExplainData.txt'
    os.chdir(file_dir)
    article = []
    for root, dirs, files in os.walk(file_dir):
        article += files  # 当前路径下所有非目录子文件

    f = open(file_out, 'a+', encoding='utf-8')
    for txt in article:
        with open(txt, encoding='gbk') as file:
            for i in file:
                f.write(i)
    f.close()
    # return file_out

# reExtractAnalysisSheet()
# reExtractApplySheet()
reExtractExplainSheet()