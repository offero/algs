'''
You are a professional robber planning to rob houses along a street. Each house
has a certain amount of money stashed. All houses at this place are arranged in
a circle. That means the first house is the neighbor of the last one. Meanwhile,
adjacent houses have a security system connected, and it will automatically
contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house,
return the maximum amount of money you can rob tonight without alerting the
police.

Example 1:
Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

Example 2:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 3:
Input: nums = [1,2,3]
Output: 3
'''
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums)

        bs1 = [nums[0]] # best given first house chosen
        bs0 = [0] # best given first house skipped
        for i in range(1, len(nums)-1):
            bs1.append(max(
                (i-1 >= 0 and bs1[i-1] or 0), # don't rob the house because we robbed the last one
                (i-2 >= 0 and bs1[i-2] or 0) + nums[i], # rob this one
            ))
            bs0.append(max(
                (i-1 >= 0 and bs0[i-1] or 0),
                (i-2 >= 0 and bs0[i-2] or 0) + nums[i],
            ))

        bs1.append(bs1[-1])
        bs0.append(bs0[-2] + nums[-1])
        #print(bs0, bs1)
        return max(bs0[-1], bs1[-1])