'''
Author: Vincent
Date: 2021-02-03 12:57:51
LastEditors: Vincent
LastEditTime: 2021-02-03 15:17:40
Description: file content
'''
#
# @lc app=leetcode.cn id=704 lang=python3
#
# [704] 二分查找
#

# @lc code=start
class Solution:
    # def search(self, nums: List[int], target: int) -> int:
    #     # 普通二分查找法
    #     left = 0
    #     right = len(nums)-1
    #     while( left <= right):
    #         mid = int(left + (right-left)/2)
    #         if target < nums[mid]:
    #             right = mid - 1
    #         elif target > nums[mid]:
    #             left = mid + 1
    #         elif target == nums[mid]:
    #             return mid
    #     return -1

    # def search(self, nums: List[int], target: int) -> int:
    #     # 左边界
    #     left = 0
    #     right = len(nums) - 1
    #     while(left <= right):
    #         mid = int(left + (right - left )/2)
    #         if target < nums[mid]:
    #             right = mid - 1
    #         elif target > nums[mid]:
    #             left = mid + 1
    #         elif target == nums[mid]:
    #             right = mid - 1
    #     return left if left < len(nums) and nums[left] == target else -1


    def search(self, nums: List[int], target: int) -> int:
        # 右边界
        left = 0
        right = len(nums) - 1
        while(left <= right):
            mid = int(left + (right - left)/2)
            if target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
            elif target == nums[mid]:
                left = mid + 1
        return right if right >= 0 and nums[right] == target else -1

# @lc code=end

