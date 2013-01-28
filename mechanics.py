#!/usr/bin/env python27
# -*- coding: utf-8 -*-
import colorama
import sys
from colorama import Fore, Back, Style


class BaseAdventure:
    """This is a base class for all of our adventure objects."""

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def look(self):
        return self.description


class Character(BaseAdventure):
    def __init__(self, name, startarea):
        self.name = name
        self.location = startarea
        self.inventory = []

    def move(self, direction):
        area = self.location.exits.get(direction, None)
        if area:
            self.location = self.location.exits[direction]
            self.look()
        else:
            print "You don't see any way to go {}".format(direction)

    def drop(self, item):
        item = self.location.remove(item)
        if item:
            self.location.push(item)
        else:
            print "Couldn't drop {}".format(item)

    def look(self):
        print self.location.look()


class Area(BaseAdventure):
    def __init__(self, name, description):
        self.exits = dict()
        self.description = description
        self.inventory = []

    def addPath(self, direction, area):
        self.exits[direction] = area


class Item(BaseAdventure):
    def put(self, location):
        location.inventory.push(self)


class Game:
    def __init__(self):
        first = Area("first", "this is first area")
        second = Area("second", "this is the second area")
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
