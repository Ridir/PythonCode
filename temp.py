import time
import sys
import configparser
import os

a1 = "2"
menu = 4
sleepcounter = 0
ans = "Answer: "
name = ""
a = ""
go = "Game over"
namebol = "no"
GAMENAME = "Swagster"
test = "Ingen ändring"

config = configparser.RawConfigParser()
config.read("D:\\config.cfg")
textspeed = config.get('info', 'speed')

if config['info']['speed'] == "fast":
    def type(str):
        for letter in str:
            print(letter, end='')
            time.sleep(0.02)
        print("\n")
if config['info']['speed'] == "medium":
    def type(str):
        for letter in str:
            print(letter, end='')
            time.sleep(0.05)
        print("\n")
if config['info']['speed'] == "instant":
    def type(str):
        for letter in str:
            print(letter, end='')
        print("\n")
