# Last updated: 3/4/2026, 5:48:01 PM
1class Solution(object):
2    def removeOuterParentheses(self, s):
3        """
4        :type s: str
5        :rtype: str
6        """
7        depth=0
8        result=[]
9        for char in s:
10            if char == "(":
11                depth+=1
12                if depth>1:
13                    result.append(char)
14            else:
15                depth-=1
16                if depth>0:
17                    result.append(char)
18        return ''.join(result)
19        
20        