# Last updated: 2/2/2026, 9:37:02 PM
1class Solution(object):
2    def moveZeroes(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: None Do not return anything, modify nums in-place instead.
6        """
7        i=0
8        for j in range(0,len(nums)):
9                if nums[j]!=0:
10                    nums[i],nums[j]=nums[j],nums[i]
11                    i+=1
12