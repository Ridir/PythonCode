import os
import time
import sched
import sound
import storage

sleepcounter = 0
gamename = "Led"
ans = "Answer: "
stage = 2
s = sched.scheduler(time.time, time.sleep)
name = ""
namebol = "no"
trainbol = ""
go = "Game over"
battlemenu = 0
bn = 0
weaponswag = ""
gamepath = os.path.dirname(os.path.realpath(__file__))

#Attack/Defence
baseattack = 50
basedefence = 50
armour = storage.equip['head'] + storage.equip['chest'] + storage.equip['legs'] + storage.equip['feet'] + storage.equip['offhand']


def loot(items, nr):
    storage.backpack[items] = storage.backpack[items] + nr
    nr = str(nr)
    sound.loot()
    cleandotdotdot()
    print(nr + " " + items + " added to backpack!")
def equip(item, slot):
    storage.equip[slot] = storage.gear[item]
    sound.equip()
    print(item + " was equiped!")
    pause()
    cls()
def yon(question):
    yesorno = input(question)
    if yesorno != "yes":
        return True
    return False
def cls():
    print("\n" * 25)      
def tomenu():
    menu = 4
    cls()
def pause():
        input("Press enter to continue...")
        time.sleep(0.0)
        cls()
def dotdotdot():
    time.sleep(0.5)
    print(".", end="")
    time.sleep(0.5)
    print(".", end="")
    time.sleep(0.5)
    print(".", end="")
    time.sleep(1.0)
    cls()
def cleandotdotdot():
    time.sleep(0.5)
    print(".", end="")
    time.sleep(0.5)
    print(".", end="")
    time.sleep(0.5)
    print(".", end="")
def GameOver():
    sound.gameover()
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

def battle(enemyname, enemymaxhp, enemydefencepower, enemyattackpower, fleepercent, enemybattleroar, enemyfinishroar, items, xpgain):
    print("swag")