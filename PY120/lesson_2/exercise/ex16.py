
class Transform:
    def __init__(self, string):
        self.string = string
    def uppercase(self):
        return self.string.upper()

    @classmethod
    def lowercase(cls, string):
        return string.lower()




my_data = Transform('abc')
print(my_data.uppercase())              # ABC
print(Transform.lowercase('XYZ'))       # xyz