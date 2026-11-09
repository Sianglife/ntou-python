def quickSort(l):
    pivot = l[0]
    less = []
    equi = []
    more = []
    for item in l.copy():
        if item > pivot:
            more.append(item)
        elif item < pivot:
            less.append(item)
        else:
            equi.append(item)
    if len(more) > 1:
        more = quickSort(more)
    if len(less) > 1:
        less = quickSort(less)
    return less + equi + more



l = list(map(int, input().split()))

# print(quickSort(l))

for i in quickSort(l):
    print(i, end=" ")