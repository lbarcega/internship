arr = [[1,1,1],
       [1,1,1],
       [1,1,1]]
n = 3

def diagonalDifference(arr):
    diagonal1 = 0
    diagonal2 = 0
    for i in range(n):
        diagonal1 += arr[i][i]
        diagonal2 += arr[i][n-i-1]

    abs_difference = abs(diagonal1 - diagonal2)
    
    return abs_difference

print(diagonalDifference(arr))