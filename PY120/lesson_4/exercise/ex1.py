# Let's practice creating an object hierarchy.

# Create a class called Animal with a single instance method called speak that takes a string argument and prints that argument to the terminal.

# Now create two other classes that inherit from Animal, one called Cat and one called Dog. The Cat class should have a meow method that takes no arguments and prints Meow!. The Dog class should have a bark method that says Woof! Woof! Woof! (dogs never bark just once). Make use of the Animal class's speak method when implementing the Cat and Dog classes. Don't invoke the print function in either of the subclasses.

class Animal:
    def __init__(self):
        pass
    def speak(self, message):
        print(message)

class Dog(Animal):
    def speak(self):
        super().speak("Meow")

class Cat(Animal):
    def speak(self):
        super().speak("Woof! Woof! Woof!")