# Last updated: 2/3/2026, 10:07:32 PM
1class Solution(object):
2    def findDisappearedNumbers(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: List[int]
6        """
7        
8        n=len(nums)
9        a=[]
10        s=[x for x in range(1,n+1)]
11        mis=list(set(s)-set(nums))
12        return mis
13
14
15