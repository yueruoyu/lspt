class Dog:
    def __init__(self, breed):
        self._breed = breed

    def get_breed(self):
        return self._breed


dog1 = Dog("Golden Retriever")
dog2 = Dog("Poodle")
dog3 = Dog("haba")

dog3._breed = "jingba"
print(dog3.get_breed())
print(dog1.get_breed())
print(dog2.get_breed())

class Student:
    school_name = "Oxford"
    def __init__(self, name):
        self.name = name

    @classmethod
    def get_school_name(cls):
        return cls.school_name

print(Student.get_school_name())
print(Student.school_name)

student1 = Student('bob')

print(student1.__class__.school_name)

class Car:
    manufacturer = 'BMW'
    def __init__(self, company):
        self.manufacturer = company
    def show_manufacturer(self):
        print(self.manufacturer)
        print(self.__class__.manufacturer)

car = Car('QQ')
car.show_manufacturer()

class Bird:
    def __init__(self, species):
        self.species = species

class Sparrow(Bird):
    def __init__(self):
        super().init__("sparrow")

sp1 = Sparrow
print(sp1.species)

