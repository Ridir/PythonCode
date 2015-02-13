import time
import sys
import configparser
import os

a1 = "2"
menu = 4
menutime = 0
sleepcounter = 0
ans = "Answer: "
name = ""
go = "Game over"
namebol = "no"
gamename = "Led"

configPath = "data.cfg"

config = configparser.RawConfigParser()
config.read(configPath)




def yon(question):
    yesorno = input(question)
    if yesorno != "yes":
        return True
    return False
def cls():
    print("\n" * 60)      
def wait(time):
    if time == 1:
        time.sleep(0.5)
    if time == 2:
        time.sleep(1.0)
    if time == 3:
        time.sleep(1.5)
    if time == 4:
        time.sleep(2.0)
def tomenu():
    menu = 4
    cls()
def pause():
        input("Press enter to continue...")
        cls()
def pausekeep():
        input("Press enter to continue...")
def dotdotdot(wait):
    wait()
    print("")
    print(".")
    wait()
    cls()
    print("..")
    wait()
    cls()
    print("...")
    wait()
    cls()

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
def introscreen():
    print("                ..:::::::::..          ")
    print("           ..:::aad8888888baa:::..      ")
    print("        .::::d:?88888888888?::8b::::. ")
    print("      .:::d8888:?88888888??a888888b:::.  ")
    print("      .:::d8888:?88888888??a888888b:::.  ")
    print("   ::::dP::::::::88888888888::::::::Yb::::       ")
    print("  ::::dP:::::::::Y888888888P:::::::::Yb::::     ")
    print(" ::::d8:::::::::::Y8888888P:::::::::::8b::::   ")
    print(".::::88::::::::::::Y88888P::::::::::::88::::.      ")
    print(":::::Y8baaaaaaaaaa88P:T:Y88aaaaaaaaaad8P:::::   ")
    print(":::::::Y88888888888P::|::Y88888888888P:::::::  ")
    print("::::::::::::::::888:::|:::888:::::::::::::::: ")
    print("`:::::::::::::::8888888888888b::::::::::::::'")
    print(" :::::::::::::::88888888888888:::::::::::::: ")
    print("  :::::::::::::d88888888888888:::::::::::::  ")
    print("   ::::::::::::88::88::88:::88::::::::::::")
    print("    `::::::::::88::88::88:::88::::::::::'")
    print("      `::::::::88::88::P::::88::::::::' ")
    print("        `::::::88::88:::::::88::::::'  ")
    print("           ``:::::::::::::::::::''    ")
    print("                ``:::::::::''        ")
    print("")


#///--Appplication Launch--\\\#
while menu == 4:
    cls()
    introscreen()
    print("Welcome, to " + gamename + ", an interactve game.")
    if (menutime == 0):
        input("Press enter to begin")
    print("1. Start Game")
    print("2. Options")
    print("3. Get info")
    print("x. Exit")

    menu = input(ans)
    if menutime != 1:
        menutime = 1
        
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
                print("Text speed set to " + config['info']['speed'] + ".")             
                pause()
                menu = 4
            if textoption == "2":                   
                config.set('info', 'speed', 'fast')     #speed set to fast
                cls()
                print("Text speed set to " + config['info']['speed'] + ".")
                pause()
                menu = 4
            if textoption == "3":                   
                config.set('info', 'speed', 'medium')   #speed set to medium
                cls()
                print("Text speed set to " + config['info']['speed'] + ".")
                pause()
                menu = 4
            if textoption == "4":
                config.set('info', 'speed', 'slow')     #speed set to slow
                cls()
                print("Text speed set to " + config['info']['speed'] + ".")
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




while a1 != "1":
    cls()
    dotdotdot(wait(1))
    sleepcounter = sleepcounter + 1
    if sleepcounter == 3:
        type("The voices grow distant as you slowly drift deeper asleep, never to wake again.")
        input("Press enter to continue.")
        GameOver()
    type("You drift aimlessly and as you do, you hear a faint voice.")
    wait(1)
    type("1. Wake.")
    wait(1)
    type("2. Sleep.")
    a1 = input(ans)
        

if a1 == "1":
    cls()
    type("You wake up.")
    pause()
    type("A tall, gray figure hulks over you.")
    pause()      
    type("???: 'Is he awake?'")
    wait(1)
    type("???: ...")
    wait(2)
    type("???: 'I believe so.'")
    pause()
    if sleepcounter > 1:
        type("???: 'Oh my, a moment later and I would've ended his suffering.'")      
        pause()

while name == "":
    cls()
    type("???: 'Can you hear me? Have you got a name, and if so, what is it?'")
    name = input(ans)
    if name == "no":
        type("???: 'Oh, well I'm sure you will, in time.'")
        name = "Stranger"
        
if name != "Stranger":
    cls()
    type("???: '" + name + ", is that it?'")
    while yon(ans):
        cls()
        type("???: 'Then what is it?'")
        name = input(ans)
        cls()
        type("???: '" + name + ", is that correct?'")
wait(1)

cls()
type("???: 'It's a pleasure, " + name + ". Name's Flay.")
pause()
type("Flay: 'I, along with my goblin friend here, Gaam, found you lying in \nthe nearby woods'")
pausekeep()
type("Gaam: 'Hello.'")
pause()
type("''")
