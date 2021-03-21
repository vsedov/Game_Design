import json
from dataclasses import dataclass


@dataclass(init=True)
class JsonData:
    def __init__(self, points, username) -> None:
        self.data = None
        self.json_points = points
        self.username = username

        self._read_file()

    # working
    def _read_file(self):
        with open("data.json") as json_file:
            self.data = json.load(json_file)

        try:
            # writer = self.data["scores"]

            values = []
            for info in (pointer := (self.data["scores"])) :

                for i, v in info.items():
                    values.append(v)

            if self.username not in values:
                pointer.append(
                    {"username": self.username, "highscore": self.json_points}
                )
                self._writer(self.data)

            else:
                for i in range(len(values)):
                    if self.username == values[i]:
                        if self.json_points > values[i + 1]:
                            self.data["scores"][i]["highscore"] = self.json_points
                            self._writer(self.data)

        # Some really fuck code but it works i think i havent tested this properly though
        # probably doesnt work  with more than one user >.< idk

        except Exception as e:
            pass

    def _writer(self, parser):
        # ic(parser)
        with open("data.json", "w") as json_file:
            json.dump(parser, json_file, indent=4)


"""

"""
