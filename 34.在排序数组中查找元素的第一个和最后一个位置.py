'''
Author: Vincent
Date: 2021-02-03 14:43:36
LastEditors: Vincent
LastEditTime: 2021-02-03 15:53:59
Description: file content
'''
#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return self.searchLeft(nums, target), self.searchRight(nums, target)

    def searchRight(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = int(left + (right-left)/2)
            if target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
            elif target == nums[mid]:
                left = mid + 1
        return right if right >=0 and nums[right] == target else -1

    def searchLeft(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = int(left + (right-left)/2)
            if target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
            elif target == nums[mid]:
                right = mid - 1
        return left if left < len(nums) and nums[left] == target else -1
# @lc code=end

