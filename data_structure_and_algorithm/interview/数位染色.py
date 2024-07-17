"""
小红拿到了一个正整数x。她可以将其中一些数位染成红色。然后她想让所有染红的数位数字之和等于没染色的数位数字之和。
她不知道能不能达成目标。你能告诉她吗？
"""


def func(x: int):
    l = [int(list(str(x))[i]) for i in range(len(list(str(x))))]

    if sum(l) % 2 != 0:
        return "No"

    target = sum(l) // 2

    def dfs(arr: list, tmp: list, visited: set):
        if sum(tmp) > target:
            return False
        if sum(tmp) == target:
            return True
        res = False
        for i in range(len(arr)):
            if arr[i] in visited:
                continue
            visited.add(arr[i])
            tmp.append(arr[i])
            res = dfs(arr, tmp, visited)
            if res:  # 如果一找到true,则层层向上传递true,结束栈底所有进程
                return True
            tmp.pop()
            visited.discard(arr[i])
        return res

    return dfs(l, [], set())


print(func(123))
