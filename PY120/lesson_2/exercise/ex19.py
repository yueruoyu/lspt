
import random

class PokerHand:
    DICTION = {'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}
    def __init__(self, deck):
        self.cards = [deck.draw() for _ in range(5)]
        self.suits = [card.suit for card in self.cards]
        self.ranks = [self.DICTION.get(card.rank, card.rank) for card in sorted(self.cards)]
        self.distance = [self.ranks[i+1] - self.ranks[i] for i in range(4)]
        self.dup_dict = {}
        for num in self.ranks:
            self.dup_dict[num] = self.dup_dict.get(num, 0) + 1
        self.freq = sorted(self.dup_dict.values())
    def print(self):
       for card in self.cards:
        print(card)

    def evaluate(self):
        if self._is_royal_flush():
            return "Royal flush"
        elif self._is_straight_flush():
            return "Straight flush"
        elif self._is_four_of_a_kind():
            return "Four of a kind"
        elif self._is_full_house():
            return "Full house"
        elif self._is_flush():
            return "Flush"
        elif self._is_straight():
            return "Straight"
        elif self._is_three_of_a_kind():
            return "Three of a kind"
        elif self._is_two_pair():
            return "Two pair"
        elif self._is_pair():
            return "Pair"
        else:
          return "High card"

    def _is_royal_flush(self):
        return (len(set(self.suits)) == 1 and 
                self.ranks == [10, 11, 12, 13, 14])

    def _is_straight_flush(self):
        return (len(set(self.suits)) == 1 and self.distance == [1, 1, 1, 1])

    def _is_four_of_a_kind(self):
        return self.freq[-1] == 4

    def _is_full_house(self):
        return self.freq[-1] == 3 and self.freq[-2] == 2

    def _is_flush(self):
        return len(set(self.suits)) == 1

    def _is_straight(self):
        return self.distance == [1, 1, 1, 1]

    def _is_three_of_a_kind(self):
        return self.freq[-1] == 3 and self.freq[-2] == 1

    def _is_two_pair(self):
        return self.freq[-1] == 2 and self.freq[-2] == 2

    def _is_pair(self):
        return self.freq[-1] == 2 and self.freq[-2] == 1




class Deck:
    RANKS = list(range(2, 11)) + ['Jack', 'Queen', 'King', 'Ace']
    SUITS = ['Hearts', 'Clubs', 'Diamonds', 'Spades']
    def __init__(self):
        self._deck = []
        for rank in self.RANKS:
            for suit in self.SUITS:
                self._deck.append(Card(rank, suit))
        random.shuffle(self._deck)

    def draw(self):
        if len(self._deck) == 0:
            self.__init__()
        return self._deck.pop()



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



hand = PokerHand(Deck())
hand.print()
print(hand.evaluate())
print()

# Adding TestDeck class for testing purposes

class TestDeck(Deck):
    def __init__(self, cards):
        self._deck = cards



# All of these tests should return True

hand = PokerHand(
    TestDeck(
        [
            Card("Ace", "Hearts"),
            Card("Queen", "Hearts"),
            Card("King", "Hearts"),
            Card("Jack", "Hearts"),
            Card(10, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Royal flush")

hand = PokerHand(
    TestDeck(
        [
            Card(8, "Clubs"),
            Card(9, "Clubs"),
            Card("Queen", "Clubs"),
            Card(10, "Clubs"),
            Card("Jack", "Clubs"),
        ]
    )
)
print(hand.evaluate() == "Straight flush")

hand = PokerHand(
    TestDeck(
        [
            Card(3, "Hearts"),
            Card(3, "Clubs"),
            Card(5, "Diamonds"),
            Card(3, "Spades"),
            Card(3, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "Four of a kind")

hand = PokerHand(
    TestDeck(
        [
            Card(3, "Hearts"),
            Card(3, "Clubs"),
            Card(5, "Diamonds"),
            Card(3, "Spades"),
            Card(5, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Full house")

hand = PokerHand(
    TestDeck(
        [
            Card(10, "Hearts"),
            Card("Ace", "Hearts"),
            Card(2, "Hearts"),
            Card("King", "Hearts"),
            Card(3, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Flush")

hand = PokerHand(
    TestDeck(
        [
            Card(8, "Clubs"),
            Card(9, "Diamonds"),
            Card(10, "Clubs"),
            Card(7, "Hearts"),
            Card("Jack", "Clubs"),
        ]
    )
)
print(hand.evaluate() == "Straight")

hand = PokerHand(
    TestDeck(
        [
            Card("Queen", "Clubs"),
            Card("King", "Diamonds"),
            Card(10, "Clubs"),
            Card("Ace", "Hearts"),
            Card("Jack", "Clubs"),
        ]
    )
)
print(hand.evaluate() == "Straight")

hand = PokerHand(
    TestDeck(
        [
            Card(3, "Hearts"),
            Card(3, "Clubs"),
            Card(5, "Diamonds"),
            Card(3, "Spades"),
            Card(6, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "Three of a kind")

hand = PokerHand(
    TestDeck(
        [
            Card(9, "Hearts"),
            Card(9, "Clubs"),
            Card(5, "Diamonds"),
            Card(8, "Spades"),
            Card(5, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Two pair")

hand = PokerHand(
    TestDeck(
        [
            Card(2, "Hearts"),
            Card(9, "Clubs"),
            Card(5, "Diamonds"),
            Card(9, "Spades"),
            Card(3, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "Pair")

hand = PokerHand(
    TestDeck(
        [
            Card(2, "Hearts"),
            Card("King", "Clubs"),
            Card(5, "Diamonds"),
            Card(9, "Spades"),
            Card(3, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "High card")