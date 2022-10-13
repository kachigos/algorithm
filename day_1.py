''''''
'''
1.Palindrom
'''
# class Solution:
#     def isPalindrome(self, x: int):
#         if x > 0:
#             return x == int(str(x)[::-1])
#         elif x < 0:
#             return False
#         elif x == 0:
#             return True
#
#
# s = Solution()
# s.isPalindrome(-121)


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

# 2 var


'''
Contains duplicate
'''
# class Solution:
#     def containsDuplicate(self, nums: list[int]) -> bool:
#         s = set(nums)
#         print(s)
#         if len(s) == len(nums):
#             print('false')
#         if len(s) < len(nums):
#             print('true')
#
# s = Solution()
# nums = [1,5,3,4]
# s.containsDuplicate(nums)
