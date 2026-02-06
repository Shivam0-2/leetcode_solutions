#Problem: https://leetcode.com/problems/valid-palindrome/
#Approach: Two Pointer Technique
#Time Complexity: O(n)
#Space Complexity: O(1)
def isPalindrome(self, s):
        left, right = 0, len(s) - 1

        while left < right:
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            elif s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1

        return True