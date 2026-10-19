from decimal import Decimal, ROUND_HALF_UP

n = int(input())

name_list = []
score_list = []

def load():
    inp = input().split(',')
    if len(inp) != 2:
        print("Error: invalid data format")
        return None

    try:
        if int(inp[1]) != float(inp[1]):
            print("Error: invalid score")
            return None
        else:
            score = int(inp[1])
            name = inp[0]
    except ValueError:
        print("Error: invalid score")
        return None
        

    if score < 0 or score > 100:
        print("Error: invalid score")
        return None

    name_list.append(name)
    score_list.append(score)
    print("OK")
    # print(score)

for i in range(n):
    load()

if len(score_list) == 0:
    print("No valid scores")
    exit()
else:
    # print(d.values())
    total = sum(score_list)
    average = Decimal(total) / Decimal(len(score_list))
    average = average.quantize(
        Decimal("0.01"),
        rounding=ROUND_HALF_UP
    )

    print(f"Average score: {average:.2f}")

