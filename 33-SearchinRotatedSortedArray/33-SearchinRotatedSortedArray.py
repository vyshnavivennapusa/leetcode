# Last updated: 2/10/2026, 9:05:02 PM
1class Solution(object):
2    def search(self, nums, target):
3        """
4        :type nums: List[int]
5        :type target: int
6        :rtype: int
7        """
8        low=0
9        n=len(nums)
10        high=n-1
11        ans=-1                                                      
12        while(low<=high):
13            mid=(low+high)//2
14            if nums[mid]==target:
15                ans=mid
16                break
17            if nums[low]<=nums[mid]:
18                if nums[low]<=target and target<=nums[mid]:
19                    high=mid-1
20                else:
21                    low=mid+1
22            else:
23                if nums[mid]<=target and target<=nums[high]:
24                    low=mid+1
25                else:
26                    high=mid-1
27        return ans
28                                
29        