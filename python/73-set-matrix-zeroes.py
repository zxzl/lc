"""
constant space solution: let's store info in the array

1) find first row that has 0, and set that row as 0
2) in each element in that row, store whether that column has 0 

"""

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        

        """
        Do not return anything, modify matrix in-place instead.
        """
        R = len(matrix)
        if R == 0:
            return
        C = len(matrix[0])

        memo_row = -1
        memo_col = -1
        
        for r in range(R):
            for c in range(C):
                if matrix[r][c] == 0:
                    memo_row = r
                    memo_col = c
                    break
            if memo_row != -1:
                break
                    
        if memo_row == -1:
            return
                    
        for r in range(R):
            for c in range(C):
                if matrix[r][c] == 0:
                    matrix[memo_row][c] = 0
                    matrix[r][memo_col] = 0
        
        # fill zero according to memos
        for r in range(R):
            for c in range(C):
                if r == memo_row or c == memo_col:
                    continue
                if matrix[memo_row][c] == 0 or matrix[r][memo_col] == 0:
                    matrix[r][c] = 0
        
        for r in range(R):
            matrix[r][memo_col] = 0
        for c in range(C):
            matrix[memo_row][c] = 0
            

                    
            
            
                    
