class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def loop(head):
    slow=head
    fast=head

    while(fast is not None and fast.next is not None):
        slow=slow.next
        fast=fast.next.next

        if slow.data==fast.data:
            return True
    return False


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = head.next

has_loop = loop(head)

if has_loop:
    print("The linked list has a loop")
else:
    print("The linked list does not have a loop")
