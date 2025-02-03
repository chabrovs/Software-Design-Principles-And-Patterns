class Vehicle:
    def horn(self):
        print("Beep Beep")


class Car:
    def __init__(self, vehicle: Vehicle):
        self.vehicle = vehicle


if __name__ == "__main__":
    vehicle = Vehicle()
    car = Car(vehicle)
    car.vehicle.horn()