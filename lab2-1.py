n = int(input())

def draw(n):
    cnt = 0
    for row in range(1, n+1):
        for col in range(row):
            cnt += 1
            print(cnt, end="")
            if col == row - 1:
                print("") # next line
            else:
                print(" ", end="")



if n <= 0:
    print("Invalid input")
else:
    draw(n)