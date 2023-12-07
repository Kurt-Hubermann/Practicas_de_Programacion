def matchingStrings(strings, queries):
    # Write your code here
    str_count = {}
    for s in strings:
        if s in str_count:
            str_count[s] += 1
        else:
            str_count[s] = 1
    
    q_count = []
    for q in queries:
        if q in str_count:
            q_count.append(str_count.get(q))
        else:
            q_count.append(0)
    
    return q_count

if __name__ == '__main__':
    strings = ['ab','ab','abc']
    queries = ['ab','abc','bc']
    res = matchingStrings(strings,queries)
    print(res)