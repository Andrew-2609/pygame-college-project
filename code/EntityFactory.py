#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Background import Background
from code.constant import WINDOW_WIDTH


class EntityFactory:
    def get_player(self, ):
        pass

    def get_enemy(self, ):
        pass

    @staticmethod
    def get_background(name: str, position: tuple = (0, 0)):
        match name:
            case 'level1':
                list_bg: list[Background] = []
                for i in range(7):
                    list_bg.append(Background(name=f'level1_bg{i}', position=position))
                    list_bg.append(Background(name=f'level1_bg{i}', position=(WINDOW_WIDTH, 0)))
                return list_bg
