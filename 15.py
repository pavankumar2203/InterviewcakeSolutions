def fib(n):

    if n < 0:
        raise  Exception("Invalid input")

    elif n == 0 or n == 1:
        return n

    a = 0
    b = 1
    c = 0

    for i in range(0,n):
        c = a + b
        a = b
        b = c

    return c

if __name__ == "__main__":
    print(fib(4))
