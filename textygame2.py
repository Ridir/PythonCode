import defs
import time
import sys
import configparser
import storage
import os
import textyoptions


def type(str):
    for letter in str:
        print(letter, end='', flush=True)
        time.sleep(textyoptions.numberspeed)
    print("\n")
def talk(name, str):
    print(name + ": '", end="")
    for letter in str:
        print(letter, end='', flush=True)
        time.sleep(textyoptions.numberspeed)
    print("'")
    print("\n")


defs.cls()
talk("???", "It's a pleasure, " + defs.name + ". Name's Flay.")
defs.pause()
talk("Flay", "Seems like you were in quite a fight, huh, bruises all over you.")
defs.pause()
talk("Flay", "I, along with my goblin friend here, Gaam, found you lying nearby \nnext to some ageold oaks.")
defs.pause()
talk("Gaam", "Hello.")
defs.pause()
talk("Flay", "We, and with that I mean 'I', dragged you all the way back to our \ncottage.")
defs.pause()
talk("Flay", "That was almost 48 hours ago.")
defs.pause()
talk("Gaam", "Have sum fried Sqeck, Bedhead.")
defs.pause()
defs.loot('sqeck', 1)
defs.pause()
talk("Gaam", "Eventualy, once you're in a tough situation, you'll thank me\n for that fried godness.")
defs.pause()
talk("Flay", "Now that you're awake, why don't you come with me, seems like you\n could do with some combat training, considering \nyour situation, or would you rather leave it be?")
defs.trainbol = input(ans)
while defs.trainbol != "yes" or "no":
    talk("Flay", "Sorry, what? Allow me to repeat, do you need training, yes or no?")


while trainbol == "yes":
    