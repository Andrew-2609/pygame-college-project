#!/usr/bin/python
# -*- coding: utf-8 -*-
from pygame import Surface

from code.Entity import Entity


class Level:
    def __init__(self, window: Surface, name: str):
        self.window = window
        self.name = name
        self.entity_list: list[Entity] = []

    def run(self, ):
        pass
