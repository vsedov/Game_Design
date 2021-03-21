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

            values = []
            for info in (pointer := (self.data["scores"])) :

                for v in info.values():
                    values.append(v)

                if self.username in info.values():
                    ic(info.items())
                    # Index of position
                    # extraction of infomation

            # values = list(zip(values[::2], values[1::2]))
            # ic(values)

            # It cant be in a loop

        #  if self.username not in [i[0] for i in values]:
        #      print(True)

        #     pointer.append(
        #         {"username": self.username, "highscore": self.json_points}
        #     )
        #     self._writer(self.data)

        # elif self.username in i:
        #     if self.json_points > i[1]:
        #         indexed_var = values.index(i[1])
        #         item = indexed_var // 2
        #         if item < 0:
        #             item = 0
        #         pointer[item]["highscore"] = self.json_points
        #         self._writer(self.data)

        #     else:
        #         return None
        except Exception as e:
            pass

    def _writer(self, parser):
        # ic(parser)
        with open("data.json", "w") as json_file:
            json.dump(parser, json_file, indent=4)


"""

"""
