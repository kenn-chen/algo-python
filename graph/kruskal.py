import networkx as nx
from union_find import UnionFind

def kruskal(g):
	V = g.number_of_nodes()
	edges = sorted(g.edges(data="weight"), key=lambda x: x[2])
	uf = UnionFind(V)
	mst = [0] * (V-1)

	e = i = 0
	while e < V-1:
		edge = edges[i]
		src, des, _ = edge
		if uf.find(src) != uf.find(des):
			uf.union(src, des)
			mst[e] = (src, des)
			e += 1
		i += 1
		
	return mst