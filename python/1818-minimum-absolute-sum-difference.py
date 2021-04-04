import bisect


class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        N = len(nums1)

        nums1_sorted = sorted(nums1)
        nums1_closest_nums2 = []

        for n2 in nums2:
            i = bisect.bisect_left(nums1_sorted, n2)

            if i == 0:
                nums1_closest_nums2.append(nums1_sorted[0])
            elif i == N:
                nums1_closest_nums2.append(nums1_sorted[N-1])
            else:
                ldiff = abs(n2 - nums1_sorted[i-1])
                rdiff = abs(n2 - nums1_sorted[i])
                if ldiff < rdiff:
                    nums1_closest_nums2.append(nums1_sorted[i-1])
                else:
                    nums1_closest_nums2.append(nums1_sorted[i])

        diff_no_change = 0
        for i in range(N):
            diff_no_change += abs(nums1[i] - nums2[i])
        ans = diff_no_change
        #print("nochange", ans)

        for i in range(N):
            orig_diff = abs(nums1[i] - nums2[i])
            change_diff = abs(nums1_closest_nums2[i] - nums2[i])

            if orig_diff > change_diff:
                new_ans = diff_no_change - orig_diff + change_diff
                ans = min(ans, new_ans)

        return ans % (10**9+7)
