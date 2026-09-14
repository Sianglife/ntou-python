n = int(input())
    

def draw(i, reverse=False):
    # print(i)
    print(" " * (n - 1 - i), end="")
    print("*", end="")
    if i == 0:
        print("")
        return
    print(" " * (2 * i - 1), end="")
    print("*", end="")
    print("")



if n <= 1:
    print("Invalid input")
else:
    for i in range(0, n):
        draw(i)
    for i in range(n - 2, -1, -1):
        draw(i, True)