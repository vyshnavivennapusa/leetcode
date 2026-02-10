# Last updated: 2/10/2026, 9:11:05 PM
1class Solution(object):
2    def search(self, nums, target):
3        """
4        :type nums: List[int]
5        :type target: int
6        :rtype: bool
7        """
8       
9 
10        low=0
11        n=len(nums)
12        high=n-1
13        ans=-1   
14
15        while(low<=high):
16            mid=(low+high)//2
17            if nums[mid]==target:
18                return True
19            if (nums[low]==nums[mid]==nums[high]):
20                low+=1
21                high-=1
22                continue
23            if nums[low]<=nums[mid]:
24                if nums[low]<=target and target<=nums[mid]:
25                    high=mid-1
26                else:
27                    low=mid+1
28            else:
29                if nums[mid]<=target and target<=nums[high]:
30                    low=mid+1
31                else:
32                    high=mid-1
33        return False
34        
35                                
36        