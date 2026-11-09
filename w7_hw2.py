class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = int(year)

    def getName(self):
        return self.__class__.__name__

    def getAttr(self):
        return self.__dict__

    def printData(self):
        # print(f"{self.__class__.__name__}: {self.brand}, Year: {self.year}, ")
        strs = [f"{key}: {value}, " for key, value in list(self.__dict__.items())[2:]]
        print(f"{self.__class__.__name__}: {self.brand}, Year: {self.year}, " + "".join(strs)[:-2])


class Bicycle(Vehicle):
    def __init__(self, brand, year, model):
        super().__init__(brand, year)
        self.Model = model

class Car(Vehicle):
    def __init__(self, brand, year, seat):
        super().__init__(brand, year)
        self.Seat = int(seat)

class Motorcycle(Vehicle):
    def __init__(self, brand, year, cc):
        super().__init__(brand, year)
        self.cc = int(cc)

vehicles = []

# car = Car("y", 1, 1)
# # print(car.getAttr())
# car.printData()

while True:
    try:
        inp = input().strip()
        if inp == "":
            continue
        if inp == "stop":
            break
        if inp == "print":
            for v in vehicles:
                v.printData()
            continue

        typename, brand, year, attr = inp.split()
    except EOFError:
        break
    except ValueError:
        continue
    if typename == "Car":
        vehicles.append(Car(brand, year, attr))
    elif typename == "Motorcycle":
        vehicles.append(Motorcycle(brand, year, attr))
    elif typename == "Bicycle":
        vehicles.append(Bicycle(brand, year, attr))
    
