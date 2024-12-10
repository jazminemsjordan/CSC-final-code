import status_module 
# test comment

def check_commands(input):
    """Compares player input to a list of possible gameplay commands.
    If command is valid, runs function command; else, it returns “invalid input” string and prompts the user to enter something else"""
    split = input.split(maxsplit=1)
    command = split[0]
    if len(split) > 1:
        qualifier = split[1]
    else:
        qualifier == ""
    if command == "go":
        if qualifier == "":
            direction = input("Where would you like to go? ")
            return go(direction)
        else:
            return go(qualifier)
    if command == "look" or command == "l":
        return look()
    if command == "examine" or command == "x":
        if qualifier == "":
            object = input("What would you like to examine? ")
            return examine(object)
        else:
            return examine(qualifier)
    if command == "use":
        if qualifier == "":
            item = input("What would you like to use? ")
            subject = input("On what will you use it on? ")
            return use(item, subject)
        else:
            subject = input("Use on what? ")
            return use(qualifier, subject)
    if command == "inventory" or command == "i":
        return status_module.inventory 
    if command == "help" or command == "?":
        return status_module.instructions()
    else:
        return "Failed: not a valid command."

def get_input():
    while True:
        input = input("Enter your command: ")
        result = check_commands(input)
        print(result)
        

def go(direction):
    """ Player input a string of direction to move (north, south, west, east).
    If the input is valid (available direction - path is available, not locked), move the player in the input direction; 
    else, returns “unavailable direction” string and prompts user to enter a different direction.
    """
    if direction != "north" and direction != "east" and direction != "south" and direction != "west" and direction != "n" and direction != "e" and direction != "s" and direction != "w":
        return "Failed: not a cardinal direction."
    if status_module.location == "vestibule":
        if direction == "north" or direction == "n":
            status_module.location = "atrium"
            return "Success!"
        if direction == "south":
            if status_module.locked["exit"] == True:
                return "Failed: the exit is locked."
            else: 
                status_module.win == True
                return "You made it out!"
        else:
            return "Failed: you can't go that way."
    
    # Checking player's location and give available direction for each location
    # If direction is valid, update location
    if status_module.location == "atrium":
        if direction == "north" or direction == "n":
            status_module.location = "classroom_1"
            return "Success!"
        if direction == "east" or direction == "e":
            if status_module.locked["classroom_2"] == True:
                return "Failed: this door is locked."
            else: 
                status_module.location = "classroom_2"
                return "Success!"
        if direction == "south" or direction == "s":
            status_module.location = "vestibule"
            return "Success!"
        if direction == "west" or direction == "w":
            status_module.location = "library"
            return "Success!"
    if status_module.location == "classroom_1":
        if direction == "east" or direction == "e":
            if status_module.locked["supply_closet"] == True:
                return "Failed: this door is locked."
            else:
                status_module.location = "supply_closet"
                return "Sucess!"
        if direction == "south" or direction == "s":
            status_module.location = "atrium"
            return "Success!"
        else: 
            return "Failed: you can't go that way."
    if status_module.location == "supply_closet":
        if direction == "west" or direction == "w":
            status_module.location == "classroom_1"
            return "Success!"
        else:
            return "Failed: you can't go that way."
    if status_module.location == "classroom_2":
        if direction == "west" or direction == "w":
            status_module.location == "atrium"
            return "Success!"
        else:
           return "Failed: you can't go that way."
    if status_module.location == "library":
        if direction == "north" or direction == "n":
            if status_module.locked["classroom_3"] == True:
                return "Failed: door is locked."
            else:
                status_module.location = "classroom_3"
                return "Success!"
        if direction == "east" or direction == "e":
            if status_module.locked["dean_office"] == True:
                return "Failed: door is locked."
            else:
                status_module.location = "dean_office"
                return "Success!"
        if direction == "south" or direction == "s":
            status_module.location = "balcony"
            return "Success!"
        if direction == "west" or direction == "w":
            status_module.location = "atrium"
            return "Success!"
    if status_module.location == "classroom_3":
        if direction == "south" or direction == "s":
            status_module.location = "library"
            return "Success!"
        else:
            return "Failed: you can't go that way."
    if status_module.location == "dean_office":
        if direction == "west" or direction == "w":
            status_module.location = "library"
            return "Success!"
        else:
            return "Failed: you can't go that way."
    if status_module.location == "balcony":
        if direction == "north" or direction == "n":
            status_module.location = "library"
            return "Success!"
        else:
            return "Failed: you can't go that way."

