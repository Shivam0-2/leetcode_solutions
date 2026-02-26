#Problem link: https://leetcode.com/problems/spiral-matrix/
#Approach: We can use four pointers to keep track of the boundaries of the matrix. We start from the top-left corner and move right, then down, then left, and then up, while updating the boundaries accordingly. We continue this process until we have traversed all the elements in the matrix.
#Time Complexity: O(m*n) where m is the number of rows and n is the

def spiralOrder(self, matrix):

        result = []
        left , right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)
        while left<right and top<bottom:
            for i in range(left,right):
                result.append(matrix[top][i])
            top+=1

            for i in range(top, bottom):
                result.append(matrix[i][right-1])
            right -=1
            if not (left < right and top < bottom):
                break

            for i in range(right-1,left-1,-1):
                result.append(matrix[bottom-1][i])
            bottom-=1

            for i in range(bottom-1,top-1,-1):
                result.append(matrix[i][left])
            left+=1
        return result