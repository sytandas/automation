#!/usr/bin/env python3

import os
import time
import csv

def create_file():
    cwd = [os.getcwd()]
    os.chdir = ("cwd")
    file = input("file name:\n") 
    with open((file), 'w+') as f:
        f.write('')

create_file()
