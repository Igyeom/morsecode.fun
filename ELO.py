import random
import math

# Original Library by @danybeam on GitHub, thank you! -Ian, creator of morsecode.fun

def approxRollingAverage(avg, new_sample):
    avg -= avg / 100
    avg += new_sample / 100
    return avg

class Player(object):
    def __init__(self, name, rating):
        self.rating = int(rating)
        self.name = name
        self.verification = random.randint(0,10000)
        self.win_ratio = 1

    # used for locating players
    def __eq__(self,other):
        return other.name == self.name and other.rating == self.rating and other.verification == self.verification
    
    # used for comparisons/orderings
    def __lt__(self,other):
        if not self.rating == other.rating:
            return self.rating < other.rating
        elif not self.name == other.name:
            return self.name < other.name
        else:
            return self.verification < other.verification

    def __gt__(self,other):
        if not self.rating == other.rating:
            return self.rating > other.rating
        elif not self.name == other.name:
            return self.name > other.name
        else:
            return self.verification > other.verification

    def __le__(self,other):
        if self == other:
            return True
        elif not self.rating == other.rating:
            return self.rating < other.rating
        elif not self.name == other.name:
            return self.name < other.name
        else:
            return self.verification < other.verification

    def __ge__(self,other):
        if self == other:
            return True
        elif not self.rating == other.rating:
            return self.rating > other.rating
        elif not self.name == other.name:
            return self.name > other.name
        else:
            return self.verification > other.verification

    def __str__(self):
        return 'Player({0},{1})'.format(self.name,self.rating)
    
    def __repr__(self):
        return str(self)

def get_exp_score(rating_a, rating_b):
    return 1.0 /(1 + 10**((rating_b - rating_a)/400.0))

def rating_adj(rating, exp_score, score, k=32):
    return rating + k * (score - exp_score)

def match_result(player, challenger, result, floor = None):
        exp_score_a = get_exp_score(player.rating, challenger.rating)

        old_player = player.rating
        old_challenger = challenger.rating

        player.rating = math.floor(rating_adj(player.rating, exp_score_a, result))
        challenger.rating = math.floor(rating_adj(challenger.rating, exp_score_a, result))

        player_ratio = 0 if player.rating-old_player <= 0 else 1
        challenger_ratio = 0 if challenger.rating-old_challenger <= 0 else 1

        player.win_ratio = approxRollingAverage(player.win_ratio, player_ratio)
        challenger.win_ratio = approxRollingAverage(challenger.win_ratio, challenger_ratio)

        if floor:
            if player.rating < floor:
                player.rating = floor
            if challenger.rating < floor:
                challenger.rating = floor

def create_match(players, player, fairness= 0.5, margin= 0.01):
    if not players or not player:
        raise ValueError("There must be a list of players and a player to have as reference")

    # Guarantee that the list is sorted
    players.sort()

    # Helper variables
    index = players.index(player)
    weaker = True if player.win_ratio < 0.5 else False
    rival = index-1 if weaker else index+1
    change_rate = -1 if weaker else 1

    # limits of fairness
    lower_bound = (fairness-margin)
    higher_bound = (fairness+margin)

    # search for a rival
    while lower_bound <= get_exp_score(player.rating, players[rival].rating) <= higher_bound:
        rival += change_rate
        if not -1 < rival < len(players):
            break
    
    # Fixing in case of small list or quirks of search
    if not -1 < rival < len(players) or not lower_bound < get_exp_score(player.rating, players[rival].rating) < higher_bound:
        rival -= change_rate
    if rival == index:
        rival += change_rate
    
    rival = random.randint(index+1,rival)
    
    return players[rival]