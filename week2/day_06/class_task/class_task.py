# class Person:
#     def __init__(self, name, age):
#         self._name = name
#         self._age = age
#
#     def display(self):
#         print(f"The person name is {self._name} is {self._age}")
#
# if __name__ == "__main__":
#      person_test = Person(name="Ram", age = "22")
#      person_test.display()

from abc import ABC, abstractmethod
class BankingApp():

    def database(self):
        print(f"Connect to database successfully")

    @abstractmethod
    def security(self):
        pass

class MobileApp(BankingApp):


    def login_app(self):
        print("Login to Mobile App successfully")

    def security(self):
        print("Security of Mobile app")

if __name__ == "__main__":
    # bank = BankingApp()
    # bank.database()
    mobile_app = MobileApp()
    print(mobile_app)