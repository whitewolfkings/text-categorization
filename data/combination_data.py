import os
os.chdir(r'C:\Users\Wangc\Desktop\光大银行数据')
new_data = ['ei_label.txt','eif_label.txt','eo_label.txt',
                'eq_label.txt','ilf_label.txt','mod_label.txt',
                'sub_label.txt','sys_label.txt']
all_data = open('val.txt','w',encoding='utf-8')
for i in new_data:
    with open(i,encoding='utf-8') as file:
        for j in file:
            all_data.write(j)
all_data.close()
