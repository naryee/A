import time
from floyd import ListNode, detectCycle

def create_linked_list_with_cycle(n):
    head = ListNode(0)
    current = head
    cycle_start = None
    for i in range(1, n):
        current.next = ListNode(i)
        current = current.next
        if i == n // 2:
            cycle_start = current
    current.next = cycle_start
    return head

def measure_execution_time(func, *args):
    start_time = time.time()
    func(*args)
    end_time = time.time()
    return end_time - start_time

if __name__ == "__main__":
    input_sizes = [100, 1000, 10000]

    for size in input_sizes:
        linked_list = create_linked_list_with_cycle(size)
        execution_time = measure_execution_time(detectCycle, linked_list)
        print(f"Input size: {size}, Execution time: {execution_time} seconds")
