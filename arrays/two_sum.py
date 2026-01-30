#Problem Link: https://leetcode.com/problems/two-sum/
#Approach: Using a hash map.
#Time Complexity: O(n)
#Space Complexity: O(n)

def twoSum(self, nums, target):
    seen = {}

    for i in range(len(nums)):
        num = nums[i]
        complement = target - num

        if complement in seen:
            return [seen[complement], i]

        seen[num] = i
