class Wallet():
    def __init__(self, money):
        self.amount = money

    def __add__(self, other):
        if not isinstance(other, Wallet):
            return NotImplemented
        else:
            return Wallet(self.amount + other.amount)
    def __str__(self):
        return f"Wallet with ${self.amount}."

wallet1 = Wallet(50)
wallet2 = Wallet(30)
merged_wallet = wallet1 + wallet2
print(merged_wallet.amount == 80)       # True
wallet1 = Wallet(50)
wallet2 = Wallet(30)
merged_wallet = wallet1 + wallet2
print(merged_wallet)          # Wallet with $80.