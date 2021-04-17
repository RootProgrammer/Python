# import sys
N = 4
M = 4

# Function to find max element
# mat[][] : 2D array to find max element


def findMax(mat):

    # Initializing max element as INT_MIN
    maxElement = 0 #-sys.maxsize - 1

    # checking each element of matrix
    # if it is greater than maxElement,
    # update maxElement
    for i in range(N):
        for j in range(M):
            if (mat[i][j] > maxElement):
                maxElement = mat[i][j]

    # finally return maxElement
    return maxElement


# Driver code
if __name__ == '__main__':

    # matrix
    mat = [[1, 2, 3, 4],
           [25, 6, 7, 8],
           [9, 10, 11, 12],
           [13, 14, 15, 16]]
    print(findMax(mat))
