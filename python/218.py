import bisect

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        
        events = []
        
        for b in buildings:
            events.append((b[0], 'OPEN', b[2]))
            events.append((b[1], 'CLOSE', b[2]))
            
        events.sort()
        
        # group by x
        events_by_x = []
        bucket = []
        for e in events:
            if len(bucket) == 0:
                bucket.append(e)
            elif e[0] == bucket[-1][0]:
                bucket.append(e)
            else:
                events_by_x.append(bucket)
                bucket = [e]
        if len(bucket) > 0:
            events_by_x.append(bucket)
        
        # (0,0) is dummy for comparing with prev skyline simpler
        skyline = [(0, 0)]
        # 0 is dummy for getting top height simpler
        heights = [0]
        
        for events_same_x in events_by_x:
            for (x, status, h) in events_same_x:
                if status == 'OPEN':
                    i = bisect.bisect_left(heights, h)
                    heights.insert(i, h)
                elif status == 'CLOSE':
                    i = heights.index(h)
                    heights.pop(i)
            
            top = heights[-1]
            if top != skyline[-1][1]:
                skyline.append((x, top))
                
        return skyline[1:]
