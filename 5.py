def makechange(arr, amt):
    ways = [0 for x in range(0,amt+1)]
    ways[0] = 1
    for i in arr:
        for j in range(i, amt+1):
            ways[j] += ways[j - i]

    return ways[amt]

if __name__ == "__main__":
    arr = [1,3,2]
    print(makechange(arr, 4))
    
