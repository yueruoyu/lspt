

class Car:
    def __init__(self, name, year, color):
        self._name = name
        self._year = year
        self._color = color

    def __str__(self):
        return f"{self._color.capitalize()} {self._year} {self._name}"


    def __repr__(self):
        return f"Car('{self._name}', {self._year}, '{self._color}')"



vwbuzz = Car('ID.Buzz', 2024, 'red')
print(vwbuzz)        # Red 2024 ID.Buzz
print(repr(vwbuzz))  # Car('ID.Buzz', 2024, 'red')