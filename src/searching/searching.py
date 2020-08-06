
def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        # find middle
        middle = (low + high) // 2
        # check if target is middle
        guess = arr[middle]
        if guess == target:
            return middle

        # check if target is greater
        if target > guess:
            low = middle + 1

        # check if target is lesser
        else:
            high = middle - 1

    return -1  # not found


