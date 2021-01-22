class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        self.R = len(board)
        self.C = len(board[0])
        
        board_start = board
        while True:
            marked_board = self.mark_crush(board_start)
            crushed_board = self.crush(marked_board)
            
            if self.is_equal(board_start, crushed_board):
                return crushed_board
            else:
                board_start = crushed_board
        
    def mark_crush(self, board):
        marked_board = self.copy_board(board)
        # find same candies horizontally
        for r in range(self.R):
            start = 0
            end = 0
            streak = 0
            while end < self.C:
                if board[r][start] == board[r][end]:
                    end += 1
                    streak += 1
                else:
                    if streak >= 3:
                        for i in range(start, end):
                            if i < self.C:
                                marked_board[r][i] = 0
                    start = end
                    streak = 0
            
            if streak >= 3:
                for i in range(start, self.C):
                    marked_board[r][i] = 0
                
        # find same candies vertically
        for c in range(self.C):
            start = 0
            end = 0
            streak = 0
            while end < self.R:
                if board[start][c] == board[end][c]:
                    end += 1
                    streak += 1
                else:
                    if streak >= 3:
                        for i in range(start, end):
                            if i < self.R:
                                marked_board[i][c] = 0
                    start = end
                    streak = 0
                    
            if streak >= 3:
                for i in range(start, self.R):
                    marked_board[i][c] = 0
                    
        return marked_board
    
    def crush(self, board):
        new_board = self.get_empty_board()

        for c in range(self.C):
            j = self.R-1
            for i in range(self.R-1, -1, -1):
                if board[i][c] == 0:
                    continue
                new_board[j][c] = board[i][c]
                j -= 1
        
        return new_board
        
    def get_empty_board(self):
        return [[0 for _ in range(self.C)] for _ in range(self.R)]
        
    def copy_board(self, board):
        empty_board = self.get_empty_board()
        for r in range(self.R):
            for c in range(self.C):
                empty_board[r][c] = board[r][c]
    
        return empty_board
        
    def is_equal(self, a, b):
        for r in range(self.R):
            for c in range(self.C):
                if a[r][c] != b[r][c]:
                    return False
        return True
        
