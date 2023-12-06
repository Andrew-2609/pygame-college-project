#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Background import Background


class EntityFactory:
    def get_player(self, ):
        pass

    def get_enemy(self, ):
        pass

    @staticmethod
    def get_background(name: str, position: tuple = (0, 0)):
        return Background(name, position)
