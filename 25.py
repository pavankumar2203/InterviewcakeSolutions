def ktolast(node, k):

    if node is None:
        raise Exception("Node cannot be None")

	start = head
    i = 0
    while(i < k):
        start = start.next

    while(start is not None):
        start = start.next
        head = head.next

    return head

    
