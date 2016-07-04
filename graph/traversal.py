from collections import deque

def bfs(g, start=0):
	visited = {}
	q = deque([start])
	visited[start] = True
	
	while q:
		v = q.popleft()
		print(v)

		for nbr in g.neighbors(v):
			if nbr not in visited:
				q.append(nbr)
				visited[nbr] = True
				
def dfs(g, start=0):
	__dfs_a(g, start)

def __dfs_a(g, start=0):
	visited = {}
	stack = [start]

	while stack:
		v = stack.pop()
		if v not in visited:
			visited[v] = True
			print(v)
			for nbr in g.neighbors(v):
				stack.append(nbr)

def __dfs_b(g, start=0):
	visited = {}
	stack = [start]
	visited[start] = True
	print(start)

	while stack:
		v = stack.pop()
		for nbr in g.neighbors(v):
			if nbr not in visited:
				stack.append(v)
				stack.append(nbr)
				visited[nbr] = True
				print(nbr)
				break

from graph import undirected
__dfs_b(undirected)
