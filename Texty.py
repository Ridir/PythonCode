import time
import sys
import configparser
import os

a1 = "2"
menu = 4
sleepcounter = 0
ans = "Answer: "
name = ""
go = "Game over"
namebol = "no"
gamename = "Text-Game"

config = configparser.RawConfigParser()
config.read("D:\\config.cfg")



def GameOver():
    while True:
        print(" ame Over")
        time.sleep(0.1)
        cls()
        print("G me Over")
        time.sleep(0.1)
        cls()
        print("Ga e Over")
        time.sleep(0.1)
        cls()
        print("Gam  Over")
        time.sleep(0.1)
        cls()
        print("Game Over")
        time.sleep(0.1)
        cls()
        print("Game  ver")
        time.sleep(0.1)
        cls()
        print("Game O er")
        time.sleep(0.1)
        cls()
        print("Game Ov r")
        time.sleep(0.1)
        cls()
        print("Game Ove ")
        time.sleep(0.1)
        cls()

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
def tomenu():
    menu = 4
    cls()
def pause():
        input("Press enter to continue...")
        cls()




#///--Appplication Launch--\\\#

print("Welcome, to " + gamename + ". Enjoy your stay!")
pause()

while menu == 4:
    
    print("1. Start Game")
    print("2. Options")
    print("3. Get info")
    print("x. Exit")

    menu = input(ans)
        
    if menu == "1":
        textspeed = "fast"
        break
    while menu == "2":
        cls()
        print("1. Text Options")
        print("x. Back")
        optionmenu = input(ans)
        if optionmenu == "x":
            break
        while optionmenu == "1":
            cls()
            print("1. Text Mode: Instant")
            print("2. Text Mode: Fast")
            print("3. Text Mode: Medium")
            print("4. Text mode: Slow")
            print("i. Info")
            print("x. Back")
            textoption = input(ans)
            if textoption == "1":
                config.set('info', 'speed', 'instant')  #speed set to instant
                cls()
                print("Text speed set to instant.")             
                pause()
                menu = 4
            if textoption == "2":                   
                config.set('info', 'speed', 'fast')     #speed set to fast
                cls()
                print("Text speed set to fast.")
                pause()
                menu = 4
            if textoption == "3":                   
                config.set('info', 'speed', 'medium')   #speed set to medium
                cls()
                print("Text speed set to medium.")
                pause()
                menu = 4
            if textoption == "4":
                config.set('info', 'speed', 'slow')     #speed set to slow
                cls()
                print("Text speed set to slow.")
                pause()
                tomenu()
            if textoption == "x":
                break
            if textoption == "i":
                cls()
                print("Instant = Text pop-ups instantly.")
                print("Fast    = 600 words per minute")
                print("Medium  = 400 words per minute")
                print("Slow    = 300 words per minute")
                pause()
                
    if menu == "x":
        cls()
        print("Bye!")
        pause()
        quit()
    
    if menu == "3":
        textspeed = config['info']['speed']
        cls()
        print("Application made by Gustav.")
        print("Text speed set to " + textspeed + ".")
        pause()
        menu = 4
        
    else:
        cls()
        menu = 4
        



#///Textspeed tested at this point\\\#
if config['info']['speed'] == "instant":            #instant
    def type(str):
        for letter in str:
            print(letter, end='')
        print("\n")
if config['info']['speed'] == "fast":               #fast
    def type(str):
        for letter in str:
            print(letter, end='')
            time.sleep(0.02)
        print("\n")
if config['info']['speed'] == "normal":            #normal
    def type(str):
        for letter in str:
            print(letter, end='')
            time.sleep(0.03)            
        print("\n")
if config['info']['speed'] == "slow":               #slow
    def type(str):
        for letter in str:
            print(letter, end='')
            time.sleep(0.04)
        print("\n")
#///-------------------------------\\\#



           
while a1 == "2":
    sleepcounter = sleepcounter + 1
    if sleepcounter == 4:
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
    cls()
    
if a1 == "1":
    type("You wake.")
    pause()
    type("Surgeons suround you as you lay hopitalised in a surgery clinic.")
    pause()      
    type("'Is he awake?'")
    wait1()
    type("...")
    wait2()
    type("'I believe so.")
    pause()
    cls()

if sleepcounter > 2:
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

