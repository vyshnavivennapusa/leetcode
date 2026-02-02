# Last updated: 2/2/2026, 10:39:31 PM
1class Solution(object):
2    def singleNumber(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: int
6        """
7        hash={}
8        for i in range(0,len(nums)):
9            if nums[i] in hash:
10                hash[nums[i]]+=1
11            elif nums[i] not in hash:
12                hash[nums[i]] = 1
13        for key,value in hash.items():
14            if value == 1:
15                return key
16                
17        