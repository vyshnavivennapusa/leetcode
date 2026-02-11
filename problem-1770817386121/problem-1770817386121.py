# Last updated: 2/11/2026, 7:13:06 PM
1class Solution(object):
2    def findPeakElement(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: int
6        """
7        n=len(nums)
8     
9    
10        low=1
11        high=n-2
12        if len(nums)==1:
13                return 0
14        
15        if nums[0]>nums[1]:
16            return 0
17        if nums[n-1]>nums[n-2]:
18            return n-1
19        while(low<=high):
20            mid=(low+high)//2
21           
22            if nums[mid-1]<nums[mid] and nums[mid]>nums[mid+1]:
23                return mid
24                
25            elif nums[mid-1]<nums[mid]:
26                low=mid+1
27            else:
28                high=mid-1
29        return -1
30