class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        e = [[0] * n for _ in range(n)]

        for (a, b) in edges:
            e[a][b] = 1
            e[b][a] = 1

        seen = [False] * n

        def dfs(i):
            seen[i] = True

            for nei in range(n):
                if e[i][nei] == 1:
                    if seen[nei]:
                        return False
                    e[i][nei] = 0
                    e[nei][i] = 0
                    dfs(nei)

        dfs(0)

        s = sum(map(sum, e))
        if s > 0:
            return False

        for i in seen:
            if not i:
                return False

        return True
