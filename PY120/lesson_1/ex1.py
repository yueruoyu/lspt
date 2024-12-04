# Create a Car class that meets these requirements:

# Each Car object should have a model, model year, and color provided at instantiation time.
# You should have an instance variable that keeps track of the current speed. Initialize it to 0 when you instantiate a new car.
# Create instance methods that let you turn the engine on, accelerate, brake, and turn the engine off. Each method should display an appropriate message.
# Create a method that prints a message about the car's current speed.
# Write some code to test the methods.

class Car:
    def __init__(self, model='BMW', model_year=2017, color='white'):
        self._model = model
        self._model_year = model_year
        self.color = color
        self.speed = 0
        self._engine_on = False

    def turn_engine_on(self):
        self._engine_on = True
        print('Engine is on!')

    def turn_engine_on(self):
        self._engine_on = False
        print('Engine is off!')

    def accelerate(self):
        print('Accelerate!')
        self._speed += 10

    def brake(self):
        print('Brake!')
        self._speed -= 10

    @property
    def speed(self):
        return self._speed
    
    @speed.setter
    def speed(self, speed):
        self._speed = speed

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color


    @classmethod
    def spray_color(cls, color):
        cls._color = color


mycar = Car()
mycar.turn_engine_on()
mycar.accelerate()
mycar.accelerate()
mycar.accelerate()
print(mycar.speed)
mycar.speed = 60
print(mycar.speed)
mycar.spray_color('black')
print(mycar.color)
print(Car._color)




