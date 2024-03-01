from abc import ABC, abstractmethod

# Abstract class Animal
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def eat(self):
        pass

# Concrete class Mammal
class Mammal(Animal):
    def move(self):
        return "Walks"

# Concrete class Bird
class Bird(Animal):
    def move(self):
        return "Flies"

# Concrete class Fish
class Fish(Animal):
    def move(self):
        return "Swims"

# Concrete classes for specific mammals
class Dog(Mammal):
    def speak(self):
        return "Bark"

    def eat(self):
        return "Meat"

class Cat(Mammal):
    def speak(self):
        return "Meow"

    def eat(self):
        return "Fish"

# Concrete classes for specific birds
class Eagle(Bird):
    def speak(self):
        return "Screech"

    def eat(self):
        return "Meat"

class Penguin(Bird):
    def speak(self):
        return "Honk"

    def eat(self):
        return "Fish"

# Concrete classes for specific fish
class Salmon(Fish):
    def speak(self):
        return "Splash"

    def eat(self):
        return "Plankton"

class Goldfish(Fish):
    def speak(self):
        return "Bubble"

    def eat(self):
        return "Flakes"

# Demonstration
if __name__ == "__main__":
    # Creating instances and calling methods
    dog = Dog()
    print("Dog:", dog.speak(), "-", dog.move(), "-", dog.eat())

    cat = Cat()
    print("Cat:", cat.speak(), "-", cat.move(), "-", cat.eat())

    eagle = Eagle()
    print("Eagle:", eagle.speak(), "-", eagle.move(), "-", eagle.eat())

    penguin = Penguin()
    print("Penguin:", penguin.speak(), "-", penguin.move(), "-", penguin.eat())

    salmon = Salmon()
    print("Salmon:", salmon.speak(), "-", salmon.move(), "-", salmon.eat())

    goldfish = Goldfish()
    print("Goldfish:", goldfish.speak(), "-", goldfish.move(), "-", goldfish.eat())
