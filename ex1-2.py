# Exercise1-2
class Team:
    def __init__(self, name, colours):
        self.name = name
        self.colours = colours

    def get_name(self):
        return self.name

    def get_colours(self):
        return self.colours


class Football(Team):
    sport = "Football"

    def __init__(self, name, colours, goalkeeper):
        super().__init__(name, colours)
        self.goalkeeper = goalkeeper

    def get_colours(self):
        return self.colours

    def get_goalkeeper(self):
        return self.goalkeeper


class Rugby(Team):
    sport = "Rugby"

    def __init__(self, name, colours, flyhalf):
        super().__init__(name, colours)
        self.flyhalf = flyhalf

    def get_name(self):
        return self.name

    def get_colours(self):
        return self.colours

    def get_flyhalf(self):
        return self.flyhalf

class Shinty(Team):
    sport = "Shinty"

    def __init__(self, name, colours, sun):
        super().__init__(name, colours)
        self.sun = sun

    def get_name(self):
        return self.name

    def get_colours(self):
        return self.colours

    def get_sun(self):
        return self.sun

class Ice_Hockey(Team):
    sport = "Ice Hockey"

    def __init__(self, name, colours, hockey_guy):
        super().__init__(name, colours)
        self.hockey_guy = hockey_guy

    def get_name(self):
        return self.name

    def get_colours(self):
        return self.colours

    def get_sun(self):
        return self.hockey_guy

team1 = Football("Raith ROvers", "Blue and White", "Jamie MacDonal")
team2 = Rugby("Glasgow Warriors", "Light Blue , Black and White", "Adam Hastings")
team3 = Shinty("East Fife", "Yellow and Black", "Brett Long")
team4 = Ice_Hockey("Edinburgh", "Blue and Red", "Charlie Savala")

print("Versions FOUR")

teams = [team1, team2, team3, team4]

for team in teams:
    print()
    print(team.get_name(), "is a", team.sport, "team.")
    print("They play in", team.get_colours())

# print("Version ONE")
# print("Team : ", team1.get_name())
# print("Sport : ", team1.sport)
# print("Colours: ", team1.colours())
# print("Goalkeeper : ", team1.get_goalkeeper())
# print()
# print("Team : ", team2.get_name())
# print("Sport : ", team2.sport)
# print("Colours: ", team2.colours())
# print("Goalkeeper : ", team2.get_goalkeeper())
