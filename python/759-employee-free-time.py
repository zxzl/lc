"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

"""
get free time
count intersection one by one
"""

MAX_T = 10**8+1

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        
        def getFreeTimeFromSchedule(s):
            times = []
            if len(s) ==0:
                return times
            
            #0~first
            if s[0].start != 0:
                times.append((0, s[0].start))
            
            for i in range(len(s) - 1):
                times.append((s[i].end, s[i+1].start))
            
            times.append((s[-1].end, MAX_T))
            return times
            
        
        def merge(A, B):
            if len(A) == 0 or len(B) == 0:
                return []
            
            common = []
            
            i = 0
            j = 0
            
            while True:
                a = A[i]
                b = B[j]
                if not(a[1] < b[0] or b[1] < a[0]): # has intersection
                    common.append((max(a[0], b[0]),
                                   min(a[1], b[1])))
                if i < len(A) - 1 and j < len(B) - 1:
                    if a[1] < b[1]:
                        i += 1
                    else:
                        j += 1
                elif i < len(A)-1:
                    i += 1
                elif j < len(B)-1:
                    j += 1
                else:
                    break
            
            return common

        freeTimes = [getFreeTimeFromSchedule(s) for s in schedule]
                
        intersection = freeTimes[0]
        for i in range(1, len(freeTimes)):
            intersection = merge(intersection, freeTimes[i])
            
        ans = []
        for i in intersection:
            if i[0] == 0 or i[1] == MAX_T or i[0] == i[1]:
                continue
            ans.append(Interval(i[0], i[1]))
        
        return ans
            
