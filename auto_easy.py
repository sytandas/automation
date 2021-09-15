#!/usr/bin/env python3

import os
import time


def create_c():
    i = os.chdir("/Users/sayantandas/fun/automation/test/")
    file_name = time.strftime("%Y-%m-%d-%H-%M-%S.c")
    with open((file_name), 'w+') as f:
        f.write('//created a new c file!')

def create_cc():
    i = os.chdir("/Users/sayantandas/fun/automation/test/")
    file_name = time.strftime("%Y-%m-%d-%H-%M-%S.cc")
    with open(file_name, 'w+') as f:
        f.write('//created a new cc file!')
  
def create_py():
    i = os.chdir("/Users/sayantandas/fun/automation/test/")
    file_name = time.strftime("%Y-%m-%d-%H-%M-%S.py")
    with open(file_name, 'w+') as f:
        f.write('#created a new py file!')

def default():
    return "Please choose correct input 1 for c, 2 for c++, 3 for python"

print("give i/p 1 for c, 2 for c++, 3 for python")

i = int(input("please enter\n"))

if i == 1:
    print(create_c())
elif i == 2:
    print(create_cc())
elif i == 3:
    print(create_py())
else:
    print("please give i/p between 1-3 next time")
