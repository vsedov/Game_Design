#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# File Name: json_controller

import json
from dataclasses import dataclass


@dataclass(init=True)
class JsonData:
    def __init__(self, points, username) -> None:
        self.data = None
        self.json_points: int = points
        self.username: str = username

        self.__name_exists: bool = False
        self._read_file()

    def _writer(self, parser):
        """
        write self.name to json file

        writer parser into json file

        Parameters
        ----------
        parser : dictionary to be writen
        """
        # ic(parser)
        with open("src/system_components/data.json", "w") as json_file:
            json.dump(parser, json_file, indent=4)

    def _read_file(self):
        """
        read file

        read from json
        """
        with open("src/system_components/data.json") as json_file:
            self.data = json.load(json_file)

        try:
            for counter, info in enumerate(main := (self.data["scores"])):
                values = info.values()
                if self.username in values:
                    self.__name_exists = True
                    x = dict(info.items())
                    high_score = x["highscore"]

                    if self.json_points >= high_score:
                        main[counter]["highscore"] = self.json_points
                        return self._writer(self.data)

                    else:
                        break

            if not self.__name_exists:
                main.append({"username": self.username, "highscore": self.json_points})
                return self._writer(self.data)

        except Exception as e:
            pass
