#Problem link: https://leetcode.com/problems/set-matrix-zeroes/
#Approach: We can use the first row and first column of the matrix to keep track of which rows and columns should be set to zero. We iterate through the matrix and whenever we find a zero, we mark the corresponding row and column in the first row and first column. After that, we iterate through the matrix again and set the elements to zero based on the markings in the first row and first column. Finally, we handle the first row and first column separately if they were marked.
#Time Complexity: O(m*n) where m is the number of rows and n is the number of columns in the matrix.    


def setZeroes(self, matrix):
        row, col =len(matrix), len(matrix[0])
        temp = False

        for i in range(row):
            for j in range(col):
                if matrix[i][j]==0:
                    matrix[0][j]=0
                    if i>0:
                        matrix[i][0] =0
                    else: temp= True
        for i in range(1,row):
            for j in range(1,col):
                if matrix[0][j] == 0 or matrix[i][0]== 0:
                    matrix[i][j]= 0

        if matrix[0][0]== 0:
            for i in range(row):
                matrix[i][0]=0
        if temp:
            for j in range(col):
                matrix[0][j]=0