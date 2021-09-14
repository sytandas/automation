#!/usr/bin/env python3

""" this is a program/script for automate testing and debuging purpose for easy learning process testing piece of code
 by running this scipt open and asking what to create c/cc/python and and ready to create a file and open vim and just ready to code 
 less friction = more quality work 
"""

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
