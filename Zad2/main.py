import json_loader
import properties
import figures
import os, sys, pygame
from pygame.locals import *


def load_figures(figures_table, content, palette):
    for figure in content:
            if figure["type"] == "point":
                figures_table.append(figures.Point(figure, palette))
            elif figure["type"] == "square":
                figures_table.append(figures.Square(figure, palette))
            elif figure["type"] == "rectangle":
                figures_table.append(figures.Rectangle(figure, palette))
            elif figure["type"] == "circle":
                figures_table.append(figures.Circle(figure, palette))
            elif figure["type"] == "polygon":
                figures_table.append(figures.Polygon(figure, palette))
            else:
                print("Unknown type of figure")

def main(argv):
    content = json_loader.read_file(argv[1])
    screen = properties.Screen(json_loader.read_screen_settings(content))
    palette = properties.Palette(json_loader.read_palette(content))

    if screen.fg_color in palette.colors:
        figures.fg_color = palette.colors[screen.fg_color]
    else:
        figures.fg_color = "#abcdef"

    figures_table = []
    load_figures(figures_table, content["Figures"], palette)

    screen.start(palette)
    pygame.init()

    for figure in figures_table:
        figure.draw(screen.screen)

    pygame.display.update()

    while 1:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.image.save(screen.screen, "file.png")
                pygame.display.quit()
                sys.exit(0)
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.display.quit()
                sys.exit(0)


if __name__ == '__main__':
    main(sys.argv)
