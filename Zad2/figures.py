import pygame
import properties

fg_color = ""

class Figure:
    def __init__(self, content, palette):
        try:
            self.type = content["type"]
        except:
            print("Figure initialize type: KeyError")

        try:
            if content["color"] in palette.colors:
                self.color = pygame.Color(palette.colors[content["color"]])
            else:
                self.color = pygame.Color(content["color"])
        except:
            self.color = pygame.Color(fg_color)

    def draw(self, screen):
        pass


class Point(Figure):
    def __init__(self, content, palette):
        try:
            super().__init__(content, palette)
        except:
            print("Point super() initialize: KeyError")

        try:
            self.x = content["x"]
            self.y = content["y"]
        except:
            print("Point point initialize: KeyError")

    def draw(self, screen):
        pygame.draw.line(screen, self.color, (self.x, self.y), (self.x, self.y))


class Square(Figure):
    def __init__(self, content, palette):
        try:
            super().__init__(content, palette)
        except:
            print("Rectangle super() initialize: KeyError")

        try:
            self.x = content["x"]
            self.y = content["y"]
        except:
            print("Rectangle point initialize: KeyError")

        try:
            self.size = content["size"]
        except:
            print("Rectangle size initialize: KeyError")

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))


class Rectangle(Figure):
    def __init__(self, content, palette):
        try:
            super().__init__(content, palette)
        except:
            print("Rectangle super() initialize: KeyError")

        try:
            self.x = content["x"]
            self.y = content["y"]
        except:
            print("Rectangle point initialize: KeyError")

        try:
            self.width = content["width"]
            self.height = content["height"]
        except:
            print("Rectangle size initialize: KeyError")

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))


class Circle(Figure):
    def __init__(self, content, palette):
        try:
            super().__init__(content, palette)
        except:
            print("Circle super() initialize: KeyError")

        try:
            self.x = content["x"]
            self.y = content["y"]
        except:
            print("Circle point initialize: KeyError")

        try:
            self.radius = content["radius"]
        except:
            print("Circle radius initialize: KeyError")

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius, 0)  # filled


class Polygon(Figure):
    def __init__(self, content, palette):
        try:
            super().__init__(content, palette)
        except:
            print("Circle super() initialize: KeyError")

        try:
            self.points = []
            for point in content["points"]:
                self.points.append(point)
        except:
            print("Polygon points initialize: KeyError")

    def draw(self, screen):
        pygame.draw.polygon(screen, self.color, self.points, 0)