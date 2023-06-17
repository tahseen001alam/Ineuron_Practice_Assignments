class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def middle_element(head):
    if head is None or head.next is None:
        return None
    slow=head
    fast=head
    prev=None
        
    while(fast is not None and fast.next is not None):
        fast=fast.next.next
        prev=slow
        slow=slow.next
        
    prev.next=slow.next
    return head

def print_linked_list(head):
    current = head
    while current is not None:
        print(current.data, end=" ")
        current = current.next
    print()

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

print("Original linked list:")
print_linked_list(head)

head1 = middle_element(head)

print("Modified linked list:")
print_linked_list(head1)
