cnt = 0

def end():
    print(f"You guessed {cnt} times.")
    exit()

# phase 1
try: 
    n = float(input())
except ValueError:
    print("Error: please enter a number")
    end()

if int(n) != n:
    print("Error: please enter an integer")
    end()
else:
    n = int(n)
    
if n < 0 or n > 50:
    print("Error: number out of range")
    end()

while True:
    inp = input()
    try: 
        inp = float(inp)
    except ValueError:
        cnt += 1
        print("Error: please enter a number")
        continue

    if int(inp) != inp:
        cnt += 1
        print("Error: please enter an integer")
        continue
    else:        
        inp = int(inp)

    if inp < 0 or inp > 50:
        cnt += 1
        print("Error: number out of range")
        continue

    if inp > n:
        cnt += 1
        print("You are too high!")
        continue

    if inp < n:
        cnt += 1
        print("You are too low!")
        continue

    if inp == n:
        cnt += 1
        print("You got it!")
        end()



