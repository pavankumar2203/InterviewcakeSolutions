def find_unique(arr):

    u = 0
    for i in arr:
        u ^= i

    return u

if __name__ == "__main__":

    arr = [1,2,2,1,3]
    print(find_unique(arr))
    
