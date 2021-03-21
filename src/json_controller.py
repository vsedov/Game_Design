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

    # working

    def item(self, item):
        pass

    def _read_file(self):
        with open("data.json") as json_file:
            self.data = json.load(json_file)

        try:
            # writer = self.data["scores"]

            # values = []
            for counter, info in enumerate(self.data["scores"]):
                values = info.values()
                if self.username in values:
                    x = dict(info.items())
                    high_score = x["highscore"]

                    if self.json_points >= high_score:
                        high_score = self.json_points

                    x["highscore"] = high_score
                    ic(x)

        except Exception as e:

            pass

    def _writer(self, parser):
        # ic(parser)
        with open("data.json", "w") as json_file:
            json.dump(parser, json_file, indent=4)


"""

"""
