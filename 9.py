def isvalid_bst(root, left, right):
    if not root:
        return True

    if root.val < left or root.val > right:
        return False

    return root.val >= left and root.val <= right and isvalid_bst(root.left, left, root.val) and isvalid_bst(root.right, root.val, right)


isvalid_bst(root, -sys.maxsize-1, sys.maxsize)
