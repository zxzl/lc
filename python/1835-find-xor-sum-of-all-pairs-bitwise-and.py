class Solution:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:

        ca = 0
        for a in arr1:
            ca = ca ^ a

        cb = 0
        for b in arr2:
            cb = cb ^ b

        return ca & cb
