class Animal:
    def __init__(self,*args):
        if len(args)==1:
            self.name = args[0]
        elif len(args) == 2:
            self.name = args[0]
            self.species = args[1]
        elif len(args) == 3:
            self.name = args[0]
            self.species = args[1]
            self.age = args[2]


    # def __init__(self, name, species, age):
    #     self.name = name
    #     self.species = species
    #     self.age = age

    def walk(self):
        print(f"{self.name} is walking")
if __name__ == "__main__":
    cat = Animal("Cat", "Cat Family")
    cat.walk()