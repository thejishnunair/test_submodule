"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

https://leetcode.com/problems/minimum-path-sum/
"""

import sys
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        num_rows = len(grid)
        num_cols = len(grid[0])

        dp = [[0 for cols in range(num_cols)] for rows in range(num_rows)]

        def min_path(i, j):
            if i < 0 or j < 0:
                return sys.maxsize

            if i == 0 and j == 0:
                return grid[0][0]

            if dp[i][j] != 0:
                return dp[i][j]

            dp[i][j] = grid[i][j] + min(min_path(i - 1, j), min_path(i, j - 1))
            return dp[i][j]

        return min_path(num_rows - 1, num_cols - 1)