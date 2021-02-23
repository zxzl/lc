class Solution:
    def compress(self, chars: List[str]) -> int:
        
        if len(chars) == 1:
            return 1
        
        reader = 1
        writer = 0
        
        acc = 1
        
        while reader < len(chars):
            
            if chars[reader] != chars[reader-1]:
                #print(reader, writer)
                chars[writer] = chars[reader-1]
                writer += 1
                if acc >= 2:
                    for c in str(acc):
                        chars[writer] = c
                        writer += 1
                acc = 1
                
            else:
                acc += 1
            reader += 1
            
        # last chars
        chars[writer] = chars[-1]
        writer += 1
        
        if acc > 1:
            for c in str(acc):
                chars[writer] = c
                writer += 1
                    
        chars[writer:] = []
        
        return len(chars)
                
                    
                
            
