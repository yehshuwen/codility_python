A = [2, 3, 1, 5]  
'''
def solution(A):
    # write your code in Python 3.6
    B = list(sorted(A))
    C = [x for x in range(1,max(B)+1)]
    D = list(set(C) - set(B))
    return(D[0])
'''

def solution(A):
    if len(A) == 0:
        return 1
    return sum(range(1, len(A)+2)) - sum(A)