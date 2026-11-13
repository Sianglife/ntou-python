n = int(input())
d = {}

def min_str(s):
    return "".join(sorted(s))

for i in range(n):
    inp = input()
    m = min_str(inp)
    if m in d:
        d[m].append(inp)
    else:
        d[m] = [inp]

for arr in d.values():
    arr.sort()
l = sorted(d.values(), key=lambda li: (-len(li), li[0]))

# Print
for arr in l:
    for pat in arr:
        print(pat, end=" ")
    print()