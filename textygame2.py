import defs
import time
import sound
import textyoptions
i = 0

def type(str):
    for letter in str:
        print(letter, end='', flush=True)
        global i
        i += 1
        if i == 3:
            sound.textbeep()
            if i == 3:
                i = 0
        time.sleep(textyoptions.numberspeed)
    print("\n")
def talk(name, str):
    print(name + ": '", end="")
    for letter in str:
        print(letter, end='', flush=True)
        global i
        i += 1
        if i == 3:
            sound.textbeep()
            if i == 3:
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
defs.loot('milk', 2)
defs.loot('bread', 2)
defs.loot('whetstone', 1)
defs.loot('gold', 100)
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
while(defs.weaponswag == ""):
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
    if weaponswag == "2":
        talk("Flay", "A bow, huh? Works great against most armor from a distance, doesn't work all that \nwell with clubsy heavy armour though...")
        weaponbol = input("Confirm(yes/no)?: ")
        if weaponbol == "yes":
           storage.gear['ruggedbow'] = 15
           equip('ruggedbow', 'mainhand')
    if weaponswag == "3":
        talk("Flay", "A staff, huh? Works great against all kinds of armour from a distance, heavier \narmour with strong enchantments are hard to come by though.")
        weaponbol = input("Confirm(yes/no)?: ")
        if weaponbol == "yes":
            storage.gear['ruggedstaff'] = 25
            equip('ruggedstaff', 'mainhand')

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
attackpower = storage.equip['mainhand'] + defs.baseattack
defencepower = defs.armour + defs.basedefence
enemyhp = enemymaxhp
type("What?")
defs.dotdotdot()
type(enemyname + " appeared!")
defs.pause()
talk(enemyname, enemybattleroar)
defs.pause()
battle = True
while True:
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
            type(enemyname + " took " + damage + "points of damage!")
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
            type("You took " + enemydamage + " points of damage!")
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
            type(name + " used " + attackchoice + "!")
            defs.pause()
            attackpower = storage.attacklist[attackchoice] * randint(0.80, 1.20)
            damage = ((attackpower / enemydefencepower) * (storage.stats['agillity'] / 200) * (storage.stats['intellect']) * attackpower) + 50
            if randint(1.00, 2.00) <= storage.stats['critchance']:
                damage = damage * randint(1.25, 1.50)
            enemyhp = enemyhp - damage
            type("...")
            defs.pause()
            type(enemyname + " took " + damage + " points of damage!")
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
                print("Under construction")                                  #FIX THIS SHIT
    if battlemenu == 3 and runbol == True and randint(1, 10) < fleepercent:
        defs.cls()
        type("You fled from the battle!")
        defs.pause()
        break
    else:
        defs.cls()
        type("Couldn't get away!")
        defs.pause()
