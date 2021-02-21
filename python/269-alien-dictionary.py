import collections

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        
        chars = set()
        for word in words:
            for c in word:
                chars.add(c)
        
        graph = collections.defaultdict(list)
        
        for i in range(len(words)-1):
            for j in range(i+1, len(words)):
                wordA = words[i]
                wordB = words[j]
            
                C = min(len(wordA), len(wordB))
                
                if len(wordA) > len(wordB) and wordA[:C] == wordB:
                    return ""
            
                for k in range(C):
                    ca = wordA[k]
                    cb = wordB[k]
                    if ca == cb:
                        continue
                
                    if ca in graph[cb]:
                        return ""
                
                    if cb not in graph[ca]:
                        graph[ca].append(cb)
                    break
                    
        # topoligical sort using graph
        seen = set()
        self.ans = []
        
        def dfs(root):
            if root in seen:
                return
            seen.add(root)
            for nei in graph[root]:
                dfs(nei)
            
            self.ans.append(root)
        
        for c in chars:
            if c not in seen:
                dfs(c)
                
        return "".join(reversed(self.ans))
                    
            
