import defs
import time
import sys
import configparser
import backpack
import os
import textyoptions


def type(str):
    for letter in str:
        print(letter, end='')
        time.sleep(textyoptions.numberspeed)
    print("\n")

defs.cls()
defs.pause()
print("Swag")
time.sleep(5)
print("swag")
defs.pause()

while defs.stage != "1":
    defs.cls()
    defs.dotdotdot(time.sleep(0.5))
    defs.sleepcounter = defs.sleepcounter + 1
    if defs.sleepcounter == 3:
        type("The voices grow distant as you slowly drift deeper asleep, never to wake again.")
        input("Press enter to continue.")
        GameOver()
    type("You drift aimlessly and as you do, you hear a faint voice.")
    defs.wait(1)
    type("1. Wake.")
    defs.wait(1)
    type("2. Sleep.")
    defs.stage = input(defs.ans)
        

if defs.stage == "1":
    defs.cls()
    type("You wake up.")
    defs.pause()
    type("A tall, gray figure hulks over you.")
    defs.pause()      
    type("???: 'Is he awake?'")
    defs.wait(1)
    type("???: ...")
    defs.wait(2)
    type("???: 'I believe so.'")
    defs.pause()
    if defs.sleepcounter > 1:
        type("???: 'Oh my, a moment later and I would've ended his suffering.'")      
        defs.pause()

while defs.name == "":
    defs.cls()
    type("???: 'Can you hear me? Have you got a name, and if so, what is it?'")
    defs.name = input(defs.ans)
    if defs.name == "no":
        type("???: 'Oh, well I'm sure you will, in time.'")
        defs.name = "Stranger"
        
if defs.name != "Stranger":
    defs.cls()
    type("???: '" + defs.name + ", is that it?'")
    while defs.yon(defs.ans):
        defs.cls()
        type("???: 'Then what is it?'")
        defs.name = input(defs.ans)
        defs.cls()
        type("???: '" + defs.name + ", is that correct?'")
defs.wait(1)

defs.cls()
type("???: 'It's a pleasure, " + defs.name + ". Name's Flay.")
defs.pause()
type("Flay: 'I, along with my goblin friend here, Gaam, found you lying in \nthe nearby woods'")
defs.pausekeep()
type("Gaam: 'Hello.'")
defs.pause()
type("Gaam: 'That was almost 48 hours ago, drowsy!")
defs.pause()
type("Flay: 'Here, have some fried Sqeck.'")
defs.pause()
backpack(backpack, 'sqeck', 1)
backpack.backpack['sqeck'] = backpack.backpack['sqeck'] + 1
item = 'Fried Sqeck'
nr = '1'
print(itemgot)
defs.pause()
