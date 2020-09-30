def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1  # not found

# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # Your code here
    nani = 0
    wtf = len(arr) - 1

    while nani <= wtf:
        midpoint = (nani + wtf) // 2

        if arr[midpoint] == target:
            return midpoint

        if arr[midpoint] < target:
            nani = midpoint +1
        else:
            wtf = midpoint -1
    return -1  # not found
