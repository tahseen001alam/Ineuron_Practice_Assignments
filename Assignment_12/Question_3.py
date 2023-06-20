class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def find_nth_from_end(head, N):
    fast = head
    slow = head

    for _ in range(N):
        if fast is None:
            return None
        fast = fast.next

    while fast is not None:
        fast = fast.next
        slow = slow.next

    return slow

