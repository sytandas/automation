#!/usr/bin/env python3

""" this is a program/script for automate testing and debuging purpose for easy learning process testing piece of code
 by running this scipt open and asking what to create c/cc/python and and ready to create a file and open vim and just ready to code 
 less friction = more quality work 
"""

import os
import time
import sys
from datetime import datetime
from sys import argv


def create_c():
    os.chdir("/Users/sayantandas/Desktop/test/")  # working directory for test file
    file_name = datetime.now().strftime('%Y-%m-%d_%H-%M-%S.c')
    with open(file_name, 'w') as f:
        f.write('created a new c file!')

def create_cc():
    os.chdir("/Users/sayantandas/Desktop/test/")  # working directory for test file
    file_name = datetime.now().strftime('%Y-%m-%d_%H-%M-%S.cc')
    with open(file_name, 'w') as f:
        f.write('created a new cc file!')
  
def create_py():
    os.chdir("/Users/sayantandas/Desktop/test/")  # working directory for test file
    file_name = datetime.now().strftime('%Y-%m-%d_%H-%M-%S.py')
    with open(file_name, 'w') as f:
        f.write('created a new py file!')


