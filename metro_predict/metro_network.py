import transbigdata as tbd
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd
import json
import os



if not os.path.exists('line.json'):
    line, stop = tbd.getbusdata('北京', ['10号线'])
    geometry = line['geometry'].to_json()
    with open('line.json', 'w', encoding='utf-8') as f:
        json.dump(geometry, f, ensure_ascii=False, indent=4)

with open('line.json', 'r', encoding='utf-8') as f: 
    line = json.loads(json.load(f))
    corrdinate = line['features'][0]['geometry']['coordinates']
    x = [i[0] for i in corrdinate]
    y = [i[1] for i in corrdinate]
    plt.figure(dpi=300)
    plt.plot(x, y, color='black')
    # print(line['bbox'])
    plt.show()
