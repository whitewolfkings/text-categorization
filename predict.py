# coding: utf-8

from __future__ import print_function

import re
import os
import tensorflow as tf
import tensorflow.contrib.keras as kr

from cnn_model import TCNNConfig, TextCNN
from rnn_model import TRNNConfig, TextRNN
from data.cnews_loader import read_category, read_vocab

from self_code.ectractByVerb import extractByVerbOfPredict
from data.extractFunctionDataOfPredict import reExtractAnalysisSheetOfPredict,reExtractExplainSheetOfPredict

try:
    bool(type(unicode))
except NameError:
    unicode = str

base_dir = 'data/cnews'
vocab_dir = os.path.join(base_dir, 'cnews.vocab.txt')

save_dir = 'checkpoints/textcnn'
# save_dir_rnn = 'checkpoints/textrnn'
save_path = os.path.join(save_dir, 'best_validation')  # 最佳验证结果保存路径


class CnnModel:
    def __init__(self):
        self.config = TCNNConfig()
        self.categories, self.cat_to_id = read_category()
        self.words, self.word_to_id = read_vocab(vocab_dir)
        self.config.vocab_size = len(self.words)
        self.model = TextCNN(self.config)

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

        y_pred_cls = self.session.run(self.model.y_pred_cls,feed_dict=feed_dict)
        # print(predict)
        # print(y_pred_cls)
        # label = ['ei','eo','eq','ilf']
        # for i in range(len(label)):
        #     print('标签',label[i],'预测的概率是：{:.4f}%'.format(predict[0][i]*100))
        # print('预测的概率是：{:.4f}%'.format((i*100) for i in predict[0]))
        # print('预测的标签是：',self.categories[y_pred_cls[0]])
        # print('预测的概率是：',predict[0][y_pred_cls[0]])
        # return '预测的标签是:',self.categories[y_pred_cls[0]],'预测的概率是：',predict[0][y_pred_cls[0]]
        return self.categories[y_pred_cls[0]]

    def out(self, list, result_out):
        with open(result_out, 'w', encoding='utf-8') as file:
            for i in list:
                file.write(i.strip() + '\t' + cnn_model.predict(i) + '\n')


if __name__ == '__main__':
    cnn_model = CnnModel()
    file = r'CAMS_业务需求分析单_银川招标易项目相关优化需求.docx.txt'

    if "分析单" in file:
        file_out = 'predictAnalysisData_cnn.txt'
        result_out = 'predictAnalysis_cnn.txt'
        file_out = reExtractAnalysisSheetOfPredict(file,file_out) #将正则匹配到的数据输出到fileout文件上。
    else:
        file_out = 'predictExplainData_cnn.txt'
        result_out = 'predictExplain_cnn.txt'
        file_out = reExtractExplainSheetOfPredict(file, file_out)
    list2 = extractByVerbOfPredict().analisis(file_out)  #分析单和说明书的分析流程是一样的。
    cnn_model.out(list2, result_out)
