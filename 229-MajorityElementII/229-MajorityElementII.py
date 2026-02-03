# Last updated: 2/3/2026, 7:24:46 PM
1class Solution(object):
2    def majorityElement(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: List[int]
6        """
7        cnt1=0
8        el1=None
9        cnt2=0
10        el2=None
11        n=len(nums)
12        for i in range(0,len(nums)):
13            if cnt1==0 and nums[i]!=el2:
14                cnt1=1
15                el1=nums[i]
16            elif cnt2==0 and nums[i]!=el1:
17                cnt2=1
18                el2=nums[i]
19            elif nums[i]==el1:
20                cnt1+=1
21            elif nums[i]==el2:
22                cnt2+=1
23            else:
24                cnt1-=1
25                cnt2-=1
26        cnt1=0
27        cnt2=0
28        for num in nums:
29            if num==el1:
30                cnt1+=1
31            if num==el2:
32                cnt2+=1
33        ans=[]
34        if cnt1>n//3:
35            ans.append(el1)
36        if cnt2>n//3:
37            ans.append(el2)
38        return ans
39