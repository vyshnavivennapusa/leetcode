# Last updated: 2/10/2026, 9:40:49 PM
1class Solution(object):
2    def findMin(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: int
6        """
7        low=0
8        n=len(nums)
9        high=n-1
10        mini=float('inf')
11        while(low<=high):
12            mid=(low+high)//2
13            if nums[low]<=nums[mid]:
14                mini=min(mini,nums[low])
15                low=mid+1
16            else:
17                mini=min(mini,nums[mid])
18                high=mid-1
19        return mini
20        