"""
Given a sorted array of n elements, possibly with duplicates, find the number of occurrences of the target element.

Example 1:

Input: arr = [4, 4, 8, 8, 8, 15, 16, 23, 23, 42], target = 8 
Output: 3
Example 2:

Input: arr = [3, 5, 5, 5, 5, 7, 8, 8], target = 6
Output: 0
Example 3:

Input: arr = [3, 5, 5, 5, 5, 7, 8, 8], target = 5
Output: 4
Expected O(logn) time solution.
"""
import bisect
def solve(a, target):
	l = bisect.bisect_left(a, target)
	r = bisect.bisect_right(a, target)
	if (l == 0 and r == 0) or (l == len(a) - 1 and r == len(a) - 1): return 0
	return r - l

print(solve([4, 4, 8, 8, 8, 15, 16, 23, 23, 42], 8))
print(solve([3, 5, 5, 5, 5, 7, 8, 8], 6))	
print(solve([3, 5, 5, 5, 5, 7, 8, 8], 5))