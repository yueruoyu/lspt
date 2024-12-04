

class Pet():
    def __init__(self, species, name):
        self._species = species
        self._name = name

    @property
    def name(self):
        return self._name

    @property
    def species(self):
        return self._species

class Owner():
    def __init__(self, name):
        self._name = name
        self._pet_list = []

    @property
    def name(self):
        return self._name

    @property
    def pet_list(self):
        return self._pet_list

    def number_of_pets(self):
        return len(self._pet_list)
    

class Shelter():
    def __init__(self):
        self._owner_set = set()
        

    def adopt(self, owner, pet):
        self._owner_set.add(owner)
        owner.pet_list.append(pet)

    def print_adoptions(self):
        for owner in self._owner_set:
            print(f"{owner.name} has adopted the following pets:")
            for pet in owner.pet_list:
                print(f"a {pet.species} named {pet.name}")
            print()


cocoa   = Pet('cat', 'Cocoa')
cheddar = Pet('cat', 'Cheddar')
darwin  = Pet('bearded dragon', 'Darwin')
kennedy = Pet('dog', 'Kennedy')
sweetie = Pet('parakeet', 'Sweetie Pie')
molly   = Pet('dog', 'Molly')
chester = Pet('fish', 'Chester')

phanson = Owner('P Hanson')
bholmes = Owner('B Holmes')

shelter = Shelter()
shelter.adopt(phanson, cocoa)
shelter.adopt(phanson, cheddar)
shelter.adopt(phanson, darwin)
shelter.adopt(bholmes, kennedy)
shelter.adopt(bholmes, sweetie)
shelter.adopt(bholmes, molly)
shelter.adopt(bholmes, chester)

shelter.print_adoptions()
print(f"{phanson.name} has {phanson.number_of_pets()} "
      "adopted pets.")
print(f"{bholmes.name} has {bholmes.number_of_pets()} "
      "adopted pets.")


# P Hanson has adopted the following pets:
# a cat named Cocoa
# a cat named Cheddar
# a bearded dragon named Darwin

# B Holmes has adopted the following pets:
# a dog named Molly
# a parakeet named Sweetie Pie
# a dog named Kennedy
# a fish named Chester

# P Hanson has 3 adopted pets.
# B Holmes has 4 adopted pets.