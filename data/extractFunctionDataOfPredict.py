# -*- coding: utf-8 -*-
import re
import os

# file_dir = r'C:\Users\Wangc\Desktop\业务分析单txt'
# os.chdir(file_dir)

'''
正则处理预测时候的分析表
'''
def reExtractAnalysisSheetOfPredict(file_in,file_out):
    with open(file_in,encoding='gbk') as file:
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
    return file_out


'''
正则处理预测时候的申请表
'''
def reExtractApplySheet():
    pass


def reExtractExplainSheetOfPredict(file_in,file_out):
    f = open(file_out, 'w', encoding='utf-8')
    with open(file_in,encoding='utf-8') as file:
        for i in file:
            f.write(i)
    return file_out