M1 = [[1,2,3,4]]
M2 = [[2,3,4,5]]


def addMatrices(M1,M2):
    for i in range(len(M1)):
        L3= []
        for j in range(len(M1[i])):
            L3.append(M1[i][j]+M2[i][j])
    return L3

print(addMatrices(M1,M2))