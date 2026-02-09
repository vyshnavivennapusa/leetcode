# Last updated: 2/9/2026, 5:16:36 PM
1class Solution(object):
2    def searchInsert(self, nums, target):
3        """
4        :type nums: List[int]
5        :type target: int
6        :rtype: int
7        """
8        n=len(nums)
9        high=n-1
10        low=0
11        ans=n
12        if target>nums[high]:
13            return n
14        elif target<nums[low] and nums[low]!=target:
15            return low
16        while(low<=high):
17            mid=(low+high)//2
18            if nums[mid]>=target:
19                ans= mid
20                high=mid-1
21            elif nums[mid]<target:
22                low=mid+1
23        return ans
24           
25        