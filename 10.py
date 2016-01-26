def find_largest(root):

    if root:
        return find_largest(root.right)

    return root.value

def find_second_largest(root):

    if not root:
        return None

    if root.left and not root.right:
        return find_largest(root.left)

    if root.right and not root.right.left and not root.right.right:
        return root.value

    return find_second_largest(root.right)


#O(n), O(n)
#for balanced tree, O(log n), O(log n)
#make iterative version to get constant space
