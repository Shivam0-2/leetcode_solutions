#Problem: https://leetcode.com/problems/first-missing-positive/
#Approach: We can use the input array itself to keep track of which numbers are present. We can iterate through the array and mark the presence of each number by negating the value at the corresponding index. Finally, we can iterate through the array again to find the first positive index, which will give us the first missing positive number.
#Time Complexity: O(n)  
#Space Complexity: O(1)

def firstMissingPositive(self, nums):
        n = len(nums)

        #Replace all negative numbers and numbers greater than n with (n + 1)
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = n + 1

        #Mark the presence of numbers by negating the value at the corresponding index  
        for i in range(n):
            val = abs(nums[i])
            if 1 <= val <= n:
                if nums[val - 1] > 0:
                    nums[val - 1] *= -1
        #Find the first positive index, which will give us the first missing positive number    
        for i in range(n):
            if nums[i] >= 0:
                return i + 1

        return n + 1