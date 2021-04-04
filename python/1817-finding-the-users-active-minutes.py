from collections import defaultdict


class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:

        user_t = defaultdict(set)

        for (u, t) in logs:
            user_t[u].add(t)

        ans = [0 for _ in range(k)]

        for v in user_t.values():
            if len(v) == 0:
                continue
            ans[len(v) - 1] += 1

        return ans
