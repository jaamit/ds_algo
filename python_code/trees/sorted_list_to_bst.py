"""
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Convert List -> Arr
# Arr[mid] -> BST Root

class Solution:
    def list_to_arr(self, head):
        curr = head
        arr = []
        
        while curr:
            arr.append(curr.val)
            curr = curr.next
        
        return arr
    
    def arr_to_tree(self, nums, left, right):
        while left <= right:
            mid = (left + right) // 2
            node = TreeNode(nums[mid])
            node.left = self.arr_to_tree(nums, left, mid-1)
            node.right = self.arr_to_tree(nums, mid+1, right)
            return node
    
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        nums = self.list_to_arr(head)
        
        return self.arr_to_tree(nums, 0, len(nums)-1)
        
