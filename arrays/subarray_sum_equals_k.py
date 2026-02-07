#Problem: https://leetcode.com/problems/subarray-sum-equals-k/
#Approach: We can use a hashmap to store the prefix sum and its frequency. We iterate through the array and calculate the prefix sum at each step. We check if the prefix sum minus k exists in the hashmap, if it does, we add the frequency of that prefix sum to our count. Finally, we update the hashmap with the current prefix sum.
#Time Complexity: O(n) where n is the length of the input array.
def subarraySum(self, nums, k):
        hashmap = {0:1}
        prefix_sum = 0
        count = 0
        i=0
        for num in nums:
            prefix_sum += num
            if prefix_sum-k in hashmap:
                count += hashmap[prefix_sum-k]
            hashmap[prefix_sum]= hashmap.get(prefix_sum,0)+1
        return count