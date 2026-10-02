class linkedlist:
    def __init__(self, val=0, next=None):
        self.prev = None
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)

    def reverse(self):
        self.prev = None
        current = self
        while current:
            next_node = current.next
            current.next = self.prev
            current.prev = next_node
            self.prev = current
            current = next_node
        return self.prev

    def print_list(self):
        current = self
        while current:
            print(current.val)
            current = current.next

    def middle(self):
        slow = self
        fast = self
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def detect(self):
        slow = self
        fast = self
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

arr = [1,1,2,3,4,5]

for i in range(len(arr)):
    if i == 0:
        A = linkedlist(arr[i])
        current = A
    else:
        current.next = linkedlist(arr[i])
        current = current.next

# A = linkedlist()
# B = linkedlist(2)
# C = linkedlist(3)
# D = linkedlist(4)
# E = linkedlist(5)
# A.next = B
# B.next = C
# C.next = D
# D.next = C
# E = A.reverse()

# print(A.detect())
# print(A.middle().val)
# A.print_list()
# while C:
#     print(C.val)
#     C = C.next











# class linkedlist:
#     def __init__(self, val):
#         self.val = val
#         self.next = None

# A = linkedlist(1)
# B = linkedlist(2)
# C = linkedlist(3)
# D = linkedlist(4)
# E = linkedlist(5)
# A.next = B
# B.next = C
# C.next = D
# D.next = E

# slow = A
# fast = A
# while fast and fast.next:
#     slow = slow.next
#     fast = fast.next.next
#     print(f"Slow pointer at: {slow.val}, Fast pointer at: {fast.val if fast else None}")

# print(f"Middle element: {slow.val}")


# class TwoWayLinkedList:
#     def __init__(self, head):
#         self.prev = None
#         self.head = head
#         self.next = None

# A = TwoWayLinkedList(1)
# B = TwoWayLinkedList(2)
# C = TwoWayLinkedList(3)

# A.next = B
# B.next = C
# B.prev = A
# C.prev = B

# while A is not None:
#     print(A.head)
#     A = A.next


# class TwoWayLinkedList:
#     def __init__(self, value):
#         self.value = value
#         self.prev = None
#         self.next = None


# def reverse_linked_list(head):
#     current = head
#     new_head = None

#     while current is not None:
#         next_node = current.next
#         print(f"Reversing node with value: {current.value}")
#         current.next = current.prev
#         print(f"Setting current.next to: {current.prev.value if current.prev else None}")
#         current.prev = next_node
#         print(f"Setting current.prev to: {next_node.value if next_node else None}")
#         new_head = current
#         current = next_node
        

#     return new_head

# A = TwoWayLinkedList(1)
# B = TwoWayLinkedList(2)
# C = TwoWayLinkedList(3)

# A.next = B
# B.prev = A
# B.next = C
# C.prev = B

# head = reverse_linked_list(A)

# while head:
#     print(head.value)
#     head = head.next   