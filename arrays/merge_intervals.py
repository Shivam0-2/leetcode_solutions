#Problem: https://leetcode.com/problems/merge-intervals/
#Approach: We first sort the intervals based on their start time. Then we iterate through
#the sorted intervals and merge them if they overlap. If they don't overlap, we add the current interval to the merged list and move on to the next one.
#Time Complexity: O(n log n) due to sorting the intervals.
def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])

        merged = []
        curr = intervals[0]

        for i in range(1, len(intervals)):
            next_interval = intervals[i]

            if next_interval[0] <= curr[1]:
                curr[1] = max(curr[1], next_interval[1])
            else:
                merged.append(curr)
                curr = next_interval

        merged.append(curr)
        return merged

        