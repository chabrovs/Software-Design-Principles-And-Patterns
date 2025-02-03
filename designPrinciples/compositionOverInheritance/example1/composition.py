class Vehicle:
    def horn(self):
        print("Beep Beep")


class Car:
    def __init__(self):
        self.vehicle = Vehicle()


if __name__ == "__main__":
    car = Car()
    car.vehicle.horn()
