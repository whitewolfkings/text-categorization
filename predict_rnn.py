# coding: utf-8

from __future__ import print_function

import os
import tensorflow as tf
import tensorflow.contrib.keras as kr
from rnn_model import TRNNConfig, TextRNN
from data.cnews_loader import read_category, read_vocab
from data.extractFunctionDataOfPredict import reExtractAnalysisSheetOfPredict,reExtractExplainSheetOfPredict
from self_code.ectractByVerb import extractByVerbOfPredict


try:
    bool(type(unicode))
except NameError:
    unicode = str

base_dir = 'data/cnews'
vocab_dir = os.path.join(base_dir, 'cnews.vocab.txt')

save_dir = 'checkpoints/textrnn'
save_path = os.path.join(save_dir, 'best_validation')  # 最佳验证结果保存路径


class RnnModel:
    def __init__(self):
        self.config = TRNNConfig()
        self.categories, self.cat_to_id = read_category()
        self.words, self.word_to_id = read_vocab(vocab_dir)
        self.config.vocab_size = len(self.words)
        self.model = TextRNN(self.config)

        self.session = tf.Session()
        self.session.run(tf.global_variables_initializer())
        saver = tf.train.Saver()
        saver.restore(sess=self.session, save_path=save_path)  # 读取保存的模型

    def predict(self, message):
        # 支持不论在python2还是python3下训练的模型都可以在2或者3的环境下运行
        content = unicode(message)
        data = [self.word_to_id[x] for x in content if x in self.word_to_id]

        feed_dict = {
            self.model.input_x: kr.preprocessing.sequence.pad_sequences([data], self.config.seq_length),
            self.model.keep_prob: 1.0
        }

        y_pred_cls = self.session.run(self.model.y_pred_cls, feed_dict=feed_dict)
        return self.categories[y_pred_cls[0]]

    def out(self, list, result_out):
        with open(result_out, 'w', encoding='utf-8') as file:
            for i in list:
                file.write(i.strip() + '\t' + rnn_model.predict(i) + '\n')


if __name__ == '__main__':
    rnn_model = RnnModel()
    file = r'D:\工作\光大银行\样本数据\样本数据\pkdata\业务分析单txt\EPAMS-总行综合管理系统-业务需求分析单R17040837.doc.txt'

    if "分析单" in file:
        # print('111111111111111')
        file_out = 'predictAnalysisData_rnn.txt'
        result_out = 'predictAnalysis_rnn.txt'
        file_out = reExtractAnalysisSheetOfPredict(file, file_out)  # 将正则匹配到的数据输出到fileout文件上。
    else:
        # print('22222222222222222222')
        file_out = 'predictExplainData_rnn.txt'
        result_out = 'predictExplain_rnn.txt'
        file_out = reExtractExplainSheetOfPredict(file, file_out)
    # print(file_out)
    list2 = extractByVerbOfPredict().analisis(file_out)  # 分析单和说明书的分析流程是一样的。
    rnn_model.out(list2, result_out)
    #test_demo = ['录入订单',#ei
                 #'修改订单',#ei
                 #'查询订单',#eo
                 #'汇率查询转换系统',#eif
                # '订单和客户',#ilf
                #'统计订单']#eq
    #for i in test_demo:
       # print(rnn_model.predict(i))
