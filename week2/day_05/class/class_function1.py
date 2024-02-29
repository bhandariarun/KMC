class Car:
    def __init__(self, tyres, doors, window, engine_type):
        self.tyres = tyres
        self.doors = doors
        self.window = window
        self.engine_type = engine_type


    def drive(self):
        print(f"The type of car is {self.engine_type}")

if __name__ == "__main__":
    car_01 = Car(4,6,8,"Petrol")

    car_01.drive()