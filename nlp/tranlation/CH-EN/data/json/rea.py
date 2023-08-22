import json

with open('ChineseNMT/data/json/train.json', 'r') as fp:
    f = json.load(fp)
    for i in f:
        print(i)