import numpy as np


def floyd(graph):
    n = len(graph)
    dist = graph

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i, j] > dist[i, k] + dist[k, j]:
                    dist[i, j] = dist[i, k] + dist[k, j]
    return dist


INF = float("inf")
graph = np.array([[0, INF, -2, INF], [4, 0, 3, INF], [INF, INF, 0, 2], [INF, -1, INF, 0]])
result = floyd(graph)
print(result)
