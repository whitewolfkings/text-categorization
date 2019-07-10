filter_string = '　)\t □█■▉'

def analysis():
    f = open('all_preprocess.txt', 'w', encoding='utf-8')
    with open('all.txt', encoding='utf-8') as file:
        for i in file:
            lines = filter(lambda c: c not in filter_string, i)
            for j in lines:
                f.write(j)
    f.close()

def apply():
    f = open('businessApplySheet_preprocess.txt', 'w', encoding='utf-8')
    with open('businessApplySheet.txt', encoding='utf-8') as file:
        for i in file:
            if '新增需求' in i:
                pass
            else:
                lines = filter(lambda c: c not in filter_string, i)
                for j in lines:
                    f.write(j)


    f.close()

def explain():
    f = open('businessExplain_preprocess.txt', 'w', encoding='utf-8')
    with open('businessExplain.txt', encoding='utf-8') as file:
        for i in file:
            if i == '*变化状态：A--增加，M--修改，D--删除\n':
                pass
            else:
                lines = filter(lambda c: c not in filter_string, i)
                for j in lines:
                    f.write(j)
    f.close()

analysis()
# apply()
# explain()