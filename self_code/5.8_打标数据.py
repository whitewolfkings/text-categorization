f = open('dabiao.txt','w',encoding='utf-8')
with open(r'C:\Users\Wangc\Desktop\业务分析单0508.txt',encoding='utf-8') as file:
    for i in file:
        if i != '\n':
            f.write('ilf    '+i)
f.close()

