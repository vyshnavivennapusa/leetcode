# Last updated: 2/2/2026, 9:14:05 PM
1class Solution(object):
2    def removeDuplicates(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: int
6        """
7        j=0
8        n= len(nums)
9        for i in range(1,len(nums)):
10            if nums[i]!=nums[j]:
11                j+=1
12                nums[j]=nums[i]
13                
14                
15        
16
17        return j+1
18
19