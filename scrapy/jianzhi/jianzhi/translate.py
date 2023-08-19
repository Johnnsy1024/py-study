import json

with open('jianzhi/jianzhi/result/result_current_missions_2023-08-13 15:09:19.json', 'r') as fp:
    txt = json.load(fp)
    with open('jianzhi/jianzhi/current_mission/current.txt', 'w+') as f:
        for t in txt:
            title = t['title'][0]
            desc = t['desc'][0]
            content = t['content']
            f.write(title)
            f.write('\n')
            f.write('\n')
            f.write(desc)
            f.write('\n')
            f.write('\n')
            f.write(content)
            f.write('\n')
            f.write('\n')

with open('jianzhi/jianzhi/result/result_future-missions_2023-08-13 15:09:27.json', 'r') as fp:
    txt = json.load(fp)
    with open('jianzhi/jianzhi/current_mission/future.txt', 'w+') as f:
        for t in txt:
            title = t['title'][0]
            desc = t['desc'][0]
            content = t['content']
            f.write(title)
            f.write('\n')
            f.write('\n')
            f.write(desc)
            f.write('\n')
            f.write('\n')
            f.write(content)
            f.write('\n')
            f.write('\n')

with open('jianzhi/jianzhi/result/result_past-missions_2023-08-13 15:09:33.json', 'r') as fp:
    txt = json.load(fp)
    with open('jianzhi/jianzhi/current_mission/past.txt', 'w+') as f:
        for t in txt:
            title = t['title'][0]
            desc = t['desc'][0]
            content = t['content']
            f.write(title)
            f.write('\n')
            f.write('\n')
            f.write(desc)
            f.write('\n')
            f.write('\n')
            f.write(content)
            f.write('\n')
            f.write('\n')
            
        