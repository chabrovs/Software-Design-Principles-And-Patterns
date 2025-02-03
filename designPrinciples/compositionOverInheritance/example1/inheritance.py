class Vehicle:
    def horn(self):
        print("Beep Beep")


class Car(Vehicle):
    def drive(self):
        print("Car drives")


if __name__ == '__main__':
    car = Car()
    car.horn()