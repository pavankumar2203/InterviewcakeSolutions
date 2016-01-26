def check_cycle(head):

    slow = head
    fast = head

    while(fast != null and fast.next != null):
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False
