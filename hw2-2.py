l = []

def calc_mid():
    leng = len(l)

    # sort
    for i in range(0, leng):
        for j in range(i, leng):
            if l[i] > l[j]:
                l[i], l[j] = l[j], l[i]

    # get mid
    if (leng % 2) == 1:
        # odd
        return l[(leng - 1) // 2]
    else:
        # even
        return (l[leng // 2] + l[leng // 2 - 1]) // 2

    
while True:
    try:
        n = input()
        l.append(int(n))
        print(calc_mid())
    except EOFError:
        break
