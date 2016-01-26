def mult(arr):

    p = 1
    res = [1 for x in range(0, len(arr))]
    for i in range(0, len(arr)):
        res[i] = p
        p *= arr[i]

    p = 1
    for i in range(len(arr)-1, -1, -1):
        res[i] *= p
        p *= arr[i]

    return res


if __name__ == "__main__":

    arr = [2,4,10]
    print(mult(arr))
