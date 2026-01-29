# Last updated: 1/29/2026, 10:50:36 PM
1class Solution(object):
2    def twoSum(self, nums, target):
3        """
4        :type nums: List[int]
5        :type target: int
6        :rtype: List[int]
7        """
8        hash={}
9        for i in range(0,len(nums)):
10            n= target - nums[i]
11            if n  in hash:
12                return([i,hash[n]])
13                break
14            else:
15                hash[nums[i]]=i
16
17
18        