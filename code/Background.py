#!/usr/bin/python
# -*- coding: utf-8 -*-

from code.Entity import Entity


class Background(Entity):
    def __init__(self, name: str, position: tuple = (0, 0)):
        Entity.__init__(self, name, position)

    def move(self):
        pass
