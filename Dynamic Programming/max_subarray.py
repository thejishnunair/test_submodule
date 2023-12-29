"""
https://cses.fi/problemset/task/1643/
"""
import sys


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        sum = -sys.maxsize
        max_sum = -sys.maxsize

        for num in nums:
            sum = max(num, sum + num)
            max_sum = max(max_sum, sum)
        return max_sum

n = int(input())
mylist = [int(x) for x in input().split()]
s = Solution()
print(s.maxSubArray(mylist))