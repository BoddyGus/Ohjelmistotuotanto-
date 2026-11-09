import unittest

from player import Player
from player_stats import PlayerStats


class PlayerReaderStub:
    def get_players(self):
        return [
            Player({
                "name": "Semenko",
                "team": "EDM",
                "nationality": "CAN",
                "goals": 4,
                "assists": 12,
            }),
            Player({
                "name": "Lemieux",
                "team": "PIT",
                "nationality": "CAN",
                "goals": 45,
                "assists": 54,
            }),
            Player({
                "name": "Kurri",
                "team": "EDM",
                "nationality": "FIN",
                "goals": 37,
                "assists": 53,
            }),
            Player({
                "name": "Gretzky",
                "team": "EDM",
                "nationality": "CAN",
                "goals": 35,
                "assists": 89,
            }),
        ]


class TestPlayerStats(unittest.TestCase):
    def setUp(self):
        self.stats = PlayerStats(PlayerReaderStub())

    def test_top_scorers_by_nationality(self):
        players = self.stats.top_scorers_by_nationality("CAN")

        self.assertEqual(
            [player.name for player in players],
            ["Gretzky", "Lemieux", "Semenko"],
        )

    def test_top_scorers_by_team(self):
        players = self.stats.top_scorers_by_team("EDM")

        self.assertEqual(
            [player.name for player in players],
            ["Gretzky", "Kurri", "Semenko"],
        )
