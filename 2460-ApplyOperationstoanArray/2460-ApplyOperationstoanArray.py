# Last updated: 2/2/2026, 9:58:54 PM
1class Solution(object):
2    def applyOperations(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: List[int]
6        """
7        
8        for i in range(0,len(nums)-1):
9            if nums[i]==nums[i+1]:
10                nums[i]=nums[i]*2
11                nums[i+1]=0
12        j=0
13        for k in range(0,len(nums)):
14            if nums[k]!=0:
15                nums[j],nums[k]=nums[k],nums[j]
16                j+=1
17        return nums
18
19
20        