import defs
import time
import sound
import textyoptions
import math
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
        if i == 4:
            sound.textbeep()
            if i == 4:
                i = 0
        time.sleep(textyoptions.numberspeed)
    print("'")
    print("\n")


defs.cls()
talk("???", "It's a pleasure, " + defs.name + ". Name's Flay.")
defs.pause()
talk("Flay", "Seems like you were in quite a fight, huh, bruises all over you.")
defs.pause()
talk("Flay", "I, along with my goblin friend here, Gaam, found you lying nearby \nnext to some age-old oaks.")
defs.pause()
talk("Gaam", "That's me.")
defs.pause()
talk("Flay", "You've been asleep ever since.")
defs.pause()
talk("Flay", "I did what I could to the bruised skin, bandaged it and we, \nwith that I mean 'I', dragged you all the way back to our cottage.")
defs.pause()
talk("Gaam", "Ye, the bedhead seems suspicious.")
defs.pause()
talk("Flay", "You souldn't speak that way to our guest.")
defs.pause()
talk("Gaam", "Whatever, elf.")
defs.pause()
talk("Flay", "Feel free to stay as long you want, company has been sparse\n lately.")
defs.pause()
talk("Flay", "Although...")
defs.pause()
talk("Flay", "...now that you're awake, you should come with me to the yard. Seems \nlike you could do with some combat training, considering your \nsituation.")
defs.pause()
talk("Flay", "Having you run around not being able to protect yourself can't be good.")
defs.pause()
talk("Flay", "After that, you're free to go wherever you want.")
defs.pause()
talk("Flay", "Gaam, why don't you head on outside and prepare the trainee rag?")
defs.pause()
talk("Gaam", "Ye, ye. I'm going.")
defs.pause()
talk("Flay", "Don't mind Gaam, he's rather stubborn at times.")
defs.pause()
talk("Flay", "Just leave him be for a while and it will pass.")
defs.pause()
talk("Flay", "I prepared this bag of supplies while you were asleep, if you were to \nleave as soon as you woke up.")
defs.loot('Milk', 2)
defs.loot('Bread', 2)
defs.loot('Whetstone', 1)
defs.loot('Gold', 100)
talk("Flay", "I found that wetstone out in the woods about the same time we found you.")
defs.pause()
talk("Flay", "It will allow you to sharpen any weapon you happen to find.")
defs.pause()
talk("Flay", "Now, let us head outside. I'm sure Gaam already has finished setting up the dummy.")
defs.pause()
defs.dotdotdot()
type("You exit the cottage, into an area contained within a frail fence.")
time.sleep(1)
type("To the east, a thick, old forest, presumably where you came from.")
time.sleep(1)
type("To the North, a giant hill obscures your vision of anything beyond it.")
time.sleep(1)
type("To the west and south, plains of yellow grass cover the area like a thin \nbedcover.")
time.sleep(1)
type("By the frail fence, a worn sack of hay impaled upon a pole represents a \ntraining dummy.")
time.sleep(1)
type("Gaam rests next to the dummy. He turns and stares at you with a grimacing face.")
defs.pause()
talk("Fray", "In addition to the supplies, I allow you to pick one of these weapons \nto accompany you from this point on.")
type("Fray points towards a weaponrack, situated right besides the exit.")
defs.pause()
talk("Fray", "Of course, should you change your mind you can always get your hands on \nweapons just like these from elsewhere.")
defs.pause()
while(defs.weaponswag == "4"):
    print("Pick one of the following weapons:")
    print("1. Rugged Sword")
    print("2. Rugged Bow")
    print("3. Rugged Staff")
    weaponswag = input(defs.ans)
    if(weaponswag != "1" or "2" or "3"):
        weaponswag = ""
    if weaponswag == "1":
        talk("Flay", "A sword huh? Works great against light armor, at close range.")
        weaponbol = input("Confirm(yes/no)?: ")
        if weaponbol == "yes":
            storage.gear['ruggedsword'] = 10
            equip('ruggedsword', 'mainhand')
            defs.addatk('Slash', 20, 'empty')
            defs.addatkall('Slash', 20, 'empty')
    if weaponswag == "2":
        talk("Flay", "A bow, huh? Works great against most armor from a distance, doesn't work all that \nwell with clubsy heavy armour though...")
        weaponbol = input("Confirm(yes/no)?: ")
        if weaponbol == "yes":
           storage.gear['ruggedbow'] = 15
           equip('ruggedbow', 'mainhand')
           defs.addatk('Arrow Shot', 30, 'empty')
           defs.addatkall('Arrow Shot', 30, 'empty')
    if weaponswag == "3":
        talk("Flay", "A staff, huh? Works great against all kinds of armour from a distance, heavier \narmour with strong enchantments are hard to come by though.")
        weaponbol = input("Confirm(yes/no)?: ")
        if weaponbol == "yes":
            storage.gear['ruggedstaff'] = 25
            equip('ruggedstaff', 'mainhand')
            addspatk('Firebolt', 50, 'empty')
            addspatkall('Firebolt', 50, 'empty')

defs.cls()
talk("Flay", "Great!")
defs.pause()
talk("Flay", "Now, face off aginst that dummy over there.")
defs.pause()
talk("Flay", "Do you need me to go over the basic principles of fighting, or can \nyou handle yourself?")
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
    type("Once battle is engaged, a menu will popup. Within this menu, you will be able to attack the enemy with a variety of attacks  \ndepending on your weapon and your skills. Your attack value will be pitted against the enemy's, and the outcome depends on each of your stats. 'Normal Attacks' are attacks using your normal weapon and will be judged by your strength and agillity stat. 'Special Attacks' are attacks using mana and therefore depend on your intellect and agility stat.")
    type("In addition to that, you'll be able to activate items from your inventory by selecting 'Inventory' from the battle menu. Various items to various things and it is often stated in the item description what it actually does.")
    type("Finally, you have the option to escape from battle, should the need occur. Different battles give you different odds of escaping while some are simply put impossible to flee from. Do this by selecting 'Run' in the battle menu.")
if trainbol == "2":
    talk("Flay", "Suit yourself!")
    defs.pause()


#BATTLE PART THINGY DO THIS AND THAT I GET THE DRILL
