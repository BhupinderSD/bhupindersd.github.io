#Bhupinder Dhoofer

import sqlite3
import pandas
print("""
 ______ _______    ______        _ _     _ _                _______          _  _ _
(_____ (_______)  (____  \      (_) |   | (_)              (_______)        | || |   (_) _
 _____) )          ____)  )_   _ _| | __| |_ ____   ____       _  ___   ___ | || |  _ _ _| |_
|  ____/ |        |  __  (| | | | | |/ _  | |  _ \ / _  |     | |/ _ \ / _ \| || |_/ ) (_   _)
| |    | |_____   | |__)  ) |_| | | ( (_| | | | | ( (_| |     | | |_| | |_| | ||  _ (| | | |_
|_|     \______)  |______/|____/|_|\_)____|_|_| |_|\___ |     |_|\___/ \___/ \_)_| \_)_|  \__)
                                                  (_____|                                     """)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def Mode():
    global UserName, ModeInput
    UserName = input("What is your name (Will be used as the file name)? \n")
    while True:
        try:
            ModeInput = int(input("""\nWould you like to use:
    1. Basic Mode
    2. Advanced Mode
    3. More information
"""))
            if ModeInput == 3:
                print("In Basic mode, compatibility checks will be enabled throughout the program, meaning that the components that you select will work with each other. Advanced mode is only for professionals as they will not have any compatibility checks.")
            elif ModeInput == 1 or ModeInput == 2:
                break
            else:
                print("***Please enter a valid number***\n")
        except ValueError:
            print("***Please enter the number***\n")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def ComponentSelection():
    global ComponentInput
    while True:
        try:
            ComponentInput = int(input("""\nWhat component would you like to select?
    1. CPU
    2. Motherboard
    3. Memory
    4. Storage
    5. Video Card
    6. Power Supply
    7. Case
"""))
            if ComponentInput <1 or ComponentInput >7:
                print("***Please enter a valid number***")
            else:
                break
        except ValueError:
            print("***Please enter the number***\n")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def ItemSelection():
    global ComponentList
    while True:
        ComponentSelection()

        Database = sqlite3.connect("Components2.db")
        cursor = Database.cursor()
        ComponentList = ["CPU","Motherboard","Memory","Storage","VideoCard","PowerSupply","Tower"]

        print("\n", pandas.read_sql_query("SELECT * FROM {}".format(ComponentList[ComponentInput-1]), Database, "id"))

        while True:
            ItemChoice = input("\nWhat item would you like? \n")
            cursor.execute('''SELECT id FROM '''+ ComponentList[int(ComponentInput)-1] + ''' WHERE id = ''' + ItemChoice)
            Check = cursor.fetchall()
            print("----------------------------------------------------------------------------------------------------")
            if Check == []:
                print("***Please enter a valid id***")
            else:
                #BasicMode()
                ComponentChoice [ComponentInput-1] = ItemChoice
                break

        AnotherComponent = int(input("""\nDo you want to select another component?
        1. Yes
        2. No
"""))
        if AnotherComponent == 1:
            pass
        elif AnotherComponent == 2:
            break
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def UserComponents():
    global UserName

    Database = sqlite3.connect("Components2.db")
    cursor = Database.cursor()
    cursor.execute

    loops = 0
    UserChoices = [["CPU",""],
                   ["Motherboard",""],
                   ["Memory",""],
                   ["Storage",""],
                   ["Video Card",""],
                   ["Power Supply",""],
                   ["Case",""]
                   ]

    for position in ComponentChoice:
        while loops <= 7:
            try:
                cursor.execute('SELECT Name FROM ' + ComponentList[loops-1] + ' WHERE id = {}'.format(ComponentChoice[loops-1]))
                for row in cursor:
                    ItemText = row[0]
            except sqlite3.OperationalError:
                ItemText = 0
            UserChoices[loops-1][1] = ItemText
            loops = loops + 1
    
    db = sqlite3.connect("Customers.db")
    cursor = db.cursor()
    while True:
        try:
            cursor.execute("""CREATE TABLE {}(id INTEGER PRIMARY KEY, Component TEXT, Name TEXT)""".format(UserName))
            break
        except sqlite3.OperationalError:
            UserName = input("A file with this name may already exists or this may contain special characters. Please enter another name.\n")
    cursor.executemany("""INSERT INTO """+UserName+""" Values (NULL,?,?)""",UserChoices)
    Database.commit()
    db.commit()
    cursor.execute('''SELECT * FROM ''' +UserName)
