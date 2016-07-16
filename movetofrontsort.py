from __future__ import (absolute_import, division, print_function, unicode_literals)


'''
You have an array of unique integer numbers and only one operation: MoveToFront(x) that moves
given number to the beginning of the array.  Write a program to sort the array using the minimum
possible number of MoveToFront() calls.
'''

def moveToEndSort(arr):
    n = len(arr)

    i = 0
    while i < n:
        # if arr[i] is < any element, move to end
        j = i+1
        moved = False

        # print(arr)
        while j < n:
            if arr[i] <= arr[j]:
                # move to end
                arr.append(arr[i])
                del arr[i]

                moved = True
                break

            j += 1

        if not moved:
            i += 1

    return arr

def main():
    arr = [6, 3, 2, 7, 1, 4]
    print(moveToEndSort(arr))

if __name__ == '__main__':
    main()
