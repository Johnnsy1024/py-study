import sys

for idx, line in enumerate(sys.stdin):
    a = line.split()
    if idx == 0:
        str_len, int_len = int(a[0]), int(a[1])
        
    