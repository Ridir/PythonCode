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
talk("Flay", "Now that you're awake, why don't you come with me, seems like you\n could do with some combat training, considering \nyour situation.")
defs.pause()
talk("Flay", "This way.")
desf.pause()
type("You exit the cottage, to an area contained within a frail fence.")
defs.pause()
type("To the east, a thick, old forest spreads, presumably where you came form.")
defs.pause()
type("To the North, a giant hill obscures your vision of anything beyond it.")
defs.pause()
type("To the west and south, plains of yellow grass lay like a thin bedcover.")
defs.pause()
defs.cls()
type("By the frail fence, a worn sack of hay impaled upon a pole represents a training dummy.")
defs.pause()
defs.cls()
type("Fray points towards a weaponrack, situated right besides the exit.")
talk("Fray", "I allow you to pick one of these weapons toa accompany you from this point on.")
defs.pause()
defs.cls
talk("Fray", "Of course, should you change your mind you can always get your hands on weapons like these from elsewhere.")
defs.pause()
defs.cls()
while(defs.weaponswag == ""):
    print("Pick one of the following weapons:")
    print("1. Rugged Sword")
    print("2. Rugged Bow")
    print("3. Rugged Staff")
    weaponswag = input(ans)
    if(weaponswag != "1" or "2" or "3"):
        weaponswag = ""
    if weaponswag == "1":
        talk("Flay", "A sword huh? Works great against light armor, at close range. ")
        weaponbol = input("Confirm(yes/no)?: ")
        if weaponbol = "yes":
            storage.gear['ruggedsword'] = 2
            equip('ruggedsword', 'mainhand')
    if weaponswag == "2":
        talk("Flay", "A bow, huh? Works great against most armor from a distance, doesn't work all that well with heavier armour though...")
        weaponbol = input("Confirm(yes/no)?: ")
        if weaponbol = "yes":
           storage.gear['ruggedbow'] = 4
            equip('ruggedbow', 'mainhand')
    if weaponswag == "3":
        talk("Flay", "A staff, huh? Works great against all kinds of armour from a distance, heavier armour with strong enchantments are hard to come by though.")
        weaponbol = input("Confirm(yes/no)?: ")
        if weaponbol = "yes":
            storage.gear['ruggedstaff'] = 5
            equip('ruggedstaff', 'mainhand')

defs.cls()
talk("Flay", "Great!")
defs.pause()
talk("Flay", "Now, face off aginst that dummy over there.")
defs.pause()
talk("Flay", "Do you need me to go over the basic principles of fighting, or can you handke yourself?")
defs.cls()
defs.trainbol = input(ans)
defs.cls()
while defs.trainbol != "1" or "2":
    talk("Flay", "Sorry, what? Allow me to repeat; do you need training, yes or no?")
    defs.pause()
    defs.cls()
if trainbol == "1":
    talk("Flay", "Alrighty then, here goes.")
    defs.pause()
if trainbol == "2":
    talk("Flay", "Suit yourself!")
    defs.pause()

enemyhp = enemymaxhp
type("What?")
defs.dotdotdot()
type(enemyname + " appeared!")
defs.pause()
talk(enemyname, enemybattleroar)
defs.pause()



