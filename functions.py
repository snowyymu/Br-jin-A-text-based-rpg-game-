import random
import time

abandonedvillage = ["Main gate", ""]


bosslist = ["Rogar The Wretched",
            "Merwin, Daughter of Brehmir",
            "Brehmir The Immortal",
            "Mathilda the accursed",
            "Verkthervrimth"
                   ]
enemylist = ["Verides",
             "Foot soldier",
             "Metrisians",
             "Mutated Civilian",
             "Wretched Beast"
             ]


def getstat():
    return health, shield


def attacksequence(enemyname, type):
    round = 1
    check = False
    playerturn = True
    rng = 0
    while True:
        print("----------------------------------------------------------------")
        print(f"Round : {round}")
        print(f"Current player stats [HP: {health}, Shield: {shield}]")
        print(f"Current enemy stats [HP: {enemyhealth}, Shield: {enemyshield}]")
        if enemyhealth == 0:
            print("You defeated the enemy")
            print("----------------------------------------------------------------")
            time.sleep(0.5)
            break
        elif health == 0:
            print("You died")
            print("----------------------------------------------------------------")
            time.sleep(0.5)
            break
        if playerturn is True:
            time.sleep(0.3)
            if check == False:
                round = round + 1
            print("----------------------------------------------------------------")
            while True:
                print("Your turn")
                print("1. Attack")
                print("2. Escape")
                desc = int(input(">> "))
                if desc != 1 and desc != 2:
                    print("----------------------------------------------------------------")
                    print("Wrong input, Type either 1 or 2")
                    print("----------------------------------------------------------------")
                else:
                    break
            time.sleep(0.2)
            if desc == 2:
                if type == "FINAL":
                    print("{YOU CANNOT ESCAPE THE BOSS FIGHT}")
                    check = True
                else:
                    rng = random.randint(0, 2)
                    if rng == 1 or rng == 2:
                        print("Failed to escape")
                        time.sleep(0.5)
                        print("You lost a turn")
                    elif rng == 0:
                        print("Sucessfully escaped")
                        print("---------------------------------------")
                        time.sleep(0.5)
                        break
            if desc == 1:
                check = False
                print("Attacking...")
                time.sleep(0.3)
                miss = random.randint(0,2)
                if miss == 0:
                    print("Your attacked missed!")
                    playerturn = False
                else:
                    totalattack = pattack
                    updateenemy(totalattack)
                    time.sleep(0.3)
                    print(f"You dealt {totalattack} damage to {enemyname}")
                    playerturn = False
        if rng == 1 or rng == 2 or playerturn is False:
            time.sleep(0.5)
            print("----------------------------------------------------------------")
            print(f"{enemyname} is about to attack")
            updateplayer(enemyattack)
            time.sleep(0.3)
            print(f"{enemyname} dealt {enemyattack} damage")
            playerturn = True


def encounter():
    rng = random.randint(0, 9)
    if rng == 0:
        rng = random.randint(0, len(bosslist)-1)
        enemy = bosslist[rng]
        type = "B"
    else:
        rng = random.randint(0, len(enemylist)-1)
        enemy = enemylist[rng]
        type = "E"
    return enemy, type


def setenemy(type):
    global enemyhealth, enemyshield, enemyattack
    if type == "FINAL":
        enemyhealth = 500
        enemyshield = 40
        enemyattack = 25
    elif type == "B":
        enemyhealth = 250
        enemyshield = 50
        enemyattack = 20
    elif type == "E":
        enemyhealth = round(random.randint(50,80),-1)
        enemyshield = round(random.randint(10,20),-1)
        enemyattack = round(random.randint(10,15),-1)


def setplayer(buildselected):
    global health, shield, pattack
    if buildselected == 1:
        health = 120
        shield = 40
        pattack = 15
        buildname = "Tank"
    elif buildselected == 2:
        health = 100
        shield = 50
        pattack = 25
        buildname = "All-Rounder"
    elif buildselected == 3:
        health = 90
        shield = 30
        pattack = 30
        buildname = "Strength"
    print(f"{buildname} stat : [HP: {health}, Shield: {shield}, Attack: {pattack}]")
    return buildname


def updateenemy(damage):
    global enemyshield, enemyhealth
    if enemyshield == 0:
        if damage >= enemyhealth:
            enemyhealth = 0
        else:
            enemyhealth = enemyhealth - damage
    else:
        if enemyshield >= damage:
            enemyshield = enemyshield - damage
        else:
            remaining = damage - enemyshield
            enemyshield = 0
            enemyhealth = enemyhealth - remaining


def updateplayer(damage):
    global shield, health
    if shield == 0:
        if damage >= health:
            health = 0
        else:
            health = health - damage
    else:
        if shield >= damage:
            shield = shield - damage
        else:
            remaining = damage - shield
            shield = 0
            health = health - remaining


def charcreation():
    print("-------Welcome to character creation-------")
    print("Enter your character name")
    charname = input(">> ")
    while True:
        print("Choose between the preset builds: ")
        print("1.Tank {HP Focused}")
        print("2.All-Rounder {Balanced Build}")
        print("3.Strength {Attack Focused}")
        buildselected = int(input(">> "))
        if buildselected != 1 and buildselected != 2 and buildselected != 3:
            print("Wrong input, Enter '1', '2', or '3'")
        else:
            break
    return charname,buildselected


