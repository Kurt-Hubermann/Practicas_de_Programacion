def sum(a, b): 
    res = 0
    ar = a.copy()
    ar.pop(b)
    for i in ar:
        res += i
    return res

def miniMaxSum(arr):
    # Write your code here
    arr.sort()
    minSum = sum(arr, -1)
    maxSum = sum(arr, 0)
    print(minSum, maxSum)

if __name__ == '__main__':
    arr = [1,3,5,7,9]
    miniMaxSum(arr)