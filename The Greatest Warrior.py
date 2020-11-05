import math

ranks = ["Pushover", "Novice", "Fighter", "Warrior", "Veteran", "Sage", "Elite", "Conqueror", "Champion", "Master",
         "Greatest"]

get_rank_number = lambda l: math.floor(l / 10)
get_rank = lambda l: ranks[get_rank_number(l)]


class Warrior:
    def __init__(self):
        self.level = 1
        self.experience = 100
        self.rank = ranks[0]
        self.achievements = []

    def update_experience(self, e):
        self.experience = min(10000, self.experience + e)
        self.level = math.floor(self.experience / 100)
        self.rank = get_rank(self.level)

    def training(self, result):
        if self.level < result[2]:
            return "Not strong enough"
        self.achievements.append(result[0])
        self.update_experience(result[1])
        return result[0]

    def battle(self, level):
        if level > 100 or level < 1:
            return "Invalid level"
        level_diff = level - self.level
        if level_diff == 0:
            self.update_experience(10)
            return "A good fight"
        if level_diff == -1:
            self.update_experience(5)
            return "A good fight"
        if level_diff < -1:
            return "Easy fight"

        rank_diff = get_rank_number(level) - get_rank_number(self.level)
        if level_diff >= 5 and rank_diff > 0:
            return "You've been defeated"
        if level_diff >= 1:
            self.update_experience(20 * level_diff * level_diff)
            return "An intense fight"
