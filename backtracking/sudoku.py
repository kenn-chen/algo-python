class Solution(object):
    def build_cache(self, board):
        self.row = [[1]*10 for i in range(9)]
        self.col = [[1]*10 for i in range(9)]
        self.box = [[[1]*10 for i in range(3)] for j in range(3)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    num = int(board[i][j])
                    self.row[i][num] = 0
                    self.col[j][num] = 0
                    self.box[i//3][j//3][num] = 0

    def isvalid(self, board, x, y, num):
        return self.row[x][num] and self.col[y][num] and self.box[x//3][y//3][num]
    
    def move(self, board, x, y):
        x, y = (x, y+1) if y < 8 else (x+1, 0)
        while x<9 and board[x][y] != ".":
            x, y = (x, y+1) if y < 8 else (x+1, 0)
        return x, y

    def solved(self, board, x, y):
        if x == 9: return True
        
        for num in range(1, 10):
            if self.isvalid(board, x, y, num):
                board[x][y] = str(num)
                self.row[x][num] = self.col[y][num] = self.box[x//3][y//3][num] = 0
                next_x, next_y = self.move(board, x, y)
                if self.solved(board, next_x, next_y):
                    return True
                else:
                    board[x][y] = '.'
                    self.row[x][num] = self.col[y][num] = self.box[x//3][y//3][num] = 1
        return False
        
    def solveSudoku(self, board):
        self.build_cache(board)
        start_x, start_y = 0, 0
        if board[0][0] != ".":
            start_x, start_y = self.move(board, start_x, start_y)

        return self.solved(board, start_x, start_y)


def print_sudoku(board):
    for i in range(9):
        print ' '.join([x for x in board[i]])

if __name__ == "__main__":
    board = [
                ["5", "3", ".", ".", "7", ".", ".", ".", "."],
                ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                [".", "9", "8", ".", ".", ".", ".", "6", "."],
                ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                [".", "6", ".", ".", ".", ".", "2", "8", "."],
                [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                [".", ".", ".", ".", "8", ".", ".", "7", "9"]
            ]
    s = Solution()
    print s.solveSudoku(board)
    print_sudoku(board)