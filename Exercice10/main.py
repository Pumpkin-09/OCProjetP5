## Écrivez votre code ici !

class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_details(self):
        print(f"nom: {self.name}, age: {self.age}")


class Employee(Person):
    
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def display_details(self):
        super().display_details()
        print(f"Salaire: {self.salary}")

person_1 = Person("Marc", 27)
person_2 = Employee("Sophie", 36, 75000)

person_1.display_details()
person_2.display_details()