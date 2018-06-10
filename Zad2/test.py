import unittest
import json_loader
import properties
import figures
import pygame


figures.fg_color = "#abcdef"


class UnitTests(unittest.TestCase):
    def test_color(self):
        content = json_loader.read_file("file.json")
        palette = properties.Palette(json_loader.read_palette(content))
        figure = {"type": "point", "x": 10, "y": 50}
        point = figures.Point(figure, palette)
        self.assertEqual(point.color, pygame.Color("#abcdef"))

    def test_point(self):
        content = json_loader.read_file("file.json")
        palette = properties.Palette(json_loader.read_palette(content))
        figure = {"type": "point", "x": 10, "y": 50}
        point = figures.Point(figure, palette)
        self.assertEqual(point.x, 10)
        self.assertEqual(point.y, 50)

    def test_size(self):
        content = json_loader.read_file("file.json")
        palette = properties.Palette(json_loader.read_palette(content))
        figure = {"type": "rectangle", "x": 100, "y": 50, "width": 200, "height": 50}
        rectangle = figures.Rectangle(figure, palette)
        self.assertEqual(rectangle.width, 200)
        self.assertEqual(rectangle.height, 50)


if __name__ == '__main__':
    unittest.main()
