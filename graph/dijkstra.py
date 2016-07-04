INF = 0x7FFFFFFF

def dijkstra(g, src):
	V = g.number_of_nodes()
	dist = [INF] * V
	spt = [0] * V

	dist[src] = 0
	for i in range(V):
		min_dist = INF
		for k in range(V):
			if not spt[k] and dist[k] < min_dist:
				min_dist, u = dist[k], k
		if u == None: break
		spt[u] = True

		for v in g.neighbors(u):
			if not spt[v]:
				dist[v] = min(dist[v], dist[u]+g[u][v]["weight"])

	return [-1 if x==INF else x for x in dist]
