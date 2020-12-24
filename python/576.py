"""
option 1

iterate all possible paths

4^N -> infeasible

option2 

count the number of paths to each cell within N-1 times
than we can use paths to edges to get answer

corner : x2
not corner: x1

eg N=1

1 1
1 0

N = 0

0 1 0 => 2

N = 1

1 0 1 => 6

N = 2

0 2 0 => 4

----

N = 3

2 0 2 => 6

"""



class Solution:
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        
        MOD = 10**9 + 7
        
        board = [[0] * n for _ in range(m)]
        board[i][j] = 1
        
        R = len(board)
        C = len(board[0])
        
        ans = 0
        for _ in range(N):
            ans = (ans + self.count(board, R, C)) % MOD
            board = self.getNext(board, R, C)
            
        return ans
        
    def getNext(self, board, R, C):
        new_board = [[0] * C for _ in range(R)]
        
        
        deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        for r in range(R):
            for c in range(C):
                for d in deltas:
                    nr = r + d[0]
                    nc = c + d[1]
                    
                    if 0 <= nr < R and 0 <= nc < C:
                        new_board[nr][nc] += board[r][c]
                        
        return new_board
    
    def count(self, board, R, C):
        # boundary path
        ans = 0
        
        # top, bottom edge
        for c in range(C):
            ans += board[0][c]
            ans += board[R-1][c]
        
        # left, right edge
        for r in range(R):
            ans += board[r][0]
            ans += board[r][C-1]
            
        return ans
    
        
        
