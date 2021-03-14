"""
simplify the question -> maximize the sum of average point

then it becomes dp -> (rest of classes, rest of extra students)

complexity: N*K <- too much?

how can we improve? 
- skip already 100% pass classes

TLE
---

k*log(N) solution

we keep expected increase of avg score for each class

every time, we pop the class that will get the most biggest benefit
and update expected benefit

run this for k times

"""

import heapq

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        N = len(classes)
        
        incs = []
        
        for (i,c) in enumerate(classes):
            curr_ratio = c[0] / c[1]
            new_ratio = (c[0] + 1) / (c[1] + 1)
            gain = new_ratio - curr_ratio
            incs.append((-1 * gain, i))
            
        heapq.heapify(incs)
        
        for _ in range(extraStudents):
            (ng, i) = heapq.heappop(incs)
            
            classes[i][0] += 1
            classes[i][1] += 1
            
            curr_ratio = classes[i][0] / classes[i][1]
            new_ratio = (classes[i][0] + 1) / (classes[i][1] + 1)
            gain = new_ratio - curr_ratio
            heapq.heappush(incs, (-1 * gain, i))
            
        # get final average ratio
        s = 0
        
        for (passed, total) in classes:
            s += passed / total
            
        return s / N
            
            
