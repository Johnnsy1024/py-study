"""深度优先算法用栈实现（后入先出）"""
"""python中的栈可以通过list实现"""


def dfs_search(graph: dict, start, target):
    #  创建一个已访问集合储存已访问的节点
    #  创建已访问节点的意义在于，一个节点其周围的邻接点只能入栈一次，被搜索过的点不会再被搜索
    visited = set()
    #  将起点入栈
    stack = [start]

    while stack:  # 栈不为空时代表所有的点还没有搜索完毕
        node = stack.pop()

        if node == target:
            return True

        if node not in visited:
            visited.add(node)
            for i in graph[node]:
                stack.append(i)
    return False


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'A'],
    'D': [],
    'E': ['F'],
    'F': []
}
start = 'A'
target = 'D'
print(dfs_search(graph, start, target))
