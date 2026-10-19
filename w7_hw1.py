class Account:
    
    def __init__(self, name, balance):
        self.name = name
        self.balance = int(balance)

    def deposit(self, amount):
        # self.getBalance()
        # print(f"d: {amount}")
        self.balance += int(amount)
        # self.getBalance()

    def withdraw(self, amount):
        # self.getBalance()
        # print(f"w: {amount}")
        if int(amount) > self.balance:
            print("Insufficient funds")
            return
        self.balance -= int(amount)
        # self.getBalance()

    def getBalance(self):
        print(self.balance)


bank = {}

while True:
    # print(bank)
    inp = input()
    if inp == "stop":
        break
    
    try: 
        act, name, balance = inp.split()
    except ValueError:
        act, name = inp.split()
    if act == "create":
        bank[name] = Account(name, balance)
    if name not in bank:
        print("Account not found")
        continue
    elif act == "deposit":
        bank[name].deposit(balance)
    elif act == "withdraw":
        bank[name].withdraw(balance)
    elif act == "balance":
        bank[name].getBalance()
