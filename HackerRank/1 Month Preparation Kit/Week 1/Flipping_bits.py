def to_bin32(i):
    bin = ""
    while i > 0:
        bin = str(i % 2) + bin
        i //= 2
    
    bin = ('0' * (32 - len(bin))) + bin
    return bin

def flippingBits(n):
    # Write your code here
    bin_num = to_bin32(n)
    f_num = ""
    for c in bin_num:
        if c == '1':
            f_num = f_num + "0"
        elif c == '0':
            f_num = f_num + "1"
    return int(f_num, 2)

if __name__ == '__main__':
    n = 2147483647
    res = flippingBits(n)
    print(res)