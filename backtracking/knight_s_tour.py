N = 8
moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
board = [[-1]*N for _ in range(N)]

def isvalid(x, y):
	return 0<=x<N and 0<=y<N and board[x][y]==-1

def solved(x, y, count):
	if count == N**2: return True

	for move in moves:
		next_x, next_y = x+move[0], y+move[1]
		if isvalid(next_x, next_y):
			board[next_x][next_y] = count
			if solved(next_x, next_y, count+1):
				return True
			else:
				board[next_x][next_y] = -1 #backtracking
	return False

if __name__ == "__main__":
	board[0][0] = 0
	solved(0, 0, 1)
	print(board)
