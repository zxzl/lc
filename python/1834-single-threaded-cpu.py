import heapq


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        # (t, duration, i)
        events = []

        # (duration, i)
        pending = []

        logs = []

        for (i, task) in enumerate(tasks):
            heapq.heappush(events, [task[0], task[1], i])

        # print(events)

        e = heapq.heappop(events)
        logs.append(e[2])
        events.append([e[0] + e[1], float('inf')])

        while len(events) > 0:
            e = heapq.heappop(events)
            # print(e)
            if e[1] == float('inf'):  # a process ended
                if len(pending) == 0:
                    break

                new_task = heapq.heappop(pending)
                heapq.heappush(events, [new_task[0] + e[0], float('inf')])
                logs.append(new_task[1])
            else:  # add process to q
                heapq.heappush(pending, [e[1], e[2]])

        return logs
