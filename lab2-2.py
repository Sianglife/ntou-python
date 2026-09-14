n = int(input())
l = list(map(int, input().split()))

for i in l:
    print(i, end=" ")

print("")

# sort
for i in range(0, n):
    for j in range(i, n):
        if l[i] > l[j]:
            l[i], l[j] = l[j], l[i]


for i in l:
    print(i, end=" ")
