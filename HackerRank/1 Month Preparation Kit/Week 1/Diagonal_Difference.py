def diagonalDifference(arr):
    # Write your code here
    l2r_sum = 0
    r2l_sum = 0
    c = (len(arr)-1)
    for i in range(0,(len(arr))):
            l2r_sum += (arr[i][i])
            r2l_sum += (arr[i][c])
            c -= 1
    
    return abs(l2r_sum - r2l_sum)

if __name__ == '__main__':
    arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
    res = diagonalDifference(arr)
    print(res)