#Problem Link: https://leetcode.com/problems/maximum-average-subarray-i/
#Approach : Sliding Window Technique
#Time Complexity: O(n)  
#Space Complexity: O(1)
def findMaxAverage(self, nums, k):
        w_sum= sum(nums[0:k])
        max_sum= w_sum
        for i in range(k,len(nums)):
            w_sum = w_sum- nums[i-k]+ nums[i]
            max_sum = max(w_sum,max_sum)
        return max_sum/ float(k)