"""广度优先搜索用队列数据结构实现"""
from queue import Queue
"""一层一层，抽丝剥茧"""
def bfs(start_node, target, graph):
    #  创建队列
    q = Queue()
    nodes = list(graph.keys())
    #  创建已访问字典，该字典同时记录了搜索到的节点之间的前序后续信息
    prev = {start_node: None}
    q.put(start_node)
    while not q.empty(): # 记录有没有把相邻的数遍历完
        explore_node = q.get()
        if explore_node == target:
            path = []
            while explore_node is not None:
                path.append(explore_node)
                explore_node = prev[explore_node]
            return path[::-1]
        for n in graph[explore_node]:
            if n not in prev:
                q.put(n)
                prev[n] = explore_node

graph = {
    "A": ["B","C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D","E"],
    "D": ["B", 'C', "E", "F"],
    "E": ["C", "D"],
    "F": ["D"]
}
print(bfs('A', 'E', graph))