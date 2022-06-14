from sys import stdin

def rowWiseSum(mat, nRows, mCols):
    for i in range(nRows):
        sum = 0
        for j in range(mCols):
            sum += mat[i][j]
        print(sum, end = ' ')
