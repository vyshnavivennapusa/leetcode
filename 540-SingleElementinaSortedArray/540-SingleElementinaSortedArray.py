# Last updated: 2/11/2026, 4:53:57 PM
1class Solution(object):
2    def singleNonDuplicate(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: int
6        """
7        n=len(nums)
8        if len(nums)==1:
9            return nums[0]
10        if nums[0]!=nums[1]:
11            return nums[0]
12        if nums[n-1]!=nums[n-2]:
13            return nums[n-1]
14        low=1
15        high=n-2
16        while(low<=high):
17            mid=(low+high)//2
18            if(nums[mid]!=nums[mid-1] and nums[mid]!=nums[mid+1]):
19                return nums[mid]
20            if(mid%2==1 and nums[mid-1]==nums[mid]) or (mid%2==0 and nums[mid+1]==nums[mid]):
21                low=mid+1
22            else:
23                high=mid-1
24        return -1