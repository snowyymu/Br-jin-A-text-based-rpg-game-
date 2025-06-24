import os
from random import randint
from time import sleep
import functions
import map
inventory = []
charactername, buildselected = functions.charcreation()
buildname = functions.setplayer(buildselected)
sleep(0.3)
print("---------------------------------")
currentareaname = "Abandoned Village"
currentlocation = "Abandoned Village"
currentarea = "Area1"
type = ""
print("Your destiny has crossed this harsh land, where death is the best outcome of any poor soul who set foot upon it.")
print("You will come to realize this the more you traverse these lands, i, Rugdnar, will watch upon your every moves, like a guardian angel.")
print("---------------------------------")
sleep(0.4)
while True:
    sleep(0.5)
    locationdetails = map.getlocationdetails(currentlocation)
    print(f"[{currentlocation}]")
    print(f"{locationdetails['Description']}")
    nextlocation = map.updatelocation(currentarea, currentlocation)
    if nextlocation == "-1":
        bossdetails = map.getboss(currentarea)
        print("Each step you take, the more death you smell...")
        sleep(0.3)
        print(f"In front of you, stands [{bossdetails['Name']}]")
        sleep(0.2)
        print(bossdetails['Description'])
        sleep(0.4)
        type = "FINAL"
        functions.setenemy(type)
        print("GET.")
        sleep(0.3)
        print("READY.")
        sleep(0.5)
        functions.attacksequence(bossdetails['Name'], type)
        currentstat = functions.getstat()
        if currentstat[0] == 0:
            print("RESTART.")
        else:
            print("END of area reached.")
        break
    print("Your options:")
    print(f"1. Go to {nextlocation} ")
    print("2. Open Inventory")
    if locationdetails['Items'] != "":
        print(f"3. See nearby items")
    desc = input(">> ")
    print("---------------------------------")
    sleep(0.4)
    if desc == "1":
        enemychance = randint(0,2)
        if enemychance == 1 or enemychance == 2:
            print("You encountered an enemy!!!")
            enemydetails = functions.encounter()
            if enemydetails[1] == "B":
                print("You encountered a {BOSS}")
                print(f"{enemydetails[0]} presents before you")
            else:
                print(f"You find a {enemydetails[0]}")
            print("Entering fight, get ready!!")
            functions.setenemy(enemydetails[1])
            functions.attacksequence(enemydetails[0], type)
            currentstat = functions.getstat()
            if currentstat[0] == 0:
                print("You have to restart!")
                break
        currentlocation = map.updatelocation(currentarea,currentlocation)
    elif desc == "3":
        print(f"Current nearby items : {locationdetails['Items']}")
        sleep(0.3)
        print("1. Pick up items")
        desc = input(">> ")
        if desc == "1":
            for item in locationdetails['Items']:
                if item not in inventory:
                    inventory.append(item)
                else:
                    print("{Already picked up items in this area}")
            sleep(0.5)
    elif desc == "2":
        if inventory == []:
            print("{Inventory is empty}")
        else:
            print("Current items in inventory")
            print(inventory)
        print("---------------------------------")
        sleep(0.4)

print("////////////////////////////////////////////")
input("Press any key to continue {STILL UPDATING}")