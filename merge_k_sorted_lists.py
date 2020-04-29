"""
// Time Complexity : O(nlogk)
// Space Complexity : O(n + k) //creating the new linked list + heap storage
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : No
// Your code here along with comments explaining your approach
Algorithm explanation
Min heapifying the elements from all the linked lists and popping one by one 
to get in sorted order until heap is empty
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import heapq

class Solution:
    def getList(self,list_node):
        l = []
        temp = list_node
        while temp:
            print temp.val
            l.append(temp.val)
            temp = temp.next
        return l
    
    def getLinkedList(self,l):
        head = ListNode(l[0])
        tail = head
        for i in range(1,len(l)):
            tail.next = ListNode(l[i])
            tail = tail.next
        return head
    
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        
        heap = []
        all_ele = []
        for l in lists:
            ll = self.getList(l)
            #print "ll",ll
            all_ele+=ll
            
        if not all_ele:
            return None
        
        #heapifying all the elements collected from the linked list
        for ele in all_ele:
            heapq.heappush(heap,ele)
        
        sorted_list = []
        while heap:
            #fetchhing the element in sorted order one by one
            elem = heapq.heappop(heap)
            sorted_list.append(elem)
        
        print sorted_list
        #returning linked list from the sorted list
        return self.getLinkedList(sorted_list)