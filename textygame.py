import defs
import textyoptions
import time
import threading
import sound
i = 0

def type(str):
    for letter in str:
        print(letter, end='', flush=True)
        global i
        i += 1
        if i == 4:
            sound.textbeep()
            if i == 4:
                i = 0
        time.sleep(textyoptions.numberspeed)
    print("\n")
def talk(name, str):
    print(name + ": '", end="")
    for letter in str:
        print(letter, end='', flush=True)
        global i
        i += 1
        if i == 3:
            sound.textbeep()
            if i == 3:
                i = 0
        time.sleep(textyoptions.numberspeed)
    print("'")
    print("\n")

while defs.stage != "1":
    defs.battle("Sporre", 50, 50, 50, 50, "JAVA!! GLITCH!!", "SMELLS LIKE PYTHON!!", ['milk', 69], 69)
    defs.cls()
    defs.dotdotdot()
    defs.sleepcounter = defs.sleepcounter + 1
    if defs.sleepcounter == 3:
        type("The voices grow distant as you slowly drift deeper asleep, never to wake again.")
        input("Press enter to continue.")
        defs.GameOver()
    type("You drift aimlessly and as you do, you hear a faint voice.")
    time.sleep(0.5)
    type("1. Wake.")
    time.sleep(0.5)
    type("2. Sleep.")
    defs.stage = input(defs.ans)
        

if defs.stage == "1":
    defs.cls()
    type("You wake up.")
    defs.pause()
    type("A tall, gray figure hulks over you.")
    defs.pause()      
    talk("???", "Is he awake?")
    time.sleep(0.5)
    print("???: '", end="")
    defs.cleandotdotdot()
    print("'")
    time.sleep(1)
    print("\n")
    talk("???",  "I believe so.")
    defs.pause()
    if defs.sleepcounter > 1:
        defs.cls()
        talk("???", "Oh my, a moment later and I would've ended his suffering.")      
        defs.pause()

while defs.name == "":
    defs.cls()
    talk("???", "Can you hear me? Do you remember your name, and if so, what is it?")
    defs.name = input(defs.ans)        

    if defs.name == "no":
        talk("???",  "Oh, well I'm sure you will, in time.")
        defs.name = "Stranger"
if defs.name != "Stranger":
    defs.cls()
    talk("???", defs.name + ", is that it?")
    while defs.yon(defs.ans):
        defs.cls()
        talk("???", "Then what is it?")
        defs.name = input(defs.ans)
        defs.cls()
        talk("???", defs.name + ", is that correct?")
time.sleep(1.5)

import textygame2