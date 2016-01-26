def has_palindrome_permutation(s):

    s = list(s)

    hashset = set()
    for c in s:
        if c in hashset:
            hashset.remove(c)
        else:
            hashset.add(c)

    return len(hashset) <= 1
