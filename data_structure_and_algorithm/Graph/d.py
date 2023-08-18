import random

def dijkstra(start : int, dis_matrix : list):
    nodes = [i+1 for i in range(len(dis_matrix))]
    distance = {node : float('inf') for node in nodes}
    distance[start] = 0
    visited = []
    
    while len(visited) < len(nodes):
        cur_node = min([node for node in nodes if node not in visited], 
                       key=lambda x: distance[x])
        visited.append(cur_node)
        for node in nodes:
            if dis_matrix[cur_node - 1][node - 1] != 'inf':
                distance[node] = min(distance[node], distance[cur_node] + dis_matrix[cur_node - 1][node - 1])
        
    return distance

D = [[0, 2, 3, 'inf', 'inf'],
     ['inf', 0, 'inf', 1, 4],
     ['inf', 'inf', 0, 'inf', 2],
     ['inf', 'inf', 'inf', 0, 5],
     ['inf', 'inf', 'inf', 'inf', 0]]

print(dijkstra(1, D))