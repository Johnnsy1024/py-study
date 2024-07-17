from collections import deque
from typing import List


def dijkstra(graph: dict, start: str):
    nodes = list(graph)
    visited = []
    distance = {i: float("inf") for i in nodes}
    distance[start] = 0

    while len(visited) < len(nodes):
        cur_node = min(
            [node for node in nodes if node not in visited], key=lambda x: distance[x]
        )
        visited.append(cur_node)
        for i in graph[cur_node]:
            if distance[i] > graph[cur_node][i] + distance[cur_node]:
                distance[i] = graph[cur_node][i] + distance[cur_node]
    return distance


def floyd(graph: list):
    nodes = list(range(len(graph[0])))
    for k in nodes:
        for i in nodes:
            for j in nodes:
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
    return graph


def numIslands(grid: List[List[str]]):
    if not grid:
        return 0

    def bfs(start_i, start_j, used: set):
        res = []
        q = deque([(start_i, start_j)])
        res.append([(start_i, start_j)])
        while q:
            i, j = q.popleft()
            for add_i, add_j in direction:
                new_i, new_j = i + add_i, j + add_j
                if (
                    0 <= new_i < m
                    and 0 <= new_j < n
                    and (new_i, new_j) not in used
                    and grid[new_i][new_j] == "1"
                ):
                    q.append((new_i, new_j))
                    res.append((new_i, new_j))
                    used.add((new_i, new_j))
        return res

    res = 0
    direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    m = len(grid)
    n = len(grid[0])
    used = set()
    for i in range(m):
        for j in range(n):
            if (i, j) not in used and grid[i][j] == "1":
                bfs(i, j, used)
                res += 1
    return res


def numIslands_2(grid: List[List[str]]):

    cnt = 0
    x_scale = len(grid)
    y_scale = len(grid[0])

    def dfs(x, y):
        # 如果格子上是1，则把其标记为已探索，否则
        if grid[x][y] == "1":
            grid[x][y] = "0"
        else:
            return
        for add_x, add_y in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            if 0 <= x + add_x < x_scale and 0 <= y + add_y < y_scale:
                dfs(x + add_x, y + add_y)

    for x in range(x_scale):
        for y in range(y_scale):
            if grid[x][y] == "1":
                dfs(x, y)
                cnt += 1
    return cnt


if __name__ == "__main__":
    # graph = {
    #     "A": {"B": 5, "C": 3},
    #     "B": {"A": 5, "C": 1, "D": 2},
    #     "C": {"A": 3, "B": 1, "D": 6},
    #     "D": {"B": 2, "C": 6},
    # }
    # print(dijkstra(graph, "A"))
    # INF = float("inf")
    # print(floyd([[0, INF, -2, INF], [4, 0, 3, INF], [INF, INF, 0, 2], [INF, -1, INF, 0]]))
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
    print(numIslands_2(grid))
