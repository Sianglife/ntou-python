def sum(*nums) :
    s = 0
    for i in nums:
        if (i % 2) == 0:
            s += i
    return s



while True:
    inp_s = input()
    if inp_s.strip() == "END":
        break
    arr = list(map(int, (inp_s.split())))

    print(sum(*arr))