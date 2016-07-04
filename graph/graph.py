import networkx as nx

def __gen_sample_graph():

	G1 = nx.DiGraph()
	edges = [(0, 1, 10), (0, 3, 20), (0, 4, 20), (0, 5, 5), (0, 6, 15),
			 (1, 2, 5), (1, 3, 10),
			 (2, 1, 15), (2, 3, 5),
			 (3, 4, 10),
			 (4, 5, 5),
			 (6, 5, 10),
			 (7, 0, 5), (7, 1, 20), (7, 6, 5),
			 (8, 1, 15), (8, 7, 20), (8, 9, 10),
			 (9, 1, 5), (9, 2, 15),
			]
	G1.add_weighted_edges_from(edges)


	G2 = nx.Graph()
	edges = [(0, 1, 4), (0, 7, 8),
			 (1, 2, 8), (1, 7, 11),
			 (2, 3, 7), (2, 5, 4), (2, 8, 2),
			 (3, 4, 9), (3, 5, 14),
			 (4, 5, 10),
			 (5, 6, 2),
			 (6, 7, 1), (6, 8, 6),
			 (7, 8, 7)
			]
	G2.add_weighted_edges_from(edges)	
	return G1, G2

directed, undirected = __gen_sample_graph()