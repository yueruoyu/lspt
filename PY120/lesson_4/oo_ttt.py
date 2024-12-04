import random
import os

def clear_screen():
    os.system('clear')


class Board:
    def __init__(self):
        self.squares = {key: Square() for key in range(1, 10)}
    def display(self):
        print()
        print("     |     |")
        print(f"  {self.squares[1]}  |"
              f"  {self.squares[2]}  |"
              f"  {self.squares[3]}")
        print("     |     |     ")
        print("-----+-----+-----")
        print("     |     |     ")
        print(f"  {self.squares[4]}  |"
              f"  {self.squares[5]}  |"
              f"  {self.squares[6]}")
        print("     |     |     ")
        print("-----+-----+-----")
        print("     |     |     ")
        print(f"  {self.squares[7]}  |"
              f"  {self.squares[8]}  |"
              f"  {self.squares[9]}")
        print("     |     |     ")
        print()

    def reset(self):
        self.squares = {key: Square() for key in range(1, 10)}

    def clear_display(self):
        clear_screen()
        self.display()

    def avaiable_choices(self):
        return [key for key, square in self.squares.items()
                    if square.is_available()]

    def mark(self, player, choice):
        self.squares[choice].marker = player.marker

    def count(self, player, choices):
        counter = 0
        for choice in choices:
            if self.squares[choice].marker == player.marker:
                counter += 1
        return counter

class Square:
    INITIAL_MARKER = ' '
    HUMAN_MARKER = 'X'
    COMPUTER_MARKER = 'O'
    def __init__(self, marker=INITIAL_MARKER):
        self.marker = marker

    @property
    def marker(self):
        return self._marker

    @marker.setter
    def marker(self, value):
        self._marker = value

    def __str__(self):
        return self.marker

    def is_available(self):
        return self.marker == Square.INITIAL_MARKER

class Player:
    def __init__(self, marker):
        self.marker = marker
        self.score = 0

class Human(Player):
    def __init__(self):
        super().__init__(Square.HUMAN_MARKER)

class Computer(Player):
    def __init__(self):
        super().__init__(Square.COMPUTER_MARKER)

class Game:
    WINNING_COMBO = [
            (1, 2, 3), (4, 5, 6), (7, 8, 9),
            (1, 4, 7), (2, 5, 8), (3, 6, 9),
            (1, 5, 9), (3, 5, 7)
        ]
    def __init__(self):
        self.board = Board()
        self.human = Human()
        self.computer = Computer()
    def display_welcome_message(self):
        print("Welcome to play Tic-Tac-Toe Game!")

    def display_goodbye_message(self):
        print("Thank you! Goodbye!")

    def _is_game_over(self):
        return self.is_full() or self.someone_won()

    def is_full(self):
        return len(self.board.avaiable_choices()) == 0

    def someone_won(self):
        return self.computer_won() or self.human_won()

    def computer_won(self):
        for tup in Game.WINNING_COMBO:
            if self.board.count(self.computer, tup) == 3:
                return "Computer"
        return None

    def human_won(self):
        for tup in Game.WINNING_COMBO:
            if self.board.count(self.human, tup) == 3:
                return "You"
        return None

    def join_or(self, lst, sep=', ', word='or'):
        if len(lst) == 1:
            return lst[0]
        if len(lst) ==2:
            return f"{lst[0]} {word} {lst[1]}"
        return (sep.join([str(num) for num in lst[:-1]])
                    + f"{sep}{word} {lst[-1]}")

    def human_mark(self):
        valid_choices = self.board.avaiable_choices()
        choice_str = self.join_or(valid_choices)
        while True:
            prompt = f"Choose a square({choice_str}): "
            choice = input(prompt)
            try:
                choice = int(choice)
                if choice in valid_choices:
                    break
            except ValueError:
                pass
            print("Not a valid choice.")
        self.board.mark(self.human, choice)

    def computer_mark(self):
        valid_choices = self.board.avaiable_choices()
        threat = (self.check_threat(self.computer) or
                    self.check_threat(self.human))
        if threat:
            choice = threat
        elif 5 in valid_choices:
            choice = 5
        else:
            choice = random.choice(valid_choices)
        self.board.mark(self.computer, choice)

    def check_threat(self, player):
        for tup in Game.WINNING_COMBO:
            if self.board.count(player, tup) == 2:
                for num in tup:
                    if self.board.squares[num].is_available():
                        return num
        return None

    def display_winner(self):
        winner = self.computer_won() or self.human_won()
        if winner:
            print(f"{winner} won!")
        else:
            print("It's a tie!")
    def play_again(self):
        if self.computer.score == 3:
            print("Computer won the match!")
            return False
        if self.human.score == 3:
            print("You won the match!")
            return False
        self.continue_play = input("do you want to play again(y/n)?: ")
        return self.continue_play.casefold().startswith('y')

    def track_score(self):
        if self.computer_won():
            self.computer.score += 1
        elif self.human_won():
            self.human.score += 1

    def player_mark(self,player):
        if player.__class__.__name__ == 'Human':
            self.human_mark()
        else:
            self.computer_mark()

    def play(self):
        self.display_welcome_message()
        player_tuple = (self.human, self.computer)
        while True:
            self.board.reset()
            player_tuple = player_tuple[1], player_tuple[0]
            while True:
                self.board.clear_display()
                self.player_mark(player_tuple[0])
                if self._is_game_over():
                    break
                self.board.clear_display()
                self.player_mark(player_tuple[1])
                if self._is_game_over():
                    break
            self.board.clear_display()
            self.display_winner()
            self.track_score()
            print(self.human.score, self.computer.score)
            if not self.play_again():
                break
        self.display_goodbye_message()

board = Board()
print(board.avaiable_choices())

game = Game()
print(game.is_full())
game.play()
