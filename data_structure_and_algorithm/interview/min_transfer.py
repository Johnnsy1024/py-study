from collections import deque, defaultdict


def min_transfers(start, end, buses):
    graph = defaultdict(list)
    for bus in buses:
        src, dst = bus
        graph[src].append(dst)
        graph[dst].append(src)

    queue = deque([(start, 0)])
    visited = {start: 0}  # 既可以用来用来记录换乘次数，也可以作为已访问节点的列表，这里的换成次数本质上是距离

    while queue:
        #  将当前节点出队
        node, transfers = queue.popleft()
        #  如果出队的该节点即为目的地，则直接返回它的换乘次数
        if node == end:
            return transfers

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited[neighbor] = transfers + 1
                queue.append((neighbor, transfers + 1))

    return -1  # 如果无法到达目的地，返回-1


# 示例输入
start = 1
end = 4
buses = [[1, 3], [3, 4], [1, 5], [4, 5]]

# 调用函数并输出结果
result = min_transfers(start, end, buses)
print("最少换乘次数：", result)
