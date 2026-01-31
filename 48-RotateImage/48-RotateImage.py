# Last updated: 1/31/2026, 10:41:17 AM
1class Solution(object):
2    def rotate(self, matrix):
3        """
4        :type matrix: List[List[int]]
5        :rtype: None Do not return anything, modify matrix in-place instead.
6        """
7        n=len(matrix)
8        for i in range(0,n):
9            for j in range(i+1,n):
10                if i!=j:
11                    matrix[j][i],matrix[i][j]=matrix[i][j],matrix[j][i]
12        for i in range(0,n):
13            matrix[i].reverse()
14        
15        