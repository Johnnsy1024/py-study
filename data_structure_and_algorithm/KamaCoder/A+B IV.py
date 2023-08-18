"""
输入：每行的第一个数N，表示本行后面有N个数。

如果N=0时，表示输入结束，且这一行不要计算。

输出：对于每一行数据需要在相应的行输出和。

4 1 2 3 4
5 1 2 3 4 5
0 

10
15
"""

import sys

for line in sys.stdin:
    tmp, cnt = line.split()[1:], line.split()[0]
    if int(cnt) == 0:
        break
    res = 0
    for i in tmp:
        res += int(i)
    print(res)