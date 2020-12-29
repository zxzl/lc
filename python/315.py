"""
* we keep track of count of unseen number
* for each number, we count the occurence of small & equal number
  * and decrement current number by one
  
* how to effectively fetch values of smaller keys..?
1) ordereddict -> O(n^2) -> acceptable?
2) 
"""

from collections import OrderedDict

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        
        nums_sorted = sorted(nums)
        
        m = OrderedDict()
        for k in nums_sorted:
            if k in m:
                m[k] += 1
            else:
                m[k] = 1
                
        
        ans = []
        
        for n in nums:
            smaller_right = 0
            
            for k in m.keys():
                if k < n:
                    smaller_right += m[k]
                else:
                    break
                    
            m[n] -= 1
            ans.append(smaller_right)
        
        return ans
