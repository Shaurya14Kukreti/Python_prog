class Car:
    def __init__(self, name):
        self.name = name

    def carname(self):
        print('Hello, this car is manufactured by :: ', self.name)

p = Car('Maruti')
p.carname()
