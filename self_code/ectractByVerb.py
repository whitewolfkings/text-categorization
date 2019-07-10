# -*- coding: utf-8 -*-
import re

class extractByVerbOfPredict(): #预测的时候按照词性表进行提取句子

    def analisis(self,file):
        v_list = ['新增', '添加', '增加', '提供', '修改', '变更', '调整', '更新', '优化', '改造', '改为', '扩展', '扩容', '扩长', '作废', '取消', '屏蔽',
                  '去除', '去掉', '删除', '累加', '支持']
        n_list = ['页面', '按钮', '接口', '字段', '表', '功能', '条件', '规则', '校验', '工具', '模板', '提醒', '提示', '判断', '选项', '权限', '标记',
                  '标志','参数', '状态', '复选框', '格式', '工具', '限制', '查询', '方式']
        list = []
        list2 = []
        split = []
        with open(file, encoding='utf-8') as f:
            # 现在需要在这里根据逗号或者句号进行短文本的处理。
            for i in f:
                j = re.split('。|,|，', i)  # 正则按照句号和逗号的将句子拆分成短句子
                for jj in j:
                    split.append(jj)  # 将拆分的句子添加到列表里面

            for i in split:
                for j in v_list:
                    for o in n_list:
                        if j in i and o in i:
                            list.append(i)
            [list2.append(i) for i in list if not i in list2]
        return list2
    def apply(self):
        pass

    def explain(self,file):
        pass
    def explain(self):
        v_list = ['新增', '添加', '增加', '提供', '修改', '变更', '调整', '更新', '优化', '改造', '改为', '扩展', '扩容', '扩长', '作废', '取消', '屏蔽',
                  '去除', '去掉', '删除', '累加', '支持']
        n_list = ['页面', '按钮', '接口', '字段', '表', '功能', '条件', '规则', '校验', '工具', '模板', '提醒', '提示', '判断', '选项', '权限', '标记',
                  '标志',
                  '参数', '状态', '复选框', '格式', '工具', '限制', '查询', '方式']

        f_w = open(r'../data/explainDataByVAndN.txt', 'w', encoding='utf-8')
        list = []
        list2 = []
        split = []
        with open(r'../data/reMatchExplainData.txt', encoding='utf-8') as f:
            # 现在需要在这里根据逗号或者句号进行短文本的处理。
            for i in f:
                j = re.split('。|,|，', i)  # 正则按照句号和逗号的将句子拆分成短句子
                '''
                这里需要将数据里面的无用的字符过滤掉
                正则不适用的话就试试if判断吧
                如:将数据前面的小标题，什么F.1.1之类的数据过滤掉
                '''
                for jj in j:
                    split.append(jj)  # 将拆分的句子添加到列表里面

            for i in split:
                for j in v_list:
                    for o in n_list:
                        if j in i and o in i:
                            list.append(i)
            # print(list)
            [list2.append(i) for i in list if not i in list2]
            for i in list2:
                f_w.write(i.strip() + '\n')
        f_w.close()



# precoss = extractByVerbOfPrecoss()
# precoss.analisis()
# precoss.apply()
# precoss.explain()

