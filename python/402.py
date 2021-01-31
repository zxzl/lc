"""
k=1

12345 -> 2345,1345,1245,1235,1234 -> 1234
12543 -> 2543,1543,1243,1253,1254 -> 1243
54321 -> 4321

observation
* to remove k digits, we can keep removing 1 digits
* when removing 1 digits, remove when the digit decreases
* if there is not decreasing pair, remove the last one

"""

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == 0:
            return "0"
        
        if num[0] == "0":
            return self.removeKdigits(num[1:], k)
        
        if k == 0:
            return num
        
        # k >= 1
        N = len(num)
        for i in range(N-1):
            j = i+1
            if num[i] > num[j]:
                return self.removeKdigits(num[:i] + num[j:], k-1)
        
        return self.removeKdigits(num[:N-1], k-1)
            
                
        
        
        
