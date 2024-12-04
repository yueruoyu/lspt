class Player:
    def __init__(self):
        pass

    def choose(self):
        pass
    

class Move:
    def __init__(self):
        pass


class Rule:
    def __init__(self):
        pass

    def compare(self, move1, move2):
        pass

class RPSGame:
    def __init__(self):
        self._human = Player()
        self._computer = Player()
    def _display_welcome_message(self):
        print("Welcome to Rck Paper Scissors!")

    def _self_display_goodbye_message(self):
        print("Thanks for player Rock Paper Scissors. Goodbye!")

    def play(self):
        self_display_welcome_message()
        self._human.choose()
        self._computer.choose()
        display_winner
        self._display_goodbye_message()

