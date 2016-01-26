def validate_brackets(s):

    stack = []
    s = list(s)

    brackets = { '(' : ')', '[' : ']', '{' : '}' }

    for c in s:
        print(stack)
        if c in ['(', '[', '{']:
            stack.append(c)
        else:
            if not stack:
                return False
            else:
                item = stack.pop()
                if c != brackets[item]:
                    return False

    if stack:
	    return False
    else:
        return True

if __name__ == "__main__":
    print(validate_brackets("(){}{"))
