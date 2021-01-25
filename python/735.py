class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        if len(asteroids) == 1:
            return asteroids
        
        st = []
        
        for curr in asteroids:
            while len(st) > 0 and st[-1] > 0 and curr < 0:
                if st[-1] + curr < 0:
                    st.pop()
                    continue
                elif st[-1] + curr == 0:
                    st.pop()
                    break # dont'append curr
                else:
                    break
            else:
                st.append(curr)
        return st
