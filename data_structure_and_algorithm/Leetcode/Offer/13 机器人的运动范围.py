# def divide(num1, num2):
#     res = 0
#     while num1 > 0:
#         res += num1 % 10
#         num1 = num1 // 10
#     while num2 > 0:
#         res += num2 % 10
#         num2 = num2 // 10
#     return res

# direction = {(-1, 0), (1, 0), (0, 1), (0, -1)}
# def func(m, n, k):
#     cnt = 0
#     used = set()
#     def dfs(x, y, used: set):
#         if x < 0 or x >= m or y < 0 or y >= n:
#             # Cell is out of bounds, terminate the recursion
#             return 0
#         if divide(x, y) > k:
#             # Cell doesn't satisfy the condition, terminate the recursion
#             return 0
#         if (x, y) in used:
#             # Cell has already been visited, terminate the recursion
#             return 0

#         nonlocal cnt
#         # Count this cell as visited
#         cnt += 1
#         used.add((x, y))

#         for i, j in direction:
#             cnt += dfs(x + i, y + j, used)

#         used.discard((x, y))
#         return cnt

#     return dfs(0, 0, used)
# m = 3
# n = 2
# k = 17
# print(func(m, n, k))
def divide(num):
    res = 0
    while num > 0:
        res += num % 10
        num = num // 10
    return res

direction = {(-1, 0), (1, 0), (0, 1), (0, -1)}

def func(m, n, k):
    cnt = 0
    used = set()

    def dfs(x, y, used):
        if x < 0 or x >= m or y < 0 or y >= n:
            # Cell is out of bounds, terminate the recursion
            return 0
        if divide(x) + divide(y) > k:
            # Cell doesn't satisfy the condition, terminate the recursion
            return 0
        if (x, y) in used:
            # Cell has already been visited, terminate the recursion
            return 0

        nonlocal cnt  # Use the cnt variable from the outer function
        cnt += 1  # Count this cell as visited
        used.add((x, y))

        for i, j in direction:
            cnt += dfs(x + i, y + j, used)

        used.discard((x, y))
        return cnt

    return dfs(0, 0, used)

m = 3
n = 2
k = 17
print(func(m, n, k))
