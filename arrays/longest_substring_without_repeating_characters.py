#Problem Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
#Approach: Variable Sliding Window Technique
#Time Complexity: O(n)  

def lengthOfLongestSubstring(self, s):
        
        left = 0
        seen = set()
        max_len = 0
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            max_len = max(max_len, right - left + 1)
        return max_len
