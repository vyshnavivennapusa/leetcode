# Last updated: 1/29/2026, 10:53:33 PM
1class Solution(object):
2    def isPalindrome(self, x):
3        """
4        :type x: int
5        :rtype: bool
6        """
7        if x < 0:
8            return False
9
10        temp = x
11        rev = 0
12
13        while x > 0:
14            rev = rev * 10 + x % 10
15            x //= 10
16
17        return temp == rev
18        
19        