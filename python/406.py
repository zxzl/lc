"""
some observation

* for largest numbers -> they are always 0~occurence
* for smallest number -> it is determined first

1) sort by height
2) fix position for smaller height

4,4 5,0 5,2 6,1 7,0 7,1

5,0 7,0 5,2 6,1 4,4 7,1
"""


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        N = len(people)
        
        people.sort()
        
        ans = [None] * N
        
        for [height, order] in people:
            
            pos = 0
            num_le = 0
            
            while num_le <= order:
                if ans[pos] == None or ans[pos][0] >= height:
                    num_le += 1
                pos += 1
                
            ans[pos-1] = [height,order]
                
        
        return ans
