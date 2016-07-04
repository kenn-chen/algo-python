import networkx as nx
import numpy as np

INF  = 0x7FFFFFFF
 
def floyd_warshall(g):
    V = g.number_of_nodes()
    dist = nx.adjacency_matrix(g).toarray()
    dist[dist==0] = INF
    np.fill_diagonal(dist, 0)

    for k in range(V):
        for i in range(V):
            if dist[i][k] == INF: continue
            for j in range(V):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    dist[dist==INF] = -1
    return dist