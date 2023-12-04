#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

import pygame

from code.Level import Level
from code.Menu import Menu
from code.constant import WINDOW_WIDTH, WINDOW_HEIGHT, MENU_OPTIONS


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WINDOW_WIDTH, WINDOW_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            selected_menu_option = menu.run()

            if selected_menu_option in [MENU_OPTIONS[0]]:
                level = Level(window=self.window, name='Level 1')
                level.run()
            else:
                pygame.quit()
                sys.exit()
