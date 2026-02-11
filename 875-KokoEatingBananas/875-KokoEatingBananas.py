# Last updated: 2/11/2026, 10:18:50 PM
1class Solution(object):
2    def minEatingSpeed(self, piles, h):
3        """
4        :type piles: List[int]
5        :type h: int
6        :rtype: int
7        """
8        import math
9        low=1
10        high=max(piles)
11        s=0
12        while(low<=high):
13            s=0
14            mid=(low+high)//2
15            for i in range(0,len(piles)):
16                s+=(piles[i]+mid-1)//mid
17            if s>h:
18                low=mid+1
19            else:
20                high=mid-1
21        return low
22