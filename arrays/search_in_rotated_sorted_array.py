#Problem: https://leetcode.com/problems/search-in-rotated-sorted-array/
# For a O(n) solution, we can simply iterate through the array and check if the target is present. However, we can do better than that by using a modified binary search approach. We can determine which half of the array is sorted and then decide whether to search in the left or right half based on the target value.
#Time Complexity: O(log n)

def search(self, nums, target):
        left, right = 0 , len(nums)-1

        while left<=right:
            mid = (left+right)//2
            if target == nums[mid]:
                return mid
            if nums[left]<= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid -1
                else : 
                    left = mid + 1
                
            else: 
                if nums[mid]<target <=nums[right]:
                    left = mid +1
                else: 
                    right = mid - 1
        return -1