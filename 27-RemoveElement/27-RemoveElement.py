# Last updated: 2/2/2026, 9:32:30 PM
1class Solution(object):
2    def removeElement(self, nums, val):
3        """
4        :type nums: List[int]
5        :type val: int
6        :rtype: int
7        """
8
9        i=0
10        for j in range(0,len(nums)):
11            if nums[j]!=val:
12                nums[i]=nums[j]
13                i+=1
14        return i
15