#!/usr/bin/env python3

import argparse

from apps import Apps

parser = argparse.ArgumentParser(description='Runs a selected app.')
parser.add_argument('program', metavar='Program', type=str, nargs=1, help='The program name')

parser.add_argument('args', metavar='Args', type=str, nargs='*', default=None, help='Arguments for the program')



if __name__ == "__main__":
    args = parser.parse_args()
    
    program = args.program[0].lower()
    
    program_args = " ".join(args.args)

    apps = Apps()
    apps.load("apps")
    
    for app in apps.apps:
        if app.name.lower() == program:
            print(app.get_command("rhys", "winpass", "192.168.122.33"))
