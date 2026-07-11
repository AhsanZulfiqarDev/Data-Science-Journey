import modules
from modules import checkIfNotNumeric

result = modules.addAllNumerics(10, 20, 30)
print(result)


def findMin(L, startIndx=0):
    if not L:
        raise ValueError("List cannot be empty")

    m = L[startIndx]
    idx = startIndx

    for i in range(startIndx + 1, len(L)):
        if L[i] < m:
            m = L[i]
            idx = i

    return m, idx


a, b = findMin([10, 20, 30, 5, 40], 0)
print(a, b)


def swapValues(L, idx1, idx2):
    L = list(L)
    tmp = L[idx1]
    L[idx1] = L[idx2]
    L[idx2] = tmp
    return L


swappedList = swapValues([10, 20, 30, 5, 40], 0, 3)
print(swappedList)


def sortList(L):
    if not checkIfNotNumeric(*L):
        print("List contains non-numeric values. Cannot sort.")
        return None

    sorted_values = list(L)
    for c in range(len(sorted_values)):
        _, idx = findMin(sorted_values, c)
        sorted_values = swapValues(sorted_values, c, idx)

    return sorted_values


sortedList = sortList([10, 20, 30, 5, 40])
print(sortedList)