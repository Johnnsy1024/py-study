def func(x: int):
    l = [int(list(str(x))[i]) for i in range(len(list(str(x))))]
    
    if sum(l) % 2 != 0:
        return 'No'
    
    target = sum(l) // 2
    
    def dfs(arr: list, tmp: list, visited: list):
        if sum(tmp) > target:
            return False
        if sum(tmp) == target:
            return True
        res = False
        for i in range(len(arr)):
            if arr[i] in visited:
                continue
            visited.append(arr[i])
            tmp.append(arr[i])
            res = dfs(arr, tmp, visited)
            if res:
                return True
            tmp.pop()
            visited.pop()
        return False
    
    return dfs(l, [], [])

print(func(116))