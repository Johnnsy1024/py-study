"""
输入：输入中每行是一对a和b。其中会有一对是0和0标志着输入结束，且这一对不要计算。
输出：对于输入的每对a和b，你需要在相应的行输出a、b的和。
如第二对a和b，他们的和也输出在第二行。

2 4
11 19
0 0

6
30
"""

import sys

for line in sys.stdin:
    tmp = line.split()
    if int(tmp[0]) == int(tmp[1]) == 0:
        break
    print(int(tmp[0]) + int(tmp[1]))