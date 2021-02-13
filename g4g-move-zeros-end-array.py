'''
Given an array of random numbers, push all the zero’s of a given array to the end of the array.

For example, if the given arrays is {1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0}, it should be changed to {1, 9, 8, 4, 2, 7, 6, 0, 0, 0, 0}.

The order of all other elements should be same. Expected time complexity is O(n) and extra space is O(1).
'''

def left_most_zero(arr, start_idx):
    for x in range(start_idx, len(arr)):
        if arr[x] == 0:
            return x

def left_most_num(arr, start_idx):
    for x in range(start_idx, len(arr)):
        if arr[x] != 0:
            return x

def move_zeros_to_end(arr):
    i = 0 # left-most zero
    j = 0 # left-most number after left-most zero

    while i < len(arr) and j < len(arr):
        i = left_most_zero(arr, i)
        j = left_most_num(arr, i)
        if i is None or j is None:
            break
        arr[i], arr[j] = arr[j], arr[i]
        i += 1

    return arr

if __name__ == "__main__":
    arr = [1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0]
    print(move_zeros_to_end(arr))
