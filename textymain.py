import time
import configparser
import winsound
import os
import defs


menu = 4
menutime = 0
sleepcounter = 0

configPath = (os.path.dirname(os.path.realpath(__file__))) + "\data.cfg"
config = configparser.RawConfigParser()
config.read(configPath)

#///--Appplication Launch--\\\#
while menu == 4:
    defs.cls()
    defs.introscreen()
    print("Welcome, to " + defs.gamename + ", an interactve game.")
    if (menutime == 0):
        input("Press enter to begin")
    print("1. Start Game")
    print("2. Options")
    print("3. Get info")
    print("x. Exit")

    menu = input(defs.ans)
    if menutime != 1:
        menutime = 1
        5
    if menu == "1":
        break
    while menu == "2":
        defs.cls()
        print("1. Text Options")
        print("x. Back")
        optionmenu = input(defs.ans)
        if optionmenu == "x":
            break
        while optionmenu == "1":
            defs.cls()
            print("1. Text Mode: Instant")
            print("2. Text Mode: Fast")
            print("3. Text Mode: Medium")
            print("4. Text mode: Slow")
            print("i. Info")
            print("x. Back")
            textoption = input(defs.ans)
            if textoption == "1":
                config.set('info', 'speed', 'instant')  #speed set to instant
                defs.cls()
                print("Text speed set to " + config['info']['speed'] + ".")             
                defs.pause()
                menu = 4
            if textoption == "2":                   
                config.set('info', 'speed', 'fast')     #speed set to fast
                defs.cls()
                print("Text speed set to " + config['info']['speed'] + ".")
                defs.pause()
                menu = 4
            if textoption == "3":                   
                config.set('info', 'speed', 'medium')   #speed set to medium
                defs.cls()
                print("Text speed set to " + config['info']['speed'] + ".")
                defs.pause()
                menu = 4
            if textoption == "4":
                config.set('info', 'speed', 'slow')     #speed set to slow
                defs.cls()
                print("Text speed set to " + config['info']['speed'] + ".")
                defs.pause()
                defs.tomenu()
            if textoption == "x":
                break
            if textoption == "i":
                defs.cls()
                print("Instant = Text pop-ups instantly.")
                print("Fast    = 600 words per minute")
                print("Medium  = 400 words per minute")
                print("Slow    = 300 words per minute")
                defs.pause()
                
    if menu == "x":
        defs.cls()
        print("Bye!")
        defs.pause()
        defs.quit()
    
    if menu == "3":
        textspeed = config['info']['speed']
        defs.cls()
        print(defs.gamename + " is an interactive text adventure.")
        print("When prompted, simply enter the number listed next to the choice you wish to make.")
        print("At times, you will have to enter 'yes' or 'no' if such a question is asked.")
        print("Text speed set to " + textspeed + ".")
        defs.pause()
        menu = 4
        
    else:
        defs.cls()
        menu = 4

import textyoptions
