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
while(weaponswag == ""):
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
defs.cls()
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

defs.cls()
type("What?")
defs.dotdotdot()
type("Training-Dummy appeared!")
defs.pause()
defs.cls()
while defs.battlemenu = 0:
    print("Chose your action!")
    print("1. Attack")
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
            print("")
        while battlemenuattack == 2:                       #SPECIAL ATTACK
            defs.cls()
            print("")           
    while battlemenu == "2":
        defs.cls()
        for item in storage.backpack:
            print(item, '    ', storage.backpack[item][number])
        itemchoice = input("Which item?: ")
        for item in storage.backpack:
            if itemchoice == item:
                

