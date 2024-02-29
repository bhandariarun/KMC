"""
Class -> Entity
Example:
If class is a entity then attributes are
"""

# class Animal:
#     def __init__(self,*args):
#         if len(args)==1:
#             self.name = args[0]
#         elif len(args) == 2:
#             self.name = args[0]
#             self.species = args[1]
#         elif len(args) == 3:
#             self.name = args[0]
#             self.species = args[1]
#             self.age = args[2]
#
#
#     # def __init__(self, name, species, age):
#     #     self.name = name
#     #     self.species = species
#     #     self.age = age
#
#     def walk(self):
#         print(f"{self.name} is walking")
# if __name__ == "__main__":
#     cat = Animal("Cat", "Cat Family")
#     cat.walk()

class Car():
    def __init__(self, name, fuel_type):
        self.name = name
        self.fuel_type = fuel_type

    def display(self):
        print(self.name, self.model, self.speeds)
class Maruti(Car):
    def __init__(self, name, fuel_type, speeds):
        super().__init__(name, fuel_type)
        self.speeds = speeds

    def travel(self):
        print(f"{self.name}:{self.speeds}")



if '__name__' == '__main__':
    obj = Maruti('Suzuki','Petrol','200KM/HR')
    obj.travel()
