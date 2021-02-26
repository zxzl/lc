from collections import defaultdict

class UndergroundSystem:

    def __init__(self):
        # customer id -> (stationName, t)
        self.customer = {}
        
        #journeys[a][b] = (list of time taken)
        self.journeys = defaultdict(lambda: defaultdict(list))
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.customer[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        (startStation, startT) = self.customer[id]
        del self.customer[id]

        self.journeys[startStation][stationName].append(t - startT)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        durations = self.journeys[startStation][endStation]
        
        return sum(durations) / len(durations)
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
