#!/usr/bin/python
# -*- coding: utf-8 -*-

from code.Entity import Entity
from code.constant import WINDOW_WIDTH, ENTITY_SPEED


class Background(Entity):
    def __init__(self, name: str, position: tuple = (0, 0)):
        Entity.__init__(self, name, position)

    def move(self):
        self.rect.centerx -= ENTITY_SPEED.get(self.name)
        if self.rect.right <= 0:
            self.rect.left = WINDOW_WIDTH
