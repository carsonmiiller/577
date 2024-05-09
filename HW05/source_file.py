import math

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
    num_elements = int(input())
    elements = input().split(" ")
    sorted_elements, num_inversions = CountSort(elements)
    inversions.append(num_inversions)

for inversion in inversions:
    print(inversion)