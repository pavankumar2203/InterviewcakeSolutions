class Max_Stack:

    stack = []
    maxstack = []

    def push(item):
        stack.append(item)
        if not maxstack or item >= maxstack[-1]:
            maxstack.append(item)
        else:
            maxstack.append(maxstack[-1])

    def pop():
        if stack:
            stack.pop()
            return maxstack.pop()

    def getMax():
        if maxstack:
            return maxstack[-1]
