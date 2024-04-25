def flyod(graph):
    n = len(graph)
    dist = graph
    prev = [[i for i in range(1, n+1)] for _ in range(n)]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    prev[i][j] = k
    return dist, prev

INF = float('inf')
graph = [
    [0, 5, INF, 10],
    [INF, 0, 3, INF],
    [INF, INF, 0, 1],
    [INF, INF, INF, 0]
]
res1, res2 = flyod(graph)
print(res1, res2)