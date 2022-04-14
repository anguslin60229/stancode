"""
File: Steeplechase.py
Name: TODO:
---------------------------------
TODO:
"""

from karel.stanfordkarel import *


def main():
    """
    Karel crosses hurdles in a 12x12 world
    with a for loop 
    """
    for i in range(11):
        if front_is_clear():
            move()
            put_beeper99()
        else:
            jump()


def jump():
    up()
    cross()
    down()


def up():
    turn_left()
    while not right_is_clear():
        move()
        put_beeper99()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def cross():
    turn_right()
    move()
    put_beeper99()
    turn_right()


def down():
    move()
    put_beeper99()
    while front_is_clear():
        move()
        put_beeper99()
    turn_left()

def put_beeper99():
    for i in range(1000):
        put_beeper()
















####### DO NOT EDIT CODE BELOW THIS LINE ########

if __name__ == '__main__':
    execute_karel_task(main)
