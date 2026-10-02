# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head):
        curr = head
        slow = curr
        fast = curr

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

           
print("Finding middle of linked list...")
A = [1,2,3,4,5]

def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

head = create_linked_list(A)

solution = Solution().middleNode(head)
print("Middle node:", solution.val if solution else None)