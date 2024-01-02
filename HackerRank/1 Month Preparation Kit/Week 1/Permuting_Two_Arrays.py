def twoArrays(k, A, B):
    # Write your code here
    A.sort()
    B.sort(reverse=True)
    for i in range(len(A)):
        if (A[i] + B[i]) < k:
            return 'NO'
    return 'YES'

if __name__ == '__main__':
    A = [1,2,2,1]
    B = [3,3,3,4]
    k = 5
    res = twoArrays(k, A, B)
    print(res)
    A = [1,2,3]
    B = [9,8,7]
    k = 5
    res = twoArrays(k, A, B)
    print(res)