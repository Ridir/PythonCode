import os
import time
import sched
import sound
import storage
import math
import random

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
armour = storage.equip['Head'] + storage.equip['Chest'] + storage.equip['Legs'] + storage.equip['Feet'] + storage.equip['Offhand']


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
def useitem(item):
    print("swaggggg item sued bcihs the item was " + item + "!!!111!!")
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
    import textygame
    attackpower = storage.equip['Mainhand'] + baseattack
    defencepower = armour + basedefence
    health = storage.stats['Maxhp']
    enemyhp = enemymaxhp
    page = 0
    textygame.type("What?")
    dotdotdot()
    textygame.type(enemyname + " appeared!")
    pause()
    textygame.talk(enemyname, enemybattleroar)
    battle = True
    running = True
    while True and running:
        if health < 1:
            print(enemyname + " has defeated you.")
            pause()
            print(enemyfinishroar)
            dotdotdot()
            textygame.type("You faint")
            pause()
            GameOver
        if enemyhp < 1:
            textygame.type("You have defeated" + enemyname + "!")
            for i in rang(0, len(items)):
                loot(items[i * 2], items[i * 2 + 1])
                time.sleep(0.2)
            pause()
            storage.stats['playerxp'] = playerxp + xpgain
            break
        print("Chose your action!", end="")
        print("          Enemy Health [" + (round(enemyhp / (enemymaxhp / 20)) * "=") + (round(20 - (enemyhp / (enemymaxhp / 20))) * " ")  + "] " +  str(enemyhp) + "/" + str(enemymaxhp) + "HP")
        print("1. Attack\t  ", end="")
        print("          Player Health[" + (round(health / (storage.stats['Maxhp'] / 20)) * "=") + (round(20 - (health / (storage.stats['Maxhp'] / 20))) * " ")  + "] " + str(health) + "/" + str(storage.stats['Maxhp']) + "HP")
        print("2. Inventory")
        print("3. Run")
        battlemenu = input(ans)
        while battlemenu == "1":
            cls()
            print("1. Normal")
            print("2. Special")
            print("x. Back")
            battlemenuattack = input(ans)
            while battlemenuattack == 1:                       #NORMAL ATTACK
                cls()
                print("Select an attack.")
                for attack in storage.attacklist:
                    bn += 1
                    print(bn + ". ", end="")
                    print(attack)
                    if bn == 1:
                        attack1 = attack
                    if bn == 2:
                        attack2 = attack
                    if bn == 3:
                        attack3 = attack
                    if bn == 4:
                        attack4 = attack
                print("x. Back")
                bn = 0
                attackchoice = input(ans)
                if attackchoice == "1":
                    attackchoice = attack1
                if attackchoice == "2":
                    attackchoice = attack2
                if attackchoice == "3":
                    attackchoice = attack3
                if attackchoice == "4":
                    attackchoice = attack4
                if attackchoice == "x":
                    break
                textygame.type(name + " used " + attackchoice + ("!"))
                pause()
                attackpower = storage.attacklist[attackchoice] * randint(0.80, 1.20)
                damage = (attackpower / enemydefencepower) * (storage.stats['agillity'] / 200) * (storage.stats['strength'])
                if randint(1.00, 2.00) <= storage.stats['critchance']:
                    damage = damage * randint(1.25, 1.50)
                enemyhp = enemyhp - damage
                textygame.type("...")
                textygame.type(enemyname + " took " + damage + "points of damage!")
                pause()
                dotdotdot()
                time.sleep(1)
                textygame.type(enemyname + " prepares an attack!")
                pause()
                textygame.type("BLAM!")
                time.sleep(0.2)
                cls()
                textygame.type("BLAM!")
                time.sleep(0.2)
                cls()
                textygame.type("BLAM!")
                enemydamage = ((enemyattackpower / defencepower) * enemyattackpower) + 50
                playerhealth = playerhealth - enemydamage
                if playerhealth < 0:
                    playerhealth = 0
                dotdotdot()
                time.sleep(1)
                textygame.type("You took " + enemydamage + " points of damage!")
                pause()

            while battlemenuattack == 2:                       #SPECIAL ATTACK
                cls()
                print("Select an attack.")
                for attack in storage.spattacklist:
                    bn += 1
                    print(bn + ". ", end="")
                    print(attack)
                    if bn == 1:
                        attack1 = attack
                    if bn == 2:
                        attack2 = attack
                    if bn == 3:
                        attack3 = attack
                    if bn == 4:
                        attack4 = attack
                bn = 0
                attackchoice = input(ans)
                if attackchoice == 1:
                    attackchoice = attack1
                if attackchoice == 2:
                    attackchoice = attack2
                if attackchoice == 3:
                    attackchoice = attack3
                if attackchoice == 4:
                    attackchoice = attack4
                textygame.type(name + " used " + attackchoice + "!")
                pause()
                attackpower = storage.attacklist[attackchoice] * randint(0.80, 1.20)
                damage = ((attackpower / enemydefencepower) * (storage.stats['agillity'] / 200) * (storage.stats['intellect']) * attackpower) + 50
                if randint(1.00, 2.00) <= storage.stats['critchance']:
                    damage = damage * randint(1.25, 1.50)
                enemyhp = enemyhp - damage
                textygame.type("...")
                pause()
                textygame.type(enemyname + " took " + damage + " points of damage!")
                pause()
                dotdotdot()
                time.sleep(1)
                textygame.type(enemyname + " prepares an attack!")
                pause()
                textygame.type("BLAM!")
                time.sleep(0.2)
                cls()
                textygame.type("BLAM!")
                time.sleep(0.2)
                cls()
                textygame.type("BLAM!")
                enemydamage = ((enemyattackpower / defencepower) * enemyattackpower) + 50
                playerhealth = playerhealth - enemydamage
                if playerhealth < 0:
                    playerhealth = 0
                dotdotdot()
                time.sleep(1)
                textygame.type("You took " + enemydamage +" points of damage!")
                pause()

            if battlemenuattack == "x":
                cls()
                break
        while battlemenu == "2":
            cls()
            if page < 0:
                page = math.floor(len(storage.backpack) / 5)
            page %= math.floor(len(storage.backpack) / 5)
            print("  Items: \tAmount:")
            for item in range(0, 5):
                name = list(storage.backpack.keys())[item + page * 5]
                amt = str(list(storage.backpack.values())[item + page * 5])
                print(str(item + 1) + ". " + name + (max((15 - len(name)), 0)*" ") + amt)
            print("l. Next Page")
            print("k. Previous Page")
            print("x. Back")
            itemchoice = input("Which item?: ")
            if itemchoice == "x":
                break                          #FIX THIS SHIT
            elif itemchoice == "l":
                page += 1
            elif itemchoice == "k":
                page -= 1
            elif itemchoice == "1" or "2" or "3" or "4" or "5":
                useitem(storake.backpack[page * 5 + int(itemchoice) - 1 ])
        while battlemenu ==  "3":
            ri = random.randint(0, 100)
            if ri <= fleepercent:
                cls()
                textygame.type("You fled from the battle!")
                running = False
                pause()
                break
            elif ri > fleepercent:
                cls()
                textygame.type("Couldn't get away!")
                pause()
                dotdotdot()
                time.sleep(1)
                textygame.type(enemyname + " prepares an attack!")
                pause()
                textygame.type("BLAM!")
                time.sleep(0.2)
                cls()
                textygame.type("BLAM!")
                time.sleep(0.2)
                cls()
                textygame.type("BLAM!")
                enemydamage = ((enemyattackpower / defencepower) * enemyattackpower) + 50
                playerhealth = playerhealth - enemydamage
                if playerhealth < 0:
                    playerhealth = 0
                dotdotdot()
                time.sleep(1)
                textygame.type("You took " + enemydamage +" points of damage!")
                pause()
            break
