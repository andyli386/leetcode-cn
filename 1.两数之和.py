#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index, item in enumerate(nums[:-1]):
            sub = target - item
            if sub in nums[index+1:]:
                return index, nums[index+1:].index(sub)+index+1

# @lc code=end

