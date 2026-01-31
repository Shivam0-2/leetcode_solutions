#Problem Link: https://leetcode.com/problems/product-of-array-except-self/
#Approach: Took two passes, one to calculate prefix products and another for suffix products.
#Time Complexity: O(n)  

def productExceptSelf(self, nums):
        prefix = 1
        n = len(nums)
        answer = []

        for i in range(n):
            answer.append(prefix)
            prefix *= nums[i]

        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer
