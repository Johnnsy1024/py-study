import jieba
import pickle as pkl


def one_gram_cut(file_path, max_vocab_size):
    with open(file_path, 'r') as fp:
        tmp = fp.readlines()
    tmp = [i.split('\t') for i in tmp]
    feature = [i[0] for i in tmp]
    vocab = []
    for fea in feature:
        vocab.extend(jieba.lcut(fea))
    vocab = ['PAD', 'UNK'] + list(set(vocab))
    vocab = {i: idx for idx, i in enumerate(vocab[:max_vocab_size])}
    with open('vocab.pkl', 'wb') as fp:
        pkl.dump(vocab, fp)


one_gram_cut('/home/faizalfeng/study/dl/NLP/text_classify/datas/src/THUCNews/raw_data.txt', 50000)
