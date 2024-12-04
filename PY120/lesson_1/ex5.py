
class Candidate:
    def __init__(self, string):
        self.name = string
        self.vote = 0

    @property
    def vote(self):
        return self._vote
    @vote.setter
    def vote(self, vote):
        self._vote = vote

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name

    def __iadd__(self, other):
        self.vote += other

        return self



class Election:
    def __init__(self, lst):
        self._candidate_list = lst

    def results(self):
        for candidate in self._candidate_list:
            print(f"{candidate.name}: {candidate.vote} votes")

        result_dict = {candidate.name: candidate.vote 
                for candidate in self._candidate_list}
        vote_lst = list(result_dict.values())
        percentage = round(max(vote_lst) / sum(vote_lst) * 100, 1)
        for k, v in result_dict.items():
            if v == max(vote_lst):
                winner = k
        print(f"{winner} won: {percentage}% of votes")




mike_jones = Candidate('Mike Jones')
susan_dore = Candidate('Susan Dore')
kim_waters = Candidate('Kim Waters')

candidates = {
    mike_jones,
    susan_dore,
    kim_waters,
}

votes = [
    mike_jones,
    susan_dore,
    mike_jones,
    susan_dore,
    susan_dore,
    kim_waters,
    susan_dore,
    mike_jones,
]

for candidate in votes:
    candidate += 1

election = Election(candidates)
election.results()

# Mike Jones: 3 votes
# Susan Dore: 4 votes
# Kim Waters: 1 votes

# Susan Dore won: 50.0% of votes