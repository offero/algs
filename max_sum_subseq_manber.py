'''
Maximum Consecutive Subsequence
Udi Manber section 5.8

Given a sequence x1, x2, ..., xn of real numbers (not necessarily positive) find a subsequence xi, xi+1, ..., xj (of consecutive elements) such that the sum of the numbers in it is maximum over all subsequences of consecutive elements.

Example Sequence: (2, -3, 1.5, -1, 3, -2, -3, 3) Max: (1.5, -1, 3) with sum 3.5.

If all the numbers are negative, then the max subsequence is empty (by definition, the sum of the empty subsequence is 0.

We would like to have an algorithm that solves the problem and reads the sequence in order only once.
'''

def max_sum_consec_subseq(arr):
  global_max = 0
  suffix_max = 0
  for i in range(len(arr)):
    potential_max = suffix_max + arr[i]
    # either we have a new max
    # or we start a new suffix
    if potential_max > global_max:
      global_max = potential_max
      suffix_max = potential_max
    elif potential_max > 0:
      suffix_max = potential_max
    else:
      suffix_max = 0
  return global_max

print(max_sum_consec_subseq([2, -3, 1.5, -1, 3, -2, -3, 3]))
print(max_sum_consec_subseq([1,1,1]))
print(max_sum_consec_subseq([-1, -2, -3]))
