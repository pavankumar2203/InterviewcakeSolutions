instack = []
outstack = []

def enque(item):
    instack.append(item)

def deque():

    if outstack:
        return outstack.pop()
    else:
        for i in range(0,len(instack)):
            outstack.append(instack.pop())

        return outstack.pop()

if __name__ == "__main__":
    enque("a")
    enque("b")
    enque("c")
    print("1", instack)

    print(deque())
    print(instack)
    print(outstack)
    enque("d")
    enque("e")

    print(deque())
    print(instack)
    print(outstack)

    print(deque())
    print(deque())
    print(deque())
    print(instack)
    print(outstack)
