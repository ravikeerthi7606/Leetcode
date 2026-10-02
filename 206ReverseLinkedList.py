# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        # self.prev = prev
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # current =None
        prev = None
        while head:
            next_node = head.next
            head.next = prev
            prev = next_node
            prev = head
            head = next_node
        return prev

            
print("Reversing linked list...")
A = [1,2,3,4,5]

def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next
    return head.next

head = create_linked_list(A)

solution = Solution().reverseList(head)