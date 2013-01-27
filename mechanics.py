#!/usr/bin/env python27
# -*- coding: utf-8 -*-
import colorama
import sys
from colorama import Fore, Back, Style


class BaseAdventure:
    """This is a base class for all of our adventure objects."""

    def __init__(self, name):
        self.name = name
        self.description = ""

    def look(self):
        return self.description


class Character(BaseAdventure):
    def __init__(self, name, startarea):
        self.name = name
        self.location = startarea
        self.inventory = dict()

    def move(self, direction):
        if self.location.exits[direction]:
            self.location = self.location.exits[direction]
            self.look()

    def look(self):
        print self.location.look()


class Area(BaseAdventure):
    # it my be cool to try and use with Area(blarg) as room:
    # we would need to define __enter__ and __exit__
    def __init__(self, name):
        self.exits = dict()

    def addPath(self, direction, area):
        self.exits[direction] = area


class Game:
    def __init__(self):
        first = Area("first")
        first.description = "this is first area"
        second = Area("second")
        second.description = "this is the second area"
        first.addPath("south", second)
        self.maincharacter = Character("ranman", first)

    def parse_command(self, commandstr):
        command = commandstr.split()
        if "go" == command[0]:
            self.maincharacter.move(command[1])
        if "look" == command[0]:
            self.maincharacter.look()

    def run(self):
        colorama.init(autoreset=True)  # automatically reset colors
        prompt_str = ''.join(['\n', Fore.RED, '> '])
        try:
            while True:
                commandstr = raw_input(prompt_str).lower().strip()
                if not commandstr:
                    continue
                self.parse_command(commandstr)
        except (KeyboardInterrupt, EOFError):
            print "\n Good Game!"
            sys.exit()

if __name__ == '__main__':
    game = Game()
    game.run()
