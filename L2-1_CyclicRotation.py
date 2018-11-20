A = [3, 8, 9, 7, 6]
K = 3
def solution(A, K):
    # write your code in Python 3.6
    if not len(A):
        return A
    for i in range(K):
        A.insert(0,A[-1])
        del A[-1]
    return(A)