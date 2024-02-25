
This project provides a simple implementation of Floyd's Algorithm for cycle detection in a linked list.

To use the `detectCycle` function, import it from the `floyd` module and pass the head of the linked list as an argument.

Example:
```python
from floyd import ListNode, detectCycle

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)

cycle_start = detectCycle(head)
if cycle_start:
    print("Cycle starts at node with value:", cycle_start.val)
else:
    print("No cycle found.")
