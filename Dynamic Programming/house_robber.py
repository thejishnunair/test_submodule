"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

https://leetcode.com/problems/house-robber/
"""


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        number_of_houses = len(nums)
        dp = [0 for i in range(number_of_houses)]  # max sum at point i.

        if len(nums) > 0:
            dp[0] = nums[0]

        if len(nums) > 1:
            dp[1] = max(nums[0], nums[1])

        for i in range(2, number_of_houses):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])

        return dp[number_of_houses - 1]