import defs
import time
import sys
import configparser
import backpack
import os

sleepcounter = 0
gamename = "Led"
ans = "Answer: "
stage = 2
name = ""
namebol = "no"
go = "Game over"

def backpack(container, items, nr):
    backpack.container[items] = backpack.container[items] + 1
    print(nr + items + " added to backpack!")
def yon(question):
    yesorno = input(question)
    if yesorno != "yes":
        return True
    return False
def cls():
    print("\n" * 25)      
def wait(timer):
    if timer == 1:
        time.sleep(0.5)
    if timer == 2:
        time.sleep(1.0)
    if timer == 3:
        time.sleep(1.5)
    if timer == 4:
        time.sleep(2.0)
def tomenu():
    menu = 4
    cls()
def pause():
        input("Press enter to continue...")
        cls()
def pausekeep():
        input("Press enter to continue...")
def dotdotdot(waiter):
    waiter
    print(".")
    waiter
    cls()
    print("..")
    waiter
    cls()
    print("...")
    waiter
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
