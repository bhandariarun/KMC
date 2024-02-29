"""
Class -> Entity
Example:
If class is a entity then attributes are
"""

class Car():
    def __init__(self, name, fuel_type):
        self.name = name
        self.fuel_type = fuel_type

class Maruti(Car):
    def __init__(self, name, fuel_type, speeds):
        super().__init__(name, fuel_type)
        self.speeds = speeds

    def travel(self):
        print(f"{self.name} : {self.speeds}")



if __name__ == '__main__':
    obj = Maruti('Suzuki','Petrol','200KM/HR')
    obj.travel()
