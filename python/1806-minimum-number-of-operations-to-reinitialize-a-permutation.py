class Solution:
    def reinitializePermutation(self, n: int) -> int:

        perm = [i for i in range(n)]

        cnt = 1

        while True:
            arr = [0 for _ in range(n)]
            for i in range(n):
                if i % 2 == 0:
                    arr[i] = perm[i // 2]
                else:
                    arr[i] = perm[n // 2 + (i-1) // 2]

            done = True

            for i in range(n):
                if arr[i] != i:
                    done= False
                    break

            if done:
                break
            else:
                cnt += 1
                perm = arr

        return cnt


