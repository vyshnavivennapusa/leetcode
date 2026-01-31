# Last updated: 1/31/2026, 10:21:01 AM
1class Solution(object):
2    def rotate(self, matrix):
3        """
4        :type matrix: List[List[int]]
5        :rtype: None Do not return anything, modify matrix in-place instead.
6        """
7        n=len(matrix)
8        ans=[[0]*n for x in range(0,n)]
9        for i in range(0,n):
10            for j in range(0,n):
11                ans[j][n-1-i]=matrix[i][j]
12        for i in range(0,n):
13            for j in range(0,n):
14                matrix[i][j]=ans[i][j]
15        
16        