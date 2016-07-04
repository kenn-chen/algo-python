N = 10
total = 0
board = [[0]*N for i in range(N)]

def clear(start_line):
	global board
	if start_line == 0:
		board = [[0]*N for i in range(N)]
	else:
		for i in range(start_line, N):
			board[i] = [0] * N

def isvalid(pos):
	for i in range(pos[0]):
		if board[i][pos[1]] == 1:
			return False
	for i in range(1, pos[0]+1):
		if pos[1]-i < 0: break
		if board[pos[0]-i][pos[1]-i] == 1:
			return False
	for i in range(1, pos[0]+1):
		if pos[1]+i > N-1: break
		if board[pos[0]-i][pos[1]+i] == 1:
			return False
	return True

def solved(pos):
	global total
	if pos[0] == N-1:
		total += 1
		return True

	success = False
	for y in range(N):
		des = (pos[0]+1, y)
		if isvalid(des):
			board[des[0]][des[1]] = 1
			if solved(des):
				success = True
				clear(des[0])
			else:
				board[des[0]][des[1]] = 0
	return success

if __name__ == "__main__":
	for i in range(N):
		start = (0, i)
		board[0][i] = 1
		solved(start)
		clear(0)
	print(total)