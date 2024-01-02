def pangrams(s):
    # Write your code here
    s = (s.lower()).replace(" ", "")
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    count = [0] * 26
    for l in s:
        index = alphabet.index(l)
        count[index] += 1
    if 0 in count:
        return "not pangram"
    else:
        return "pangram"

if __name__ == '__main__':
    ex_1 = "We promptly judged antique ivory buckles for the next prize"
    ex_2 = "We promptly judged antique ivory buckles for the prize"
    res = pangrams(ex_1)
    print(res)
    res = pangrams(ex_2)
    print(res)