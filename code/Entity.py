#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod

import pygame.image
from pygame import Surface, Rect


class Entity(ABC):
    def __init__(self, name: str, position: tuple = (0, 0)):
        self.name: str = name
        self.surface: Surface = pygame.image.load('./asset/' + name + '.png')
        self.rect: Rect = self.surface.get_rect(left=position[0], top=position[1])
        self.speed = 0

    @abstractmethod
    def move(self, ):
        pass
