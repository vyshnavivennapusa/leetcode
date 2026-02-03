# Last updated: 2/3/2026, 6:51:48 PM
1class Solution(object):
2    def majorityElement(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: List[int]
6        """
7        hash={}
8        ans=[]
9        n=len(nums)
10        for i in range(0,len(nums)):
11            if nums[i] in hash:
12                hash[nums[i]]+=1
13            elif nums[i] not in hash:
14                hash[nums[i]]=1
15        for key,value in hash.items():
16            if value > n//3:
17                ans.append(key)
18        return ans
19