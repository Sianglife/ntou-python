stu = dict()

def query(idn):
    if idn in stu:
        print(stu[idn][0], stu[idn][1])
    else:
        print("Not found")
    

n = int(input())
for i in range(n):
    idn, name, score = input().split()
    stu[idn] = (name, score)

# print(stu)

q = int(input())
for i in range(q):
    idn = input().strip()
    query(idn)
