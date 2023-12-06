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
        match name:
            case 'level1':
                list_bg: list[Background] = []
                for i in range(6):
                    list_bg.append(Background(f'level1_bg{i}', position))
                return list_bg
