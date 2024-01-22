def pageCount(n, p):
    # Write your code here
    if n % 2 == 0: n += 1
    flip = 0
    if p >= (n/2):      
        for i in range(n,1,-2):
            if i == p or (i - 1) == p:
                return flip
            else:
                flip += 1
    else:
        for i in range(1,(n + 1),2):
            if i >= p:
                return flip
            else:
                flip += 1
    return flip

if __name__ == '__main__':
    n = 1
    p = 1
    res = pageCount(n, p)
    print(res)