def permute(prefix, st):
    n = len(st)
    if n == 0:
        print(prefix)
    else:
        for i in range(0, n):
            permute(st[i] + prefix, st[0:i] + st[i+1:])

if __name__ == "__main__":

    permute("", "abc")
