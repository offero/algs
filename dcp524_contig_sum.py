'''
DCP 524 Max contiguous sum in O(n) time

Given an array of numbers, find the maximum sum of any contiguous subarray of the array.

For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137, since we would
take elements 42, 14, -5, and 86.

Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would not take any elements.

Do this in O(N) time.
'''


def v1(nums):
    best_seg_sum = 0
    best_seg = (0, 0)
    cur_seg_sum = 0
    cur_seg = [0, 0]

    for i, x in enumerate(nums):
        if cur_seg_sum <= 0:
            cur_seg[0] = i
            cur_seg_sum = 0

        cur_seg[1] = i
        cur_seg_sum += x

        if cur_seg_sum >= best_seg_sum:
            best_seg_sum = cur_seg_sum
            best_seg = tuple(cur_seg)

    return best_seg_sum, best_seg


examples = [
    [34, -50, 42, 14, -5, -6], # 42+14
    [34, -50, 42, 14, -5, 86], # 42+14-5+86
    [-5, -10, 100, -90, 5, 7], # 100
    [1, 1, 1, 1, 1, -1, -2], # 1+1+1+1+1
    [-6, -1, -2, -3, -4, -5, -6], # 0
]


def main():
    for nums in examples:
        print('nums', nums)
        print('max contig sum', v1(nums))
        print('')


if __name__ == "__main__":
    main()

