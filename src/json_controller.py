import json
from dataclasses import dataclass


@dataclass(init=True)
class JsonData:
    def __init__(self, points, username) -> None:
        self.data = None
        self.json_points = points
        self.username = username

        self._read_file()

    def _writer(self, parser):
        # ic(parser)
        with open("data.json", "w") as json_file:
            json.dump(parser, json_file, indent=4)

    def _read_file(self):
        with open("data.json") as json_file:
            self.data = json.load(json_file)

        try:
            container = []
            for counter, info in enumerate(main := (self.data["scores"])):

                container.append(info)
                values = info.values()
                if self.username in values:
                    x = dict(info.items())
                    high_score = x["highscore"]

                    if self.json_points >= high_score:
                        main[counter]["highscore"] = self.json_points
                        return self._writer(self.data)

                    else:
                        continue
            if self.username not in container:
                main.append({"username": self.username, "highscore": self.json_points})
                return self._writer(self.data)

        except Exception as e:
            pass
