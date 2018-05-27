import json
import sys

def read_file(filepath):
    try:
        with open(filepath) as content:
            json_content = json.load(content)
        return json_content
    except FileNotFoundError:
        print("File not found")
        sys.exit(1)


def read_screen_settings(content):
    try:
        return content["Screen"]
    except KeyError:
        print("Screen JSON reading: KeyError")
        sys.exit(1)


def read_palette(content):
    try:
        return content["Palette"]
    except KeyError:
        print("Palette JSON reading: KeyError")
        sys.exit(1)
