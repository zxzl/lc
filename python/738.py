"""
if input is monotonic -> follow
not monotonic?
decrement leftmost digit, and fill with 9

1332
133

123775
123699

126775
126699


"""

class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        
        # p marks the start of part which is not monotonic increase
        p = 0
        S = str(N)
        
        for i in range(1, len(S)):
            if int(S[p]) < int(S[i]):
                p = i
            elif int(S[p]) > int(S[i]):
                break
                
        if p == len(S) - 1:
            return N
        
        ans = [c for c in S]
        ans[p] = str(int(S[p]) - 1)
        for i in range(p+1, len(S)):
            ans[i] = "9"
        
        return int("".join(ans))