def look():
    """ Provide a description of the player's current location (based on the location variable from go(direction)), including exits, interactable objects
    """
    if status_module.location == "vestibule":
        return status_module.vestibule_flavor
    if status_module.location == "atrium":
        return status_module.atrium_flavor
    if status_module.location == "classroom_1":
        return status_module.classroom_1_flavor
    if status_module.location == "supply_closet":
        return status_module.supply_closet_flavor
    if status_module.location == "classroom_2":
        return status_module.classroom_2_flavor
    if status_module.location == "library":
        return status_module.library_flavor
    if status_module.location == "classroom_3":
        return status_module.classroom_3_flavor
    if status_module.location == "dean_office":
        return status_module.dean_office_flavor
    if status_module.location == "balcony":
        return status_module.balcony_flavor
    
def clarify(subject):
    '''clarifying multiple confusing inputs for commands'''
    if subject == "key":
        while True:
            check = input(f"There are lots of keys. Which do you mean? \n Options: shiny key, gold key, drawer key, old key, rusty key, keycard.")
            if check == "shiny" or "shiny key":
                return "shiny key"
                break
            elif check == "gold" or "gold door":
                return "gold key"
                break
            elif check == "drawer" or "drawer key":
                return "drawer key"
                break
            elif check == "old" or "old key":
                return "old key"
                break
            elif check == "rusty" or "rusty key":
                return "rusty key"
                break
            elif check == "keycard" or "card":
                return "keycard"
                break
            else:
                return "Not a valid answer: please choose a key."
    if subject == "door":
        while True:
            check = input(f"You see more than one door in the library. \nWhich do you mean—the shiny door to the third classroom, or the golden door to the dean's office?")
            if check == "shiny" or "shiny door":
                return "shiny door"
                break
            elif check == "gold" or "gold door":
                return "gold door"
                break
            else:
                return "Not a valid answer: please choose a door."