##    for row in cursor:
##        print(row)                                              #method 1
    print("Saved")
    print(pandas.read_sql_query("SELECT * FROM "+UserName, db, "id")) #method 2
    Database.close()
    db.close()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def BasicMode():

    Database = sqlite3.connect("Components2.db")
    cursor = Database.cursor()
    while True:
        while True:
            #socket compatiblity
            if ComponentChoice[0] and ComponentChoice[1] != "":
                print("Checking socket compatibilty.")
                CPUCheck = cursor.execute('''SELECT Socket FROM CPU WHERE id = ''' + ComponentChoice[0]).fetchall()
                MotherboardCheck = cursor.execute('''SELECT Socket FROM Motherboard WHERE id = ''' + ComponentChoice[1]).fetchall()
                if CPUCheck == MotherboardCheck:
                    print("Socket is Compatible.")
                    break
                else:
                    print("The socket is not compatible. Please choose another CPU or Motherboard.")
                    ItemSelection()
            else:
                print("Socket Compatibility check not required.")
                break
        while True:
            #FormFactor compatibility
            if ComponentChoice[1] and ComponentChoice[5] != "":
                print("Checking form factor compatibilty.")
                MotherboardCheck = cursor.execute('''SELECT FormFactor FROM Motherboard WHERE id = ''' + ComponentChoice[1]).fetchall()
                PowerSupplyCheck = cursor.execute('''SELECT FormFactor FROM PowerSupply WHERE id = ''' + ComponentChoice[5]).fetchall()
                if MotherboardCheck == PowerSupplyCheck:
                    print("Form Factor is Compatible-1")
                    break
                else:
                    print("The Form Factor is not compatible. Please choose another Power Supply or Motherboard.")
                    ItemSelection()
            else:
                print("Form Factor Compatibility check not required-1")
                break
        while True:
            if ComponentChoice[5] and ComponentChoice[6]!= "":
                print("Checking form factor compatibilty.")
                PowerSupplyCheck = cursor.execute('''SELECT FormFactor FROM PowerSupply WHERE id = ''' + ComponentChoice[5]).fetchall()
                TowerCheck = cursor.execute('''SELECT FormFactor FROM Tower WHERE id = ''' + ComponentChoice[6]).fetchall()
                if PowerSupplyCheck == TowerCheck:
                    print("Form Factor is Compatible-2")
                    break
                else:
                    print("The Form Factor is not compatible. Please choose another Power Supply or Case.")
                    ItemSelection()
            else:
                print("Form Factor Compatibility check not required-2")
                break
        while True:
            if ComponentChoice[1] and ComponentChoice[6]!= "":
                print("Checking form factor compatibilty.")
                MotherboardCheck = cursor.execute('''SELECT FormFactor FROM Motherboard WHERE id = ''' + ComponentChoice[1]).fetchall()
                TowerCheck = cursor.execute('''SELECT FormFactor FROM Tower WHERE id = ''' + ComponentChoice[6]).fetchall()
                if MotherboardCheck == TowerCheck:
                    print("Form Factor is Compatible-3")
                    break
                else:
                    print("The Form Factor is not compatible. Please choose another Case or Motherboard.")
                    ItemSelection()
            else:
                print("Form Factor Compatibility check not required-3")
                break
        break
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
ComponentChoice = ["","","","","","",""]
Mode()
ItemSelection()
if ModeInput == 1:
    BasicMode()
UserComponents()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

