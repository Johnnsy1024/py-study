
# If you need to import additional packages or classes, please import here.

def func():
    m, n = map(int, input().strip().split())
    mat = []
    for i in range(m):
        tmp = [int(j) for j in input().strip().split()]
        mat.append(tmp)
    res = 0
    direction = {(-1,0),(1,0),(0,1),(0,-1)}
    result = []
    used = set()
    def dfs(i, j, res):
        if i < 0 or j < 0 or i > m - 1 or j > n - 1 or mat[i][j]==0:
            return 
        if j == n-1 and i>=0 and i < m:
            res += 1
            return res
        res += 1
        for x, y in direction:
            nx, ny = i + x, j + y
            if (nx, ny) in used:
                continue
            used.add((nx, ny))
            if dfs(nx, ny, res):
                result.append(res)
            used.discard((nx, ny))
    for k in range(m):
        res = 0
        if mat[k][0]==1:
            dfs(k, 0, res)
            
    if not result:
        return -1
    else:
        return min(result)
                    
                    
                
    #for i in range(m):
        #mat.append(input().strip().split())
    # please define the python3 input here. For example: a,b = map(int, input().strip().split())
    # please finish the function body here.
    # please define the python3 output here. For example: print().

if __name__ == "__main__":
    print(func())
