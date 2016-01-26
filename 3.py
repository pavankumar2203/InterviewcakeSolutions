def pdt_of_3(arr):

    if len(arr) < 3:
        raise Exception("please check ur input")

    highest = max(arr[0], arr[1])
    lowest = min(arr[0], arr[1])

    highest2 = lowest2  = arr[0] * arr[1]

    highest3 = arr[0] * arr[1] * arr[2]

    for i in range(2, len(arr)):

        highest3 = max(highest3, arr[i] * highest2, arr[i] * lowest2)

        highest2 = max(highest2, arr[i] * highest , arr[i] * lowest)
        lowest2 = min(lowest2, arr[i] * lowest, arr[i] * highest)

        highest = max(highest, arr[i])
        lowest = min(lowest, arr[i])

    return highest3


if __name__ == "__main__":
    arr = [1,10,-5,1,-100]
    print(pdt_of_3(arr))
