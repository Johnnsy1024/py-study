"""
输入：输入包含若干行，每行输入两个整数a和b，由空格分隔。

输出：对于每组输入，输出a和b的和，每行输出后接一个空行。

2 4
11 19

6

30


"""

import sys

for line in sys.stdin:
    a = line.split()
    print(int(a[0])+int(a[1]))
    print('')