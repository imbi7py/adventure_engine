#!/usr/bin/env python27
# -*- coding: utf-8 -*-
import sys
import yaml
import colorama
from colorama import Fore, Back, Style


class BaseAdventure:
    """This is a base class for all of our adventure objects."""

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def look(self):
        return self.description

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


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
        try:
            self.location.inventory.push(self.location.remove(item))
        except:
            print "Couldn't drop {}".format(item)

    def take(self, item):
        try:
            self.inventory.push(self.location.inventory.remove(item))
        except:
            print "Couldn't take {}".format(item)

    def look(self):
        look_str = "You find yourself in {}\n {}\n Objects: {}\n Exits: {}"
        return look_str.format(
            self.location,
            self.location.description,
            self.location.inventory,
            self.location.exits)


class Area(BaseAdventure):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = dict()
        self.inventory = []

    def addPath(self, direction, area):
        self.exits[direction] = area


class Item(BaseAdventure):
    def __init__(self, name, description, hidden=False):
        self.name = name
        self.description = description
        self.hidden = hidden

    def __str__(self):
        return ''.join([Fore.BLUE, self.name])


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
            print self.maincharacter.look()
        if "take" == command[0]:
            self.maincharacter.take(command[1])
        if "drop" == command[0]:
            self.maincharacter.drop(command[1])

    def run(self):
        colorama.init(autoreset=True)  # automatically reset colors
        prompt_str = ''.join(['\n', Fore.RED, '> '])
        try:
            print self.maincharacter.look()
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
