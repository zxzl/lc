class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        if len(timePoints) < 2:
            return 0
        
        N = len(timePoints)
        
        timePoints = list(map(self.toMinutes, timePoints))
        timePoints.sort()
        
        min_gap = float('inf')
        for i in range(N-1):
            a = timePoints[i]
            b = timePoints[i+1]
            
            min_gap = min(min_gap, b-a)
            
        gap_first_last = (self.toMinutes("24:00") - timePoints[-1]) + (timePoints[0] - self.toMinutes("00:00"))
        min_gap = min(min_gap, gap_first_last)
        
        return min_gap
        
        
    def toMinutes(self, hhmm): 
        
        minutes = 0
        
        [hh,mm] = hhmm.split(":")
        
        minutes += int(hh) * 60
        minutes += int(mm)
        
        return minutes
