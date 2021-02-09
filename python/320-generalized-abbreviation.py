class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        
        self.word = word
        self.ans = []

        self.createPermutation(len(word), [])
        
        return self.ans
    
    def createPermutation(self, remaining, prev):
        if remaining == 0:
            self.buildAbbreviation(prev)
            return
        
        self.createPermutation(remaining - 1, prev + [True])
        self.createPermutation(remaining - 1, prev + [False])
        
        
    def buildAbbreviation(self, permutation):
        
        skipped = 0
        s = ""
        for i in range(len(self.word)):
            if permutation[i]:
                if skipped > 0:
                    s += str(skipped)
                    skipped = 0
                s += self.word[i]
            else:
                skipped += 1
        
        if skipped > 0:
            s += str(skipped)
            
        self.ans.append(s)
            
