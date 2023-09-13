# %%
from sklearn.cluster import KMeans
import numpy as np 
# %%
k = KMeans()
data = np.random.random(size=(100))*100
data
# %%
k.fit(data.reshape((-1, 1)))
k
# %%
res = k.predict(data.reshape((-1, 1)))
res
# %%
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# 创建一个均值为0，标准差为1的正态分布
mean = 0
std_dev = 1
x = np.linspace(mean - 3 * std_dev, mean + 3 * std_dev, 100)  # 生成x轴的数据
pdf = norm.pdf(x, mean, std_dev)  # 计算概率密度函数
plt.rcParams['font.family'] = ['Arial Unicode MS']
# 绘制正态分布的概率密度函数图表
plt.plot(x, pdf， color='blue')
# plt.xlabel('随机变量')
# plt.ylabel('概率密度')
plt.title('正态分布图表')
plt.legend()
plt.grid(True)
plt.show()

# %%
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# 创建一个均值为0，标准差为1的正态分布
mean = 0
std_dev = 1
x = np.linspace(mean - 3 * std_dev, mean + 3 * std_dev, 100)  # 生成x轴的数据
pdf = norm.pdf(x, mean, std_dev)  # 计算概率密度函数

# 绘制正态分布的概率密度函数图表
plt.plot(x, pdf, label='正态分布', color='blue')


# 找到最高点的坐标
max_point = (x[np.argmax(pdf)], np.max(pdf))

# 添加箭头指向最高点
plt.annotate('较优值', max_point, xytext=(20, 0), textcoords='offset points',
             arrowprops=dict(arrowstyle='->', color='red'))

# 隐藏网格和x、y轴标签
plt.grid(False)
plt.xticks([])
plt.yticks([])

plt.show()

# %%
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# 创建一个均值为0，标准差为1的正态分布
mean = 0
std_dev = 1
x = np.linspace(mean - 3 * std_dev, mean + 3 * std_dev, 1000)  # 生成x轴的数据
pdf = norm.pdf(x, mean, std_dev)  # 计算概率密度函数

# 绘制正态分布的概率密度函数图表
plt.plot(x, pdf, label='Distribution', color='blue')
plt.title('Example')

# 找到峰值位置
peak_location = x[np.argmax(pdf)]
cut_off_range = 0.5  # 截取点范围的宽度，可以根据需要调整

# 绘制截取点范围
plt.axvline(x=peak_location - cut_off_range / 2, color='red', linestyle='--', label='Left Range')
plt.axvline(x=peak_location + cut_off_range / 2, color='green', linestyle='--', label='Right Range')

# 隐藏网格和x、y轴标签
plt.grid(False)
plt.xlabel('Interval')
plt.ylabel('Distribution')
plt.xticks([])
plt.yticks([])

plt.legend()
# plt.show()
plt.savefig('distribution_example.png',dpi=400)
# %%
