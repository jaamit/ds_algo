"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 

Use a sliding window approach (right - left) and set for unique elements
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_l = lt = rt = 0
        unique = set()
        
        while lt < len(s) and rt < len(s):
            if s[rt] not in unique:
                unique.add(s[rt])
                rt += 1
                max_l = max(max_l, rt-lt)
                print(f'rt {rt}, max_l {max_l}')
                print('set' ,unique)
            else:
                unique.remove(s[lt])
                lt += 1
                print(f'lt {lt}, max_l {max_l}')
                print('set 2', unique)
                
        
        return max_l

sol = Solution()
print(sol.lengthOfLongestSubstring('dvdf'))
