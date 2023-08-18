import sys
sys.path.append('/home/faizalfeng/study/dl/text_classify/text_classify/datas')
from path import *
import numpy as np
import pickle as pkl
from tqdm import tqdm

__all__ = ['DataLoader']


class DataPreparer:
    def __init__(self):
        self.thuc_train_path = thuc_train_path
        self.thuc_dev_path = thuc_dev_path
        self.vocab_save_path = thuc_vocab_path
        self.vocab_to_idx = self.trans_vocab_to_idx()

    def _load_sample(self, model='train', max_len=38):
        if model not in ['train', 'dev']:
            raise ValueError("model 只能是 train、dev其中的一种，请检查")
        if model == 'train':
            file_path = self.thuc_train_path
        else:
            file_path = self.thuc_dev_path
        if not os.path.exists(file_path):
            raise ValueError("文本不存在，请检查")
        texts = self._get_text(file_path)
        c2i = self.trans_vocab_to_idx(self.thuc_train_path, save_path=self.vocab_save_path)
        pad_id = c2i.get('[PAD]', 0)  # 得到pad在char_to_index中的index编号
        samples = []
        for line in tqdm(texts, desc="字符转index"):  # tqdm：提供一个进度条展示
            line_s = line.split('\t')
            if len(line_s) < 2:
                continue
            context, label = line_s[0], line_s[1]
            line_data = ([c2i.get(c, 1) for c in context]) + [pad_id] * (max_len - len(context))  # 将读取到的数据填充到最大长度
            line_data = line_data[:max_len]
            samples.append([line_data, int(label)])
        return samples

    def _shuffle_sample(self, raw_data) -> np.array:
        """ 打乱数据集并将feature和label分别返回 """
        shuffle_index = np.arange(len(raw_data))
        np.random.shuffle(shuffle_index)
        feature = np.array([raw_data[i][0] for i in range(len(raw_data))])
        label = np.array([raw_data[i][1] for i in range(len(raw_data))])
        feature = feature[shuffle_index]
        label = label[shuffle_index]
        return feature, label

    def trans_vocab_to_idx(self, file_path=thuc_train_path, max_chars=10000, min_freq=1, save_path=thuc_vocab_path):
        """
        获取训练数据的所有词汇对应的index
        :param file_path: 获取词汇的文件地址（默认为训练样本文件地址，即从训练样本中获取词汇）
        :param max_chars: 最大的词汇数量，即能保存的最大词汇量（默认为10000）
        :param min_freq:  最小词频，即少于这个词频的词语将会被剔除掉（默认为1）
        :param save_path: 词汇保存地址（这里的地址都是绝对地址）
        :return: 词汇表的字典 char to index
        """
        if os.path.exists(save_path):  # save_path已存在（即之前已经转化好），则直接load
            with open(save_path, 'rb') as fp:
                c2i = pkl.load(fp)
            return c2i
        texts = self._get_text(file_path)
        char_num = self._cal_char_num(texts)
        char_sort = sorted(char_num.items(), key=lambda x: x[1], reverse=True)  # 按字符出现次数从大到小排列
        char_sort = [item for item in char_sort if item[1] >= min_freq]  # 抛弃一次都没出现过的字符
        char_sort = char_sort[:max_chars]  # 取前max_chars个字
        chars = ['[PAD]', '[UNK]'] + [item[0] for item in char_sort]
        c2i = {c: i for i, c in enumerate(chars)}
        with open(save_path, 'wb') as fp:
            pkl.dump(c2i, fp)
        return c2i

    def _get_text(self, file_path) -> list:
        """
        从源词汇文件中获得所有的句子和标签，打包为列表套列表的格式
        :return: 句子和标签打包列表（二维列表格式）
        """
        tmp = os.path.exists(file_path)
        if not os.path.exists(file_path):
            raise ValueError("文本不存在，请检查")
        with open(file_path, 'r', encoding='utf-8') as f:
            texts = f.read().split("\n")
            texts = [item.strip() for item in texts if len(item) > 0]
        return texts

    def _cal_char_num(self, texts) -> dict:
        """
        :param texts: 句子和标签打包列表（二维列表格式）
        :return: char_dict：字符个数记录
        """
        char_dict = {}  # char_dict记录各字符出现的次数
        for line in texts:
            line_s = line.split('\t')
            if len(line_s) < 2:  # 如果当前句子没有对应的分类，则抛弃掉
                continue
            context, _ = line_s[0], line_s[1]  # 由于训练集存储格式为 data_text \t lable
            for char in context:
                char_dict[char] = char_dict.get(char, 0) + 1  # dict.get(item, default_value)从字典中取char，如果没取到则返回0
        return char_dict

    def trans_class_to_idx(self):
        """
        :return:
        """
        if not os.path.exists(thuc_class_path):
            raise ValueError("类别文本不存在，请检查！")
        with open(thuc_class_path, 'r', encoding='utf-8') as f:
            texts = f.read().split("\n")
            texts = [str(item).strip() for item in texts if len(str(item).strip()) > 0]
        c2i = {class_: i for i, class_ in enumerate(texts)}
        return c2i


class DataLoader(DataPreparer):

    def __init__(self, model='train', max_seq_len=38, batch_size=32):
        super().__init__()
        self.sample = self._load_sample(model, max_seq_len)
        self.feature, self.label = self._shuffle_sample(self.sample)

        self.batch_size = batch_size
        self.batch_num = len(self.sample) // self.batch_size
        self.residual = (len(self.sample) % self.batch_size != 0)

        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= self.batch_num:
            self.index = 0  # 计数置0方便下一次可能的调用
            raise StopIteration
        if self.index == self.batch_num - 1 and self.residual:
            feature = self.feature[self.index * self.batch_size: len(self.feature)]
            label = self.label[self.index * self.batch_size: len(self.label)]
            self.index += 1
            return feature, label
        else:
            feature = self.feature[self.index * self.batch_size: (self.index + 1) * self.batch_size]
            label = self.label[self.index * self.batch_size: (self.index + 1) * self.batch_size]
            self.index += 1
            return feature, label

    def __len__(self):
        """
        :return: 返回批次
        """
        if self.residual:
            return self.batch_num + 1
        else:
            return self.batch_num
