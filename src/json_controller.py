import json
from dataclasses import dataclass

from icecream import ic


@dataclass(init=True)
class JsonData:
    def __init__(self, points, username) -> None:
        self.data = None
        self.json_points = points
        self.username = username

        self._read_file()
        self._write_file()

    # working
    def _read_file(self):
        with open("src/data.json") as json_file:
            self.data = json.load(json_file)

    def _write_file(self):
        for i in self.data["scores"]:
            if self.username not in i["username"]:
                ic("this should be active ", self.username)
                self.data["scores"].append(
                    {"username": self.username, "highscore": self.points}
                )
            elif self.points > i["highscore"]:
                self.data["scores"][i]["highscore"] = self.points

                ic("Within write status ", self.data)
