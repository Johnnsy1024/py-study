import sys
import os

"""
解决vscode中python路径问题的方法
"""

os.chdir(sys.path[0])
print(os.getcwd())

with open('test.txt', 'r') as f:
    print(f.readline())
    
os.chdir('../')
print(os.getcwd())

with open('test.txt', 'r') as f:
    print(f.readline())