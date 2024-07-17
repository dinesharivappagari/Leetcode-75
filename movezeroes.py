# Solving in normal method 
""" class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        n=len(nums)
        i=0
        for j in range(n):
            if nums[j]!=0:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
"""
# Using 2 pointers to solve the problem
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        left = 0
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
        return nums