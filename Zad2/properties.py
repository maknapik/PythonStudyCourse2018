import pygame

class Screen:
    def __init__(self, screen):
        try:
            self.width = screen["width"]
        except KeyError:
            print("Screen initialize: KeyError")

        try:
            self.height = screen["height"]
        except KeyError:
            print("Screen initialize: KeyError")

        try:
            self.bg_color = screen["bg_color"]
        except KeyError:
            print("Screen initialize: KeyError")

        try:
            self.fg_color = screen["fg_color"]
        except KeyError:
            print("Screen initialize: KeyError")

    def start(self, palette):
        self.screen = pygame.display.set_mode((self.width, self.height), 0, 32)

        if self.bg_color in palette.colors:
            self.screen.fill(pygame.Color(palette.colors[self.bg_color]))
        else:
            self.screen.fill(pygame.color("#dddddd"))


class Palette:
    def __init__(self, palette):
        self.colors = {}
        for val in palette:
            self.colors[val] = palette[val]

