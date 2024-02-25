class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def detectCycle(head):
    def intersect(slow, fast):
        if not fast or not fast.next:
            return None
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return slow
        return intersect(slow, fast)

    if not head or not head.next:
        return None
    
    intersection = intersect(head, head)
    if not intersection:
        return None
    
    ptr1 = head
    ptr2 = intersection
    while ptr1 != ptr2:
        ptr1 = ptr1.next
        ptr2 = ptr2.next

    return ptr1

