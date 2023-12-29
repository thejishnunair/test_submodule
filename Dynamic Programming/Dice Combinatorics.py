"""https://cses.fi/problemset/task/1633"""

class Solution(object):
    mod = 1000000007
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = [-1 for i in range(target + 1)]
        def get_count(target, dp):
            if target < 0:
                return 0
            if target == 0:
                return 1
            if dp[target] != -1:
                return dp[target]
            count = 0
            for num in nums:
                count += get_count(target - num, dp)
                count = count % self.mod
            dp[target] = count
            return count
        return get_count(target, dp)

n = int(input())
s = Solution()
print(s.combinationSum4([1,2,3,4,5,6], n))