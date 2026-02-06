# Last updated: 2/6/2026, 7:15:09 PM
1class Solution(object):
2    def plusOne(self, digits):
3        """
4        :type digits: List[int]
5        :rtype: List[int]
6        """
7        n=len(digits)
8        a=1
9        for i in range(n-1,-1,-1):
10            digits[i]+=a
11            s=digits[i]
12            a=digits[i]//10
13            digits[i]=digits[i]%10
14        if a>=1 :
15                digits.insert(0,a)
16        return digits
17
18        