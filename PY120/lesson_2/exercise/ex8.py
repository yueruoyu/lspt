class Dog:
    def speak(self):
        return 'bark!'

    def sleep(self):
        return 'sleeping!'

    def run(self):
        return 'running!'

    def jump(self):
        return 'jumping!'

    def fetch(self):
        return 'fetching!'

class BullDog(Dog):
    def sleep(self):
        return 'snoring'


teddy = Dog()
print(teddy.speak())      # bark!
print(teddy.sleep())       # sleeping!