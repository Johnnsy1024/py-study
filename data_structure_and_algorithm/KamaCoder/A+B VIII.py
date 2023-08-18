"""
输入：输入的第一行为一个整数N，接下来N行每行先输入一个整数M，然后在同一行内输入M个整数。
输出：对于每组输入，输出M个数的和，每组输出之间输出一个空行。

3
4 1 2 3 4
5 1 2 3 4 5
3 1 2 3

10

15

6
"""

import sys

for line in sys.stdin:
    tmp = line.split()
    if len(tmp) == 1:
        cnt = int(tmp[0])
        continue
    tmp = line.split()[1:]
    res = 0
    for i in tmp:
        res += int(i)
    print(res)
    if cnt > 1:
        print('')
    cnt -= 1