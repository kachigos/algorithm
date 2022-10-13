''''''
'''
Remove linked list element
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def removeElements(self, head: list[int], val: int) -> list[int]:
#         ls = [x if x != val else None for x in head]
#         l = []
#         for i in ls:
#             if i != None:
#                 l.append(i)
#         print(l)
#
# s = Solution()
# k = [7,7,7,1]
# s.removeElements(k,7)