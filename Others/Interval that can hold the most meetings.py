"""
Problem Statement:
Given a two dimensional array arr[][] of dimensions N * 2 which contains the starting and ending time for N meetings on a given day. The task is to print a list of time slots during which most number of concurrent meetings can be held.

Explanation: 
The given 5 meetings overlap at {215, 230}.

Input: arr[][] = {{100, 200}, {50, 300}, {300, 400}} 
Output: [100, 200] 


Solution
1. Sort the array based on the start time of meetings.
2. Initialize a min-heap.
3. Initialize variables max_len, max_start and max_end to store maximum size of min heap, start time and end time of concurrent meetings respectively.
4. Iterate over the sorted array and keep popping from min_heap until arr[i][0] becomes smaller than the elements of the min_heap, i.e. pop all the meetings having ending time smaller than the starting time of current meeting, and push arr[i][1] in to min_heap.
5. If the size of min_heap exceeds max_len, then update max_len = size(min_heap), max_start = meetings[i][0] and max_end = min_heap_element.
Return the value of max_start and max_end at the end.
"""
import heapq
a = [[100, 300], [145, 215], [200, 230], [215, 300], [215, 400], [500, 600], [600, 700]]
# output = [215, 230] 
a.sort(key = lambda x:x[0])
minHeap = []
max_len, max_start, max_end = 0, 0, 0
heapq.heappush(minHeap, a[0][1])
for start, end in a:
    while minHeap and start >= minHeap[0]:
        heapq.heappop(minHeap)
    heapq.heappush(minHeap, end)
    if len(minHeap) > max_len:
        max_len = len(minHeap)
        max_start = start
        max_end = minHeap[0]
        
print(max_len, [max_start, max_end])