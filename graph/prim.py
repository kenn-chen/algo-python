INF = 0x7FFFFFFF

def prim(g):
	V = g.number_of_nodes()
	parent = [0] * V
	key = [INF] * V
	mst = [0] * V
	parent[0], key[0] = -1, 0
	for i in range(V-1):
		min_dist = INF
		for k in range(V):
			if not mst[k] and key[k] < min_dist:
				min_dist, u = key[k], k
		mst[u] = True
		for v in g.neighbors(u):
			if not mst[v] and g[u][v]["weight"] < key[v]:
				key[v] = g[u][v]["weight"]
				parent[v] = u
	
	result = []
	for i in range(1, V): result.append((parent[i], i))
	return result