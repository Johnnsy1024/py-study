import os

cur_dir = os.path.dirname(os.path.abspath(__file__))

data_set_dir = os.path.join(cur_dir, 'src')
thuc_news_dir = os.path.join(data_set_dir, 'THUCNews')
thuc_train_path = os.path.join(thuc_news_dir, 'raw_data.txt')
thuc_dev_path = os.path.join(thuc_news_dir, 'dev.txt')
thuc_class_path = os.path.join(thuc_news_dir, 'class.txt')
thuc_vocab_path = os.path.join(thuc_news_dir, "vocab.pkl")

vocab_path = os.path.join(data_set_dir, "vocab.txt")
