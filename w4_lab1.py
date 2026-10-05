def carry_count(a, b, c):
    if a == 0 and b == 0:
        return 0
    # print(f"a: {a}, b: {b}, c: {c}")
    if (a % 10) + (b % 10) + c >= 10:
        return carry_count(a // 10, b // 10, 1) + 1
    else:
        return carry_count(a // 10, b // 10, 0)

# print(carry_count(99, 9, 0))
    
while True:
    inp = input()
    if inp == "0 0":
        exit()
    a, b = map(int, inp.split())
    if int(a) == 0 and int == 0:
        exit()
    carry = carry_count(a, b, 0)
    if carry == 0:
        print("No carry operation.")
    elif carry == 1:
        print("1 carry operation.")
    else:
        print(f"{carry} carry operations.")