def birthday(s, d, m):
    # Write your code here
    w = 0
    b = 0
    while True:
        e = b + (m)
        if e <= (len(s)):
            t_sum = sum(s[b:e])
            if t_sum == d:
                w += 1
            b += 1
        else:
            return w

if __name__ == '__main__':
    s = [2,2,1,3,2]
    d = 4
    m = 2
    res = birthday(s, d, m)
    print(res)