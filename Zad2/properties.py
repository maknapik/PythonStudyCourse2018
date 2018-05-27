import sys, pygame

class Screen:
    def __init__(self, screen):
        try:
            self.width = screen["width"]
        except KeyError:
            print("Screen initialize width: KeyError")
            sys.exit(1)

        try:
            self.height = screen["height"]
        except KeyError:
            print("Screen initialize height: KeyError")
            sys.exit(1)

        try:
            self.bg_color = screen["bg_color"]
        except KeyError:
            print("Screen initialize bg_color: KeyError")
            sys.exit(1)

        try:
            self.fg_color = screen["fg_color"]
        except KeyError:
            print("Screen initialize fg_color: KeyError")
            sys.exit(1)

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

