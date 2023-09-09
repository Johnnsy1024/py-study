import sys
import os

"""
解决vscode中python路径问题的方法
"""

os.chdir(sys.path[0])
print(os.getcwd())
p = sys.path[0]

with open('test.txt', 'r') as f:
    print(f.readline())
    
print('Hello Mac World')