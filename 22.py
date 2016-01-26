def delete_node(node):
    if node:
        node.val = node.next.val
        node.next = node.next.next
    else:
        raise Exception("cant delete the last node")
