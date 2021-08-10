#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        j = len(nums)-1
        while i <= j:
            if nums[i] == val and nums[j] != val:
                nums[i] = nums[j]
                j -= 1
            elif nums[j] == val:
                j -= 1
            elif nums[i] != val:
                i += 1

        return j+1

# @lc code=end

