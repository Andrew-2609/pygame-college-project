#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.constant import WINDOW_WIDTH


class Menu:
    def __init__(self, window: Surface):
        self.window: Surface = window
        self.surface: Surface = pygame.image.load('./asset/menu_bg.png')
        self.rect: Rect = self.surface.get_rect(left=0, top=0)

    def run(self):
        pygame.mixer_music.load('./asset/menu_bgm.mp3')
        pygame.mixer_music.play(loops=-1)
        pygame.mixer_music.set_volume(.125)

        while True:
            self.window.blit(source=self.surface, dest=self.rect)
            self.display_menu_text(50, 'Mountain', (255, 128, 0), (WINDOW_WIDTH / 2, 70))
            pygame.display.flip()

    def display_menu_text(self, text_size: int, text: str, text_color: tuple, text_center_position: tuple):
        text_font: Font = pygame.font.SysFont('Lucida Sans Typewriter', size=text_size)
        text_surface: Surface = text_font.render(text, True, text_color)
        text_rect = text_surface.get_rect(center=text_center_position)
        self.window.blit(source=text_surface, dest=text_rect)
