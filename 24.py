def reverse(head):

	curr = head
    prev, next = None, None

    while (current):
        next = current.next
        current.next = prev
        prev = current
        current = next

    return prev


def reverse_rec(head):

    if head is None or head.next is None:
        return head

    rest = reverse_rec(head.next)
    head.next.next = head
    head.next = None

    return rest
