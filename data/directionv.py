import  re
v_list = ['新增','添加','增加','提供','修改','变更','调整','更新','优化','改造','改为','扩展','扩容','扩长','作废','取消','屏蔽','去除','去掉','删除','累加','支持']
n_list=['页面','按钮','接口','字段','表','功能','条件','规则','校验','工具','模板','提醒','提示','判断','选项','权限','标记','标志','参数','状态','复选框','格式','工具','限制','查询','方式']
def apply():
    # import os
    # file_dir = r'C:\Users\Wangc\Desktop\业务分析单txt'
    # os.chdir(file_dir)
    # article = []
    # for root, dirs, files in os.walk(file_dir):
    #     article += files   # 当前路径下所有非目录子文件

    f_w = open(r'directionRe.txt','w',encoding='utf-8')
    # for file in article:
    list = []
    list2 = []
    split = []
    with open(r'../direciton.txt',encoding='utf-8') as f:
        for i in f:
            j = re.split('。|,|，', i)  # 正则按照句号和逗号的将句子拆分成短句子
            for jj in j:
                split.append(jj)

        for i in split:
            for j in v_list:
                for o in n_list:
                    if j in i and o in i :
                        list.append(i)
    # print(list)
    [list2.append(i) for i in list if not i in list2]
    for i in list2:
        f_w.write(i+"\n")
    f_w.close()
apply()