#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        q = -1
        s = s.strip()
        for i in range(len(s)):
            if s[i] == ' ':
                q = i

        result = (len(s) - q - 1) if (len(s) - q - 1) > 0 else 0
        return result

# @lc code=end

