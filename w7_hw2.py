class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = int(year)

class Bicycle(Vehicle):
    def __init__(self, brand, year, model):
        super().__init__(brand, year)
        self.model = model

class Car(Vehicle):
    def __init__(self, brand, year, seat):
        super().__init__(brand, year)
        self.seat = int(seat)

class Motorcycle(Vehicle):
    def __init__(self, brand, year, cc):
        super().__init__(brand, year)
        self.cc = int(cc)

while True:
    