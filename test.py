import unittest
from floyd import ListNode, detectCycle

class TestFloyd(unittest.TestCase):
    def test_detectCycle_no_cycle(self):
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        self.assertIsNone(detectCycle(head))

    def test_detectCycle_with_cycle(self):
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        head.next.next.next = head.next
        self.assertEqual(detectCycle(head), head.next)
