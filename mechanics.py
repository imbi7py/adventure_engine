#!/usr/bin/env python27
# -*- coding: utf-8 -*-
import colorama
import sys
from colorama import Fore, Back, Style
colorama.init(autoreset=True)


def parse_command(commandstr):
    print commandstr


def run():
    prompt_str = '\n' + Fore.RED + '> '
    try:
        while True:
            commandstr = raw_input(prompt_str).lower().strip()
            if not commandstr:
                continue
            parse_command(commandstr)
    except KeyboardInterrupt:
        sys.exit()

if __name__ == '__main__':
    run()
