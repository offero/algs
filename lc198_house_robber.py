'''
198. House Robber

You are a professional robber planning to rob houses along a street. Each house
has a certain amount of money stashed, the only constraint stopping you from
robbing each of them is that adjacent houses have security systems connected and
it will automatically contact the police if two adjacent houses were broken into
on the same night.

Given an integer array nums representing the amount of money of each house,
return the maximum amount of money you can rob tonight without alerting the
police.

Example 1:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 2:
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
'''
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        bs = [0, 0]
        for i in range(0, len(nums)):
            #bs.append(max(
            bs[i%2] = max(
                bs[(i-1)%2],
                bs[i%2] + nums[i],
                #(i-1 >= 0 and bs[i-1] or 0), # don't rob the house because we robbed the last one
                #(i-2 >=0 and bs[i-2] or 0) + nums[i], # rob this one
            )
        #return bs[-1]
        return bs[(len(nums)-1)%2]