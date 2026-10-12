def gcd(a, b):
    if b > a:
        a, b = b, a
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

while True:
    inp_s = input().strip()
    if inp_s == "0":
        break
    n = int(inp_s)
    g = 0
    for i in range(1, n):
        for j in range(i+1, n+1):
            g += gcd(i, j)
    print(g)