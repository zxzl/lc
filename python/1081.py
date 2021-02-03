class Solution:
    def smallestSubsequence(self, s: str) -> str:
        
        last_pos = {}
        for i in range(len(s)):
            last_pos[s[i]] = i
            
        
        ans = []
        added = set()
        for i in range(len(s)):
            c = s[i]
            
            while c not in added and len(ans) > 0 and ans[-1] > c and last_pos[ans[-1]] > i:
                p = ans.pop()
                added.remove(p)
            
            if c not in added:
                ans.append(c)
                added.add(c)
            
        return "".join(ans)
