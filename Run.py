#!/usr/bin/env python3

import argparse
from subprocess import Popen, PIPE
import shlex

from apps import Apps


USERNAME = "rhys"
PASSWORD = "winpass"
IP = "192.168.122.33"


parser = argparse.ArgumentParser(description='Runs a selected app.')
parser.add_argument('program', metavar='Program', type=str, nargs=1, help='The program name')


parser.add_argument('--file', metavar='File', type=str, nargs=1, default=None, help='File to open')

parser.add_argument('args', metavar='Args', type=str, nargs='*', default=None, help='Arguments for the program')



if __name__ == "__main__":
    args = parser.parse_args()
    
    program = args.program[0].lower()
    
    program_args = args.args
    
    file = ""
    
    if args.file:
        file = args.file[0]
        
    if file:
        file =  "\\\\\\\\tsclient{}".format(file.replace("/home/rhys", "/home").replace("/", "\\\\")) # so many backslashes
        
    print(file)

    apps = Apps()
    apps.load("apps")
    
    for app in apps.apps:
        if app.name.lower() == program:
            command = app.get_command(USERNAME, PASSWORD, IP, [file]+program_args)
            
            command_split = shlex.split(command)
            
            print(command)
            
            proc = Popen(command_split, stdout=PIPE, stderr=PIPE)
            proc.wait()
            
            break
