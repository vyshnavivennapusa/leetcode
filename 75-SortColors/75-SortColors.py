# Last updated: 2/6/2026, 6:56:44 PM
1class Solution(object):
2    def sortColors(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: None Do not return anything, modify nums in-place instead.
6        """
7        n=len(nums)
8        low=0
9        mid=0
10        high=n-1
11        while(mid<=high):
12            if nums[mid]==0:
13                nums[low],nums[mid]=nums[mid],nums[low]
14                mid+=1
15                low+=1
16
17            elif nums[mid]==1:
18                mid+=1
19            else:
20                nums[mid],nums[high]=nums[high],nums[mid]
21                high-=1
22        return nums
23