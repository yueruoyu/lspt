class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self._name = first_name.capitalize() + ' ' + last_name.capitalize()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, tup):
        a, b = tup
        if a.isalpha() and b.isalpha():
            self._name = a.capitalize() + ' ' + b.capitalize()
        else:
            raise ValueError("Name must be alphabetic.")

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        if first_name.isalpha():
            self._first_name = first_name
        else:
            raise ValueError("Name must be alphabetic.")

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        if last_name.isalpha():
            self._last_name = last_name
        else:
            raise ValueError("Name must be alphabetic.")

# actor = Person('Mark', 'Sinclair')
# print(actor.name)              # Mark Sinclair
# actor.name = ('Vin', 'Diesel')
# print(actor.name)              # Vin Diesel
# actor.name = ('', 'Diesel')
# # ValueError: Name must be alphabetic.

character = Person('annIE', 'HAll')
print(character.name)          # Annie Hall
character = Person('Da5id', 'Meier')
# ValueError: Name must be alphabetic.

friend = Person('Lynn', 'Blake')
print(friend.name)             # Lynn Blake
friend.name = ('Lynn', 'Blake-John')
# ValueError: Name must be alphabetic.