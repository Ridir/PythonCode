import time
import sys
import configparser
import os

menu = 4
sleepcounter = 0
ans = "Answer: "
name = ""
a = ""
go = "Game over"
namebol = "no"
GAMENAME = "Swagster"

config = configparser.RawConfigParser()
config.read("C:\\config.cfg")
textspeed = config.get('info', 'speed')

if textspeed == "fast":
    def type(str):
        for letter in str:
            print(letter, end='')
            time.sleep(0.02)
        print("\n")
if textspeed == "medium":
    def type(str):
        for letter in str:
            print(letter, end='')
            time.sleep(0.05)
        print("\n")
if textspeed == "instant":
    def type(str):
        for letter in str:
            print(letter, end='')
        print("\n")



def GameOver():
    while True:
        print(go)
        time.sleep(0.9)



def cls():
    print("\n" * 100)      
def rest():
    time.sleep(1)
def wait1():
    time.sleep(0.5)
def wait2():
    time.sleep(1)
def wait3():
    time.sleep(1.5)
def wait4():
    time.sleep(2)
    
def pause():
        input("Press enter to continue...")
        cls()



print("Welcome, to " + GAMENAME + ". Enjoy your stay!")
pause()

while menu == 4:
    
    print("1. Start Game")
    print("2. Options")
    print("3. Exit")

    menu = input(ans)

    if menu == "1":
        textspeed = "fast"
        a1 = "1"
        break
    if menu == "2":
        cls()
        print("1. Text Options")
        optionmenu = input(ans)
        if optionmenu == "1":
            cls()
            print("1. Text Mode: Instant")
            print("2. Text Mode: Fast")
            print("3. Text Mode: Medium")
            option = input(ans)
            if option == "1":
                config.set('info', 'speed', 'instant')
                cls()
                print("Text speed set to instant.")
                pause()
                
            if option == "2":
                config.set('info', 'speed', 'fast')
                cls()
                print("Text speed set to fast.")
                pause()
                menu = 4
            if option == "3":
                config.set('info', 'speed', 'medium')
                cls()
                print("Text speed set to medium.")
                pause()
                menu = 4
    if menu == 3:
        cls()
        print("Bye!")
        quit()
            
while a1 == "1":
    sleepcounter = sleepcounter + 1
    if sleepcounter == 5:
        type("A cold chill passes through your right arm as you fall deeper asleep, never to wake again.")
        input("Press enter to continue.")
        GameOver()
    type("You drift within nothingness, you hear a faint voice.")
    wait1()
    type("1. Wake.")
    wait1()
    type("2. Sleep.")
    wait1()
    a1 = input(ans)
    window = False
    cls()
    
if a1 == "2":
    type("You wake.")
    pause()
    type("Surgeons suround you as you lay hopitalised in a surgery clinic.")
    pause()      
    type("'Is he awake?'")
    wait1()
    type("...")
    wait2()
    type("'I believe so.")
    time.sleep(1.5)

if sleepcounter > 3:
    type("Thank god, I was close to putting him out for good'")
    wait2()
    type("The lady squeezes the contents of a syringe into the sink next to the wall to the right of the bed.")         
    pause()

while name == "":
    type("'Can you hear me? Do you remember your name? If so, what is it?'")
    name = input(ans)
    if name == "no":
        type("Ah, well I'm sure you will, in time.")
        name = "Stranger"
        
type(name + ", is that it?")
namebol = input(ans)
while namebol == "no":
    type("Then what is it?")
    name = input(ans)
    type(name + ", is that it?")
    namebol = input(ans)
wait1()

type("It's a pleasure, " + name)
pause()