while True
    if health < 1:
        print(enemyname + " has defeated you.")
        defs.pause()
        print(enemyfinishroar)
        defs.dotdotdot()
        type("You faint")
        defs.pause()
        defs.GameOver
    if enemyhp < 1:
        type("You have defeated" + enemyname + "!")
        for i in rang(0, len(items)):
            loot(items[i * 2], items[i * 2 + 1])
            time.sleep(0.2)
        pause()
        storage.stats['playerxp'] = playerxp + xpgain
        break
    print("Chose your action!", end="")
    print("          Enemy Health [" + (enemyhp / (enemymaxhp / 20)) * "=" + (20 - (enemyhp / (enemymaxhp / 20)) * " ")  + "]" + enemyhp + " / " + enemymaxhp + "HP")
    print("1. Attack", end="")
    print("          Player Health[" + (health / (maxhealth / 20)) * "=" + (20 - (health / (maxhealth / 20)) * " ")  + "]" + health + " / " + maxhealth + "HP")
    print("2. Inventory")
    print("3. Run")
    battlemenu = input(ans)
    while battlemenu == "1":
        defs.cls()
        print("1. Normal")
        print("2. Special")
        print("x. Back")
        battlemenuattack = input(ans)
        while battlemenuattack == 1:                       #NORMAL ATTACK
            defs.cls()
            print("Select an attack.")
            for attack in storage.attacklist:
                defs.bn += 1
                print(bn + ". ", end="")
                print(attack)
                if defs.bn == 1:
                    attack1 = attack
                if defs.bn == 2:
                    attack2 = attack
                if defs.bn == 3:
                    attack3 = attack
                if defs.bn == 4:
                    attack4 = attack
            print("x. Back")
            defs.bn = 0
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
            type(name + " used " + attackchoice + ("!"))
            defs.pause()
            attackpower = storage.attacklist[attackchoice] * randint(0.80, 1.20)
            damage = (attackpower / enemydefencepower) * (storage.stats['agillity'] / 200) * (storage.stats['strength'])
            if randint(1.00, 2.00) <= storage.stats['critchance']:
                damage = damage * randint(1.25, 1.50)
            enemyhp = enemyhp - damage
            type("...")
            type(enemyname + " took " + damage "points of damage!")
            defs.pause()
            defs.dotdotdot()
            time.sleep(1)
            type(enemyname + " prepares an attack!")
            defs.pause()
            type("BLAM!")
            time.sleep(0.2)
            defs.cls()
            type("BLAM!")
            time.sleep(0.2)
            defs.cls()
            type("BLAM!")
            enemydamage = ((enemyattackpower / defencepower) * enemyattackpower) + 50
            playerhealth = playerhealth - enemydamage
            if playerhealth < 0:
                playerhealth = 0
            defs.dotdotdot()
            time.sleep(1)
            type("You took " + enemydamage +" points of damage!")
            defs.pause()

        while battlemenuattack == 2:                       #SPECIAL ATTACK
            defs.cls()
            print("Select an attack.")
            for attack in storage.spattacklist:
                defs.bn += 1
                print(bn + ". ", end="")
                print(attack)
                if defs.bn == 1:
                    attack1 = attack
                if defs.bn == 2:
                    attack2 = attack
                if defs.bn == 3:
                    attack3 = attack
                if defs.bn == 4:
                    attack4 = attack
            defs.bn = 0
            attackchoice = input(ans)
            if attackchoice == 1:
                attackchoice = attack1
            if attackchoice == 2:
                attackchoice = attack2
            if attackchoice == 3:
                attackchoice = attack3
            if attackchoice == 4:
                attackchoice = attack4
            type(name + " used " + attackchoice + ("!"))
            defs.pause()
            attackpower = storage.attacklist[attackchoice] * randint(0.80, 1.20)
            damage = ((attackpower / enemydefencepower) * (storage.stats['agillity'] / 200) * (storage.stats['intellect']) * attackpower) + 50
            if randint(1.00, 2.00) <= storage.stats['critchance']:
                damage = damage * randint(1.25, 1.50)
            enemyhp = enemyhp - damage
            type("...")
            type(enemyname " took " + damage + " points of damage!")
            defs.pause()
            defs.dotdotdot()
            time.sleep(1)
            type(enemyname + " prepares an attack!")
            defs.pause()
            type("BLAM!")
            time.sleep(0.2)
            defs.cls()
            type("BLAM!")
            time.sleep(0.2)
            defs.cls()
            type("BLAM!")
            enemydamage = ((enemyattackpower / defencepower) * enemyattackpower) + 50
            playerhealth = playerhealth - enemydamage
            if playerhealth < 0:
                playerhealth = 0
            defs.dotdotdot()
            time.sleep(1)
            type("You took " + enemydamage +" points of damage!")
            defs.pause()

        if battlemenuattack == x:
            break
    while battlemenu == "2":
        defs.cls()
        for item in storage.backpack:
            print(item, '    ', storage.backpack[item][number])
        itemchoice = input("Which item?: ")
        for item in storage.backpack:
            if itemchoice == item:
    if battlemenu == 3 and runbol == True and randint(1, 10) < fleepercent:
        defs.cls()
        type("You fled from the battle!")
        defs.pause()
        break
    else:
        defs.cls()
        type("Couldn't get away!")
        defs.pause()
