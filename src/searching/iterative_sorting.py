# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        # TO-DO: find next smallest element
        smallest_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        # TO-DO: swap
        if smallest_index != i:
            arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
            # original = arr[i]
            # toswap = arr[smallest_index]

            # arr[i] = toswap
            # arr[smallest_index] = original
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    sorted_i = len(arr) - 1
    # loop through indexes 0 - ???
    while sorted_i > 0:
        for i in range(0, sorted_i):
            # compare neighbors
            if arr[i] > arr[i+1]:
                # swap if neighbors out of order (with respect to each other)
                arr[i], arr[i+1] = arr[i+1], arr[i]
            
        # increment 1 index at a time
        sorted_i -= 1
        
    # we are done IF a loop results in NO swaps

    return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr
