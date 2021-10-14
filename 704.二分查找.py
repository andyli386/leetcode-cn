'''
Author: Vincent
Date: 2021-10-14 12:02:58
LastEditors: Vincent
LastEditTime: 2021-10-14 12:06:56
Description: file content
'''
#
# @lc app=leetcode.cn id=704 lang=python3
#
# [704] 二分查找
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = int(left + (right - left)/2)
            if nums[mid] < target:
                left = mid+1
            elif nums[mid] > target:
                right = mid-1
            elif nums[mid] == target:
                return mid
            
        return -1
# @lc code=end

