# Last updated: 2/2/2026, 8:30:03 PM
1class Solution(object):
2    def subarraySum(self, nums, k):
3        """
4        :type nums: List[int]
5        :type k: int
6        :rtype: int
7        """
8        presum=0
9        cnt=0
10        hash={}
11        hash[0]=1
12        for i in range(0,len(nums)):
13            presum+=nums[i]
14           
15            if presum-k in hash:
16                cnt+=hash[presum-k]
17            if presum not in hash:
18                hash[presum]=1
19            elif presum in hash:
20                hash[presum]+=1
21        return cnt
22
23        