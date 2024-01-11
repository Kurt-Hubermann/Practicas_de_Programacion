def sockMerchant(n, ar):
    # Write your code here
    ar.sort()
    previus = 0
    n_pairs = 0
    for i in ar:
        if i == previus:
            n_pairs += 1
            previus = 0
        else:
            previus = i
    return n_pairs

if __name__ == '__main__':
    n = 7
    ar = [1,2,1,2,1,3,2]
    res = sockMerchant(n, ar)
    print(res)