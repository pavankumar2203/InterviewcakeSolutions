def find_rotation_point(arr):

    low = 0
    high = len(arr)

    while(low <= high and arr[low] >= arr[high]):

        mid = low + (( high - low)/2)

		if arr[low] > arr[mid]:
            high = mid
        elif arr[low] < arr[mid]:
            low = mid + 1
        else:
            low += 1

    return low
            
