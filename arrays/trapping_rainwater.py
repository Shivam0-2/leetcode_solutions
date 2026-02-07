#Problem: https://leetcode.com/problems/trapping-rain-water/
#Approach: Two pointer approach, we maintain two pointers at the start and end of the array, and we keep track of the maximum height of the left and right pointers. We move the pointer with the smaller height towards the center, and we calculate the water trapped at each step.
#Time Complexity: O(n) where n is the length of the height array.
def trap(self, height):
        left,right = 0, len(height)-1
        left_max,right_max=height[left], height[right]
        water = 0
        while left<right:
            if left_max<right_max:
                left += 1
                left_max =max(left_max,height[left])
                water += left_max-height[left]
            else:
                right -=1
                right_max = max(right_max,height[right])
                water += right_max - height[right]
        return water

        