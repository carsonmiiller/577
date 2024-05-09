import math
import numpy as np

def MergeCount(A, B):
    S = []
    c = 0

    while len(A) > 0 or len(B) > 0:
        if len(A) == 0:
            S.append(B[0])
            B = B[1:len(B)]
        elif len(B) == 0:
            S.append(A[0])
            A = A[1:len(A)]
        elif int(A[0]) <= int(B[0]):
            S.append(A[0])
            A = A[1:len(A)]
        else:
            S.append(B[0])
            B = B[1:len(B)]
            c += len(A)

    return S, c

def CountSort(A):
    if len(A) == 1:
        return A, 0
    
    A_1, c_1 = CountSort(A[0:math.ceil(len(A)/2)])
    A_2, c_2 = CountSort(A[math.ceil(len(A)/2):len(A)])
    A, c = MergeCount(A_1, A_2)

    return A, (c + c_1 + c_2)

instances = int(input())
inversions = []
for i in range(instances):
    num_pairs = int(input())
    # create empty 2d array with num_pairs rows and 2 columns
    pairs = [[] for y in range(num_pairs)]

    # read in p
    for j in range(num_pairs):
        pairs[j].append(int(input()))

    # read in q
    for j in range(num_pairs):
        pairs[j].append(int(input()))

    # sort 1st row of pairs, and corresponding 2nd row
    pairs = np.array(sorted(pairs, key=lambda x: x[0]))

    second_column = pairs[:,1]
    sorted_second_column, num_inversions = CountSort(second_column)
    inversions.append(num_inversions)

for inversion in inversions:
    print(inversion)