import os
os.chdir(r'C:\Users\Wangc\Desktop\光大银行数据')
def fun():
    label = ['ei','eif','eo','eq','ilf','mod','sub','sys']
    original_data = ['ei.txt','eif.txt','eo.txt','eq.txt','ilf.txt','mod.txt','sub.txt','sys.txt']
    new_data = ['ei_label.txt','eif_label.txt','eo_label.txt',
                'eq_label.txt','ilf_label.txt','mod_label.txt',
                'sub_label.txt','sys_label.txt']
    for info in range(len(label)):
        n = 0
        f = open(new_data[info],'w',encoding='utf-8')
        with open(original_data[info],'r',encoding='utf-8') as file:
            for i in file:
                if i != '\n':
                    f.write(label[info]+'\t'+i.strip()+' '+i.strip()+' '+i.strip()+' '+i.strip()+' '+i.strip()+' '+i.strip()+' '+i.strip()+' '+i.strip()+' '+i.strip()+' '+i.strip()+'\n')
        f.close()

fun()
