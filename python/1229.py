class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort(key=lambda x: x[0])
        slots2.sort(key=lambda x: x[0])
        
        
        def intersect(a, b):
            if a[1] <= b[0] or b[1] <= a[0]:
                return False
            return True
        
        i = 0
        j = 0
        
        while True:
            a = slots1[i]
            b = slots2[j]
            
            if intersect(a, b):
                start = max(a[0], b[0])
                end = start + duration
                if end <= min(a[1], b[1]):
                    return [start, end]
            
            if a[1] <= b[1] and i + 1 < len(slots1):
                i += 1
            elif j + 1 < len(slots2):
                j += 1
            else:
                break
        
        return []
