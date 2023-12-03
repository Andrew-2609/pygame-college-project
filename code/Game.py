#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame import Surface
from pygame.font import Font

from code.Menu import Menu
from code.constant import WINDOW_WIDTH, WINDOW_HEIGHT


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WINDOW_WIDTH, WINDOW_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu.run()
