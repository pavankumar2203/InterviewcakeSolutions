def get2movies(arr, time):

    s = set()

    for i in arr:
        remaining = time - i
        if remaining in s:
            return i,remaining
        s.add(i)

    return None

if __name__ == "__main__":

    arr = [2,3,2]
    print(get2movies(arr,5))
    
