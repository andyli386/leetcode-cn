'''
Author: Vincent
Date: 2021-10-14 12:15:40
LastEditors: Vincent
LastEditTime: 2021-10-14 13:48:50
Description: file content
'''
#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
from typing import List
class Solution:
    def left_bound(self, nums: List[int], target: int)->int:
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = int((left+(right-left)/2))
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] == target:
                right = mid - 1
        
        if left >= len(nums) or nums[left] != target:
            return -1
        return left

    def right_bound(self, nums: List[int], target: int)->int:
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = int((left+(right-left)/2))
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] == target:
                left = mid + 1
        
        if right < 0 or nums[right] != target:
            return -1
        return right 
        
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.left_bound(nums, target)
        right = self.right_bound(nums, target)
        return [left, right]
# @lc code=end

s = Solution()
print(s.right_bound([1], 1))