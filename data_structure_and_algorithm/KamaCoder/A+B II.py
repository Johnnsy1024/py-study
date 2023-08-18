"""
输入：第一行是一个整数N，表示后面会有N行a和b，通过空格隔开。
输出：对于输入的每对a和b，你需要在相应的行输出a、b的和。
如第二对a和b，对应的和也输出在第二行。


2
2 4
9 21

6
30
"""


import sys

for line in sys.stdin:
    tmp = line.split()
    if len(tmp) != 2:
        continue 
    print(int(tmp[0])+int(tmp[1]))