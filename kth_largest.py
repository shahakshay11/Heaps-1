"""
// Time Complexity : O(nlogk) 
// Space Complexity : O(nlogk)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : No
// Your code here along with comments explaining your approach
Algorithm explanation
Using min heap with negating the numbers and removing the elements 
from the heap till we reach k
Last ele popped is kth element to be returned
"""

import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        N = len(nums)
        if N == 1:
            return nums[0]
        
        heap = []
        
        #heapifying all the elements
        for num in nums:
            heapq.heappush(heap,-num)
        
        i = 0
        #popping the elements till reach k
        while i < k:
            ele = heappop(heap)
            i+=1
            
        return -ele