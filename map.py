map = {'Area1': {"Abandoned Village" : "Main Gate","Main Gate": "Ramshackled House"
    , "Ramshackled House": "Old BlackSmith", "Old BlackSmith": "Village Hall", "Village Hall": "END"}


       }


story = {'Abandoned Village': {"Description": "This village was once a powerhouse of Grovenheart district, but due to 'natural' disasters and 'unluckiness', this village is now like a graveyard ",
                                "Items": ""},
         'Main Gate': {"Description" : "Once used to be a sign of great prosperity of the village, now it can barely be called a Gate",
                        "Items": ["Guard's Rapier"]},
         'Ramshackled House': {"Description": "Looks like the house of a once very lavish family",
                                "Items": ["Worn out doll", "Rusted key"]},
         'Old BlackSmith' : {"Description": "Plenty of equipments lay on the ground, damaged and rusted. Signs of a once very prosperous blacksmith"
                             , "Items": ["Anvil"]},
         'Village Hall' : {"Description": "Blood everywhere,something sinister lies ahead...",
                           "Items" : ["BOSSROOM"]}



         }

mainbosses = {'Area1': {"Name" : "Kokata Sen, The Unlegitimate Shogun" ,
                        "Description" : "The one who seeks redemption, banished from the councils of the 5 Daimyos"}



              }


def getboss(currentarea):
    bossdetails = mainbosses[currentarea]
    return bossdetails


def getlocationdetails(currentlocation):
    locationdetails = story[currentlocation]
    return locationdetails


def updatelocation(currentarea, currentlocation):
    nextlocation = map[currentarea][currentlocation]
    if nextlocation == "END":
        print("{FINAL BOSS OF AREA REACHED}")
        print("-------------------------------------------------")
        nextlocation = "-1"
    return nextlocation





