def plusMinus(arr):
    n_elements = len(arr)
    positive = 0 #Amount of positive numbers
    zero = 0 #Amount of zeros
    negative = 0 #Amount of negative numbers
    for i in arr:
        if i > 0:
            positive += 1
        elif i < 0:
            negative += 1
        elif i == 0:
            zero += 1

    print(positive/n_elements) #Ratio od positive values
    print(negative/n_elements) #Ratio of negative values
    print(zero/n_elements) #Ratio of zero values

if __name__ == '__main__':
    arr = [1,1,0,-1,-1]
    plusMinus(arr)