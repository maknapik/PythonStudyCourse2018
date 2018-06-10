import json_loader
import properties
import figures
import os, sys, getopt, pygame
from pygame.locals import *

import test


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
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
    except:
        print("main.py -i <inputfile> [-o <outputfile>]")
        sys.exit(1)
    for opt, arg in opts:
        if opt == '-h':
            print("main.py -i <inputfile> [-o <outputfile>]")
            sys.exit(0)
        elif opt in ("-i", "--input"):
            inputfile = arg
        elif opt in ("-o", "--output"):
            outputfile = arg

    content = json_loader.read_file(inputfile)
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
    pygame.display.set_caption('Python drawer')

    for figure in figures_table:
        figure.draw(screen.screen)

    pygame.display.update()

    while 1:

        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                if outputfile != '':
                    pygame.image.save(screen.screen, outputfile)
                pygame.display.quit()
                sys.exit(0)
            elif event.type == pygame.locals.KEYDOWN and event.key == pygame.locals.K_ESCAPE:
                if outputfile != '':
                    pygame.image.save(screen.screen, outputfile)
                pygame.display.quit()
                sys.exit(0)


if __name__ == '__main__':
    main(sys.argv[1:])
