class Solution:
    def maxSubArray(self, nums):
        def solve(lo, hi):
            if lo == hi:  # single element
                x = nums[lo]
                return (x, x, x, x)  # total, prefix, suffix, best
            mid = (lo + hi) // 2
            lt = solve(lo, mid)
            rt = solve(mid + 1, hi)
            total = lt[0] + rt[0]
            pref = max(lt[1], lt[0] + rt[1])
            suff = max(rt[2], rt[0] + lt[2])
            best = max(lt[3], rt[3], lt[2] + rt[1])
            return (total, pref, suff, best)

        return solve(0, len(nums) - 1)[3]
