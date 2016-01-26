def get_mindepth(root):
    #another way of doing this is by level order traversal
    if not root:
        return 0
    if root.left is None and root.right is None:
        return 1
    if root.left:
        return get_mindepth(root.left) + 1
    if root.right:
        return get_mindepth(root.right) + 1
    if root.left and root.right:
	    return min(get_mindepth(root.left), get_mindepth(root.right)) + 1

def get_maxdepth(root):
    if not root:
        return 0
    if root.left is None and root.right is None:
        return 1
    if root.left:
        return get_maxdepth(root.left) + 1
    if root.right:
        return get_maxdepth(root.right) + 1
    if root.left and root.right:
	    return max(get_maxdepth(root.left), get_maxdepth(root.right)) + 1

def is_balanced(root):
    if not root:
        return True
    if get_maxdepth(root) - get_mindepth(root) > 1:
        return False
    else
    	return True



    
