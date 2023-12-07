def lonelyinteger(a):
    # Write your code here
    int_count = {}
    for s in a:
        if s in int_count:
            int_count[s] += 1
        else:
            int_count[s] = 1
    
    for i in int_count:
        if int_count.get(i) == 1:
            return i

if __name__ == '__main__':
    a = [1,2,3,4,3,2,1]
    res = lonelyinteger(a)
    print(res)