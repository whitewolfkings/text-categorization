v_list = ['修改','删除','新增','增加','页面','节点','按钮','<<','>>']

def analisis():
    # import os
    # file_dir = r'C:\Users\Wangc\Desktop\业务分析单txt'
    # os.chdir(file_dir)
    # article = []
    # for root, dirs, files in os.walk(file_dir):
    #     article += files   # 当前路径下所有非目录子文件

    f_w = open(r'D:\work\text-classification-cnn-rnn\self_code\under.txt','w',encoding='utf-8')
    # for file in article:
    list = []
    list2 = []
    with open(r'D:\work\text-classification-cnn-rnn\self_code\re.txt',encoding='utf-8') as f:
        for i in f:
            for j in v_list:
                if j in i:
                    list.append(i)
    # print(list)
    [list2.append(i) for i in list if not i in list2]
    for i in list2:
        f_w.write(i)
    f_w.close()

analisis()