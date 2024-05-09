def popSolMatrix(weightValuePairs, sol_matrix):
    for i in range(1, len(sol_matrix)):
        for j in range(1, len(sol_matrix[0])):
            if weightValuePairs[i-1][0] <= j:
                sol_matrix[i][j] = max(sol_matrix[i-1][j], sol_matrix[i-1][j-weightValuePairs[i-1][0]] + weightValuePairs[i-1][1])
            else:
                sol_matrix[i][j] = sol_matrix[i-1][j]
    return sol_matrix

instances = int(input())
for i in range(instances):
    num_items, capacity = map(int, input().split(" "))
    sol_matrix = [[0 for x in range(capacity + 1)] for y in range(num_items + 1)]
    weightValuePairs = []
    for j in range(num_items):
        weight, value = map(int, input().split(" "))
        weightValuePairs.append((weight, value))
    print(popSolMatrix(weightValuePairs, sol_matrix)[num_items][capacity])