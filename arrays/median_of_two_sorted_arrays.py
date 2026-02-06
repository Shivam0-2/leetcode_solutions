#Problem Link: https://leetcode.com/problems/median-of-two-sorted-arrays/
#Approach: Merging two arrays and finding the median with brute force(not optimal).
#Time Complexity: O((m+n) log(m+n)) due to sorting
#Space Complexity: O(m+n) for storing the merged array.

def findMedianSortedArrays(self, nums1, nums2):
        merged = nums1 + nums2
        merged.sort()

        n = len(merged)

        if n % 2 == 1:
            return float(merged[n // 2])
        else:
            mid1 = merged[(n // 2) - 1]
            mid2 = merged[n // 2]
            return (mid1 + mid2) / 2.0