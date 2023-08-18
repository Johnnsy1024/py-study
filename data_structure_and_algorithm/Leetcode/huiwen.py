from collections import deque

def find(string : str):
    q = deque(string)
    flag = True
    if len(q) % 2 == 0:
        while q:
            l, r = q.popleft(), q.pop()
            if l != r:
                flag = False
                return flag
        return flag
    else:
        while q and len(q) != 1:
            l, r = q.popleft(), q.pop()
            if l!= r:
                flag = False
                return flag
        return flag
            
string = 'sdfpds'
print(find(string=string))