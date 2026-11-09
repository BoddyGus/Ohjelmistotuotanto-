class Player:
    def __init__(self, data):
        self.name = data["name"]
        self.team = data["team"]
        self.nationality = data["nationality"]
        self.goals = data["goals"]
        self.assists = data["assists"]

    @property
    def points(self):
        return self.goals + self.assists

    def __str__(self):
        return (
            f"{self.name:20} {self.team:10} "
            f"{self.goals} + {self.assists} = {self.points}"
        )
