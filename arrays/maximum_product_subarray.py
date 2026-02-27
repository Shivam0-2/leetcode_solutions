#Problem: https://leetcode.com/problems/maximum-product-subarray/
#Approach: We can keep track of the maximum and minimum product at each index, as the minimum product can become the maximum if multiplied by a negative number. We iterate through the array and update the current maximum and minimum products at each step, and keep track of the overall maximum product.
#Time Complexity: O(n)

def maxProduct(self, nums):
        result = nums[0]
        curr_max = nums[0]
        curr_min = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]

            temp_max = max(num, curr_max * num, curr_min * num)
            temp_min = min(num, curr_max * num, curr_min * num)

            curr_max = temp_max
            curr_min = temp_min

            result = max(result, curr_max)

        return result