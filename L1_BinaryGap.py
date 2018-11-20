# BinaryGap

def solution(N):
    # write your code in Python 3.6
    binary = list(bin(N)[2:])
    gap = []
    a = [index for index, value in enumerate(binary) if value =='1']
    for i in range(len(a)):
        if i < len(a)-1:
            b = a[i+1]-a[i]-1
            gap.append(b)
        if len(a) == 1:
            b = 0
            gap.append(b)
    return(max(gap))