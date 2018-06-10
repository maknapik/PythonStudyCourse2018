import sys
import pygame
import properties
import logging

fg_color = ""

class Figure:
    def __init__(self, content, palette):
        try:
            self.type = content["type"]
        except:
            print("Figure initialize type: KeyError")
            sys.exit(1)

        try:
            if content["color"] in palette.colors:
                self.color = pygame.Color(palette.colors[content["color"]])
            else:
                self.color = pygame.Color(content["color"])
        except:
            self.color = pygame.Color(fg_color)
            logging.warning("Wrong format of color or color not defined. Set default.");

    def draw(self, screen):
        pass


class Point(Figure):
    def __init__(self, content, palette):
        try:
            super().__init__(content, palette)
        except:
            logging.error("Point super() initialize: KeyError");
            sys.exit(1)

        try:
            self.x = content["x"]
            self.y = content["y"]
        except:
            logging.error("Point point initialize: KeyError");
            sys.exit(1)

    def draw(self, screen):
        pygame.draw.line(screen, self.color, (self.x, self.y), (self.x, self.y))


class Square(Figure):
    def __init__(self, content, palette):
        try:
            super().__init__(content, palette)
        except:
            logging.error("Square super() initialize: KeyError");
            sys.exit(1)

        try:
            self.x = content["x"]
            self.y = content["y"]
        except:
            logging.error("Square point initialize: KeyError");
            sys.exit(1)

        try:
            self.size = content["size"]
        except:
            logging.error("Square size initialize: KeyError");
            sys.exit(1)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))


class Rectangle(Figure):
    def __init__(self, content, palette):
        try:
            super().__init__(content, palette)
        except:
            logging.error("Rectangle super() initialize: KeyError");
            sys.exit(1)

        try:
            self.x = content["x"]
            self.y = content["y"]
        except:
            logging.error("Rectangle point initialize: KeyError");
            sys.exit(1)

        try:
            self.width = content["width"]
            self.height = content["height"]
        except:
            logging.error("Rectangle size initialize: KeyError");
            sys.exit(1)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))


class Circle(Figure):
    def __init__(self, content, palette):
        try:
            super().__init__(content, palette)
        except:
            logging.error("Circle super() initialize: KeyError");
            sys.exit(1)

        try:
            self.x = content["x"]
            self.y = content["y"]
        except:
            logging.error("Circle point initialize: KeyError");
            sys.exit(1)

        try:
            self.radius = content["radius"]
        except:
            logging.error("Circle radius initialize: KeyError");
            sys.exit(1)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius, 0)  # filled


class Polygon(Figure):
    def __init__(self, content, palette):
        try:
            super().__init__(content, palette)
        except:
            logging.error("Polygon super() initialize: KeyError");
            sys.exit(1)

        try:
            self.points = []
            for point in content["points"]:
                self.points.append(point)
        except:
            logging.error("Polygon points initialize: KeyError");
            sys.exit(1)

    def draw(self, screen):
        pygame.draw.polygon(screen, self.color, self.points, 0)