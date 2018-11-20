#from itertools import groupby

A = [9, 3, 9, 3, 9, 7, 9]    

def solution(A):
    # write your code in Python 3.6
    B = list(set(A))
    for i in range(len(B)):
        C = A.count(B[i])
        if C % 2 != 0:
            D = B[i]
            return(D)
'''
def solution(A):
	for k, v in groupby(sorted(A)):
		if(len(list(v)) == 1):
			return k
	return 0 
'''