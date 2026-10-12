n, dsq = map(int, input().split())
dets = []

for i in range(n):
    x, y, z, pw = map(int, input().split())
    dets.append((x, y, z, pw))

def distance(a, b):
    # print(a[0], a[1], a[2], a[3])
    # print(b[0], b[1], b[2], b[3])
    return (a[0] - b[0])**2 + (a[1] - b[1])**2 + (a[2] - b[2])**2


intes = []
for idx, det1 in enumerate(dets):
    # print(f"len: {len(dets[idx+1:])} idx: {idx}")
    for det2 in dets[idx+1:]:
        if det1[3] == det2[3]:
            continue
        if distance(det1, det2) <= dsq:
            sorted([det1, det2])[0]
            intes.append((sorted([det1, det2])[0], sorted([det1, det2])[1]))
intes.sort()

print(f"Interference Pairs: {len(intes)}")
for inte in intes:
    print(f"{inte[0]} <-> {inte[1]}")


# print(intes, len(set(intes)))