def examine(subject):
    """ Player input a string of a subject to examine. 
    If the input is valid (subject is available in location), let player interact with each object (open, close, display item available, etc).
    """
    if status_module.location == "atrium":
        if subject == "old door" or subject == "door":
            return status_module.old_door_flavor
        if subject == "indoor plants" or subject == "plants":
            return status_module.indoor_plants_flavor
        if subject == "central staircase" or subject == "stairs" or subject == "staircase":
            return status_module.central_staircase_flavor
    elif status_module.location == "vestibule":
        if subject == "keycard door" or subject == "door":
            return status_module.keycard_door_flavor
        if subject == "touchscreen directory" or subject == "touchscreen":
            return status_module.touchscreen_directory_flavor
        if subject == "coat hooks" or subject == "hooks":
            return status_module.coat_hooks_flavor
    elif status_module.location == "classroom_1": 
        if subject == "smartboard" or subject == "board":
            return status_module.smartboard_flavor
        if subject == "lab stools" or subject == "stools":
            return status_module.lab_stools_flavor
        if subject == "supply drawers" or subject == "drawers":
            status_module.inventory.append("rusty key")
            return status_module.supply_drawers_flavor
        if subject == "rusty door":
            return status_module.rusty_door_flavor  
    elif status_module.location == "supply_closet":
        if subject == "equipment shelves" or subject == "shelves":
            status_module.inventory.append("old key")
            return status_module.equipment_shelves_flavor
        if subject == "PPE cabinet" or subject == "PPE" or subject == "cabinet":
            return status_module.ppe_cabinet_flavor
    elif status_module.location == "classroom_2":
        if subject == "lab benches" or subject == "benches":
            status_module.inventory.append("drawer key")
            return status_module.lab_benches_flavor
        if subject == "safety cabinet" or subject == "cabinet":
            return status_module.safety_cabinet_flavor
        if subject == "wall-mounted monitor" or subject == "monitor":
            return status_module.wall_mounted_monitor_flavor
    elif status_module.location == "library":
        if subject == "mahogany bookcase" or subject == "bookcase":
            return status_module.mahogany_bookcase_flavor
        if subject == "librarian's desk" or subject == "desk":
            return status_module.librarian_desk_flavor
        if subject == "study table" or subject == "table":
            return status_module.study_table_flavor
        if subject == "gold door":
            return status_module.gold_door_flavor
        if subject == "shiny door":
            return status_module.shiny_door_flavor
        if subject == "door":
            clarify(subject)
    elif status_module.location == "balcony":
        if subject == "glass railing" or subject == "railing":
            return status_module.glass_railing_flavor
        if subject == "potted plants" or subject == "plants":
            return status_module.potted_plants_flavor
    elif status_module.location == "classroom_3":
        if "print" in subject:            
            status_module.inventory.append("gold key")
            return status_module.printer_flavor
        if "outlet" in subject:
            return status_module.power_outlets_flavor
        if "kit" in subject:
            return status_module.robotics_kits_flavor
    elif status_module.location == "dean_office":
        if subject == "ergonomic desk" or subject == "desk":
            return status_module.ergonomic_desk_flavor
        if subject == "bookshelf with scientific journals" or subject == "bookshelf" or subject == "shelf":
            return status_module.bookshelf_flavor
        if subject == "Smith College crest plaque" or subject == "plaque" or subject == "crest":
            status_module.inventory.append("keycard")
            return status_module.crest_plaque_flavor
    else:
        return "You can't find that object right now."


def use(item, subject):
    """ Player input a string of the name of item want to use and a string of the name of the targetted subject.
    If the input is valid (item available in inventory and the target is an interactable object at location), modify game state based on item effect 
    (eg. unlock door → new available direction for move).
    Remove item from inventory after use and show the available items in the inventory.
    """
    if item == "key":
        item = clarify(item)
    if subject == "door" and status_module.location == "library":
        subject = clarify(subject)
    # Check if the target in an interactable object at location
    if item in status_module.inventory:
        if status_module.location == "atrium" and item == "old key" and subject == "old door":
            status_module.locked["classroom_2"] == False
            status_module.inventory.remove("old key") 
            return "You unlocked the door! You can now enter Classroom 2."
        elif status_module.location == "classroom_1" and item == "rusty key" and subject == "rusty door":
            status_module.locked["supply_closet"] == False
            status_module.inventory.remove("rusty key")
            return "You unlocked the door! You can now enter the supply closet."
        elif status_module.location == "library" and item == "drawer key" and subject == "librarian's desk":
            status_module.locked["librarian's desk"] == False
            status_module.inventory.remove("drawer key")
            status_module.inventory.append("shiny key")
            return "You unlocked the drawer of the librarian's desk! You found: shiny key."
        elif status_module.location == "library" and item == "gold key" and subject == "gold door":
            status_module.locked["dean_office"] == False
            status_module.inventory.remove("gold key")
            return "You unlocked the door! You can now enter the dean's office."
        elif status_module.location == "library" and item == "shiny key" and subject == "shiny door":
            status_module.locked["classroom_3"] == False
            status_module.inventory.remove("shiny key")
            return "You unlocked the door! You can now enter Classroom 3."
        elif status_module.location == "vestibule" and item == "keycard" and subject == "keycard door":
            status_module.locked["exit"] == False
            status_module.inventory.remove("keycard")
            return "You unlocked the exit door! Now you can get out of here!"
    else:
        return "Failed: you don't have that."
    
def save_game():
    ''' writes project file with status module: inventory, location, etc.)'''

def load_game():
    '''reads file data and loads variables from past game'''
