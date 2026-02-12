# Last updated: 2/12/2026, 6:18:03 PM
1class Solution(object):
2    def smallestDivisor(self, nums, threshold):
3        """
4        :type nums: List[int]
5        :type threshold: int
6        :rtype: int
7        """
8        import math
9        n=len(nums)
10        low=1
11        ans=n
12        high=max(nums)
13        while(low<=high):
14            s=0
15            mid=(low+high)//2
16            for i in range(n):
17                s+=(nums[i]+mid-1)//mid
18            if s<=threshold:
19                ans=mid
20                high=mid-1
21            else:
22                low=mid+1
23        return ans