import random

class Deck:
    RANKS = list(range(2, 11)) + ['Jack', 'Queen', 'King', 'Ace']
    SUITS = ['Hearts', 'Clubs', 'Diamonds', 'Spades']
    def __init__(self):
        self.cards_list = []
        for rank in self.RANKS:
            for suit in self.SUITS:
                self.cards_list.append(Card(rank, suit))
        random.shuffle(self.cards_list)

    def draw(self):
        if len(self.cards_list) == 0:
            self.__init__()
        return self.cards_list.pop()



class Card:
    RANKING = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __lt__(self, other):
        if isinstance(other, Card):
            return Card.RANKING.index(self.rank) < Card.RANKING.index(other.rank)
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Card):
            return Card.RANKING.index(self.rank) == Card.RANKING.index(other.rank)

    def __str__(self):
        return f"{self.rank} of {self.suit}"



deck = Deck()
drawn = []
for _ in range(52):
    drawn.append(deck.draw())

count_rank_5 = sum([1 for card in drawn if card.rank == 5])
count_hearts = sum([1 for card in drawn if card.suit == 'Hearts'])

print(count_rank_5 == 4)      # True
print(count_hearts == 13)     # True

drawn2 = []
for _ in range(52):
    drawn2.append(deck.draw())

print(drawn != drawn2)        # True (Almost always).
