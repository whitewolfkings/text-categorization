'''
pandas读取excel表格数据。
'''

import pandas as pd
import numpy as np
import os
sheet = ['2017','2016','2015']
os.chdir(r'C:\Users\Wangc\Desktop')
file = open('excel_gongnengdian.txt','w',encoding='utf-8')
for i in sheet:
    data = pd.read_excel('gongnengdian.xlsx',sheet_name=i)
    for j in range(len(data)):
        if data['计数项名称'][j] == 'nan' or data['类别'][j] == 'nan':
            print(i,'----------',j)
        else:
            # print(data['计数项名称'][j],'-------',data['类别'][j])
            file.write(str(data['类别'][j]).lower()+'\t'+str(data['计数项名称'][j])+' '+str(data['计数项名称'][j])+' '+str(data['计数项名称'][j])+' '+str(data['计数项名称'][j])+' '+str(data['计数项名称'][j])+' '+str(data['计数项名称'][j])+' '+str(data['计数项名称'][j])+' '+str(data['计数项名称'][j])+' '+str(data['计数项名称'][j])+' '+str(data['计数项名称'][j])+'\n')
file.close()
f = open('excel_gongnengdian_update.txt','w',encoding='utf-8')
with open('excel_gongnengdian.txt',encoding='utf-8') as file:
    for i in file:
        if 'nan' in str(i):
            continue
        else:
            f.write(i)
f.close()