import status_module 
# test comment

def check_commands(user_input):
    """Compares player input to a list of possible gameplay commands.
    If command is valid, runs function command; else, it returns “invalid input” string and prompts the user to enter something else"""
    split = user_input.split(maxsplit=1)
    command = split[0]
    if len(split) > 1:
        qualifier = split[1]
    else:
        qualifier = ""
    if command == "go":
        if qualifier == "":
            u_direction = input("Where would you like to go? ")
            return go(u_direction)
        else:
            return go(qualifier)
    if command == "look" or command == "l":
        return look()
    if command == "examine" or command == "x":
        if qualifier == "":
            u_object = input("What would you like to examine? ")
            return examine(u_object)
        else:
            return examine(qualifier)
    if command == "use":
        if qualifier == "":
            u_item = input("What would you like to use? ")
            u_subject = input("On what will you use it on? ")
            return use(u_item, u_subject)
        else:
            u_subject = input("Use on what? ")
            return use(qualifier, u_subject)
    if command == "inventory" or command == "i":
        return status_module.inventory 
    if command == "help" or command == "?":
        return status_module.instructions()
    else:
        return "Failed: not a valid command."

def get_input():
    while True:
        user_input = input("Enter your command: ")
        result = check_commands(user_input)
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
    
def clarify(thing):
    '''clarifying multiple confusing inputs for commands'''
    if thing == "key":
        check = input("There are lots of keys. Which do you mean? Options: shiny key, gold key, drawer key, old key, rusty key, keycard: ")
        if check == "shiny" or check == "shiny key":
            return "shiny key"
        elif check == "gold" or check == "gold door":
            return "gold key"
        elif check == "drawer" or check == "drawer key":
            return "drawer key"
        elif check == "old" or check == "old key":
            return "old key"
        elif check == "rusty" or check == "rusty key":
            return "rusty key"
        elif check == "keycard" or check == "card":
            return "keycard"
        else:
            return "Failed."
    elif thing == "door":
        while True:
            check = input("You see more than one door in the library. \nWhich do you mean—the shiny door to the third classroom, or the golden door to the dean's office?")
            if check == "shiny" or check == "shiny door":
                return "shiny door"
            elif check == "gold" or check == "gold door":
                return "gold door"
            else:
                return "failed"
    else:
        return "Failed"

def examine(u_subject):
    """ Player input a string of a subject to examine. 
    If the input is valid (subject is available in location), let player interact with each object (open, close, display item available, etc).
    """
    if status_module.location == "atrium":
        if u_subject == "old door" or u_subject == "door":
            return status_module.old_door_flavor
        elif u_subject == "indoor plants" or u_subject == "plants":
            return status_module.indoor_plants_flavor
        elif u_subject == "central staircase" or u_subject == "stairs" or u_subject == "staircase":
            return status_module.central_staircase_flavor
        else:
            return "You can't find that object right now."
    elif status_module.location == "vestibule":
        if u_subject == "keycard door" or u_subject == "door":
            return status_module.keycard_door_flavor
        elif u_subject == "touchscreen directory" or u_subject == "touchscreen" or u_subject == "directory":
            return status_module.touchscreen_directory_flavor
        elif u_subject == "coat hooks" or u_subject == "hooks":
            return status_module.coat_hooks_flavor
        else:
            return "You can't find that object right now."
    elif status_module.location == "classroom_1": 
        if u_subject == "smartboard" or u_subject == "board":
            return status_module.smartboard_flavor
        elif u_subject == "lab stools" or u_subject == "stools":
            return status_module.lab_stools_flavor
        elif u_subject == "supply drawers" or u_subject == "drawers":
            status_module.inventory.append("rusty key")
            return status_module.supply_drawers_flavor
        elif u_subject == "rusty door":
            return status_module.rusty_door_flavor
        else:
            return "You can't find that object right now."  
    elif status_module.location == "supply_closet":
        if u_subject == "equipment shelves" or u_subject == "shelves":
            status_module.inventory.append("old key")
            return status_module.equipment_shelves_flavor
        elif u_subject == "PPE cabinet" or u_subject == "PPE" or u_subject == "cabinet":
            return status_module.ppe_cabinet_flavor
        else:
            return "You can't find that object right now."
    elif status_module.location == "classroom_2":
        if u_subject == "lab benches" or u_subject == "benches":
            status_module.inventory.append("drawer key")
            return status_module.lab_benches_flavor
        elif u_subject == "safety cabinet" or u_subject == "cabinet":
            return status_module.safety_cabinet_flavor
        elif u_subject == "wall-mounted monitor" or u_subject == "monitor":
            return status_module.wall_mounted_monitor_flavor
        else:
            return "You can't find that object right now."
    elif status_module.location == "library":
        if u_subject == "mahogany bookcase" or u_subject == "bookcase":
            return status_module.mahogany_bookcase_flavor
        elif u_subject == "librarian's desk" or u_subject == "desk":
            return status_module.librarian_desk_flavor
        elif u_subject == "study table" or u_subject == "table":
            return status_module.study_table_flavor
        elif u_subject == "gold door":
            return status_module.gold_door_flavor
        elif u_subject == "shiny door":
            return status_module.shiny_door_flavor
        elif u_subject == "door":
            clarify(u_subject)
        else:
            return "You can't find that object right now."
    elif status_module.location == "balcony":
        if u_subject == "glass railing" or u_subject == "railing":
            return status_module.glass_railing_flavor
        elif u_subject == "potted plants" or u_subject == "plants":
            return status_module.potted_plants_flavor
        else:
            return "You can't find that object right now."
    elif status_module.location == "classroom_3":
        if "print" in u_subject:            
            status_module.inventory.append("gold key")
            return status_module.printer_flavor
        elif "outlet" in u_subject:
            return status_module.power_outlets_flavor
        elif "kit" in u_subject:
            return status_module.robotics_kits_flavor
        else:
            return "You can't find that object right now."
    elif status_module.location == "dean_office":
        if u_subject == "ergonomic desk" or u_subject == "desk":
            return status_module.ergonomic_desk_flavor
        elif u_subject == "bookshelf with scientific journals" or u_subject == "bookshelf" or u_subject == "shelf":
            return status_module.bookshelf_flavor
        elif u_subject == "Smith College crest plaque" or u_subject == "plaque" or u_subject == "crest":
            status_module.inventory.append("keycard")
            return status_module.crest_plaque_flavor
        else:
            return "You can't find that object right now."

def use(u_item, u_target):
    """ Player input a string of the name of item want to use and a string of the name of the targetted subject.
    If the input is valid (item available in inventory and the target is an interactable object at location), modify game state based on item effect 
    (eg. unlock door → new available direction for move).
    Remove item from inventory after use and show the available items in the inventory.
    """
    if u_item == "key":
        item = clarify(u_item)
    else:
        item = u_item
    subject = ""
    if u_target == "door" and status_module.location == "library":
        subject = clarify(u_target)
    else:
        subject = u_target
    # Check if the target in an interactable object at location
    if item in status_module.inventory:
        if status_module.location == "atrium" and item == "old key" and subject == "old door" or status_module.location == "atrium" and item == "old key" and subject == "door":
            status_module.locked["classroom_2"] == False
            status_module.inventory.remove("old key") 
            return "You unlocked the door! You can now enter Classroom 2."
        elif status_module.location == "classroom_1" and item == "rusty key" and subject == "rusty door" or status_module.location == "classroom_1" and item == "rusty key" and subject == "door":
            status_module.locked["supply_closet"] == False
            status_module.inventory.remove("rusty key")
            return "You unlocked the door! You can now enter the supply closet."
        elif status_module.location == "library" and item == "drawer key" and subject == "librarian's desk" or status_module.location == "library" and item == "drawer key" and subject == "desk":
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
        elif status_module.location == "vestibule" and item == "keycard" and subject == "keycard door" and status_module.location == "vestibule" and item == "keycard" and subject == "door":
            status_module.locked["exit"] == False
            status_module.inventory.remove("keycard")
            return "You unlocked the exit door! Now you can get out of here!"
    else:
        return "Failed: you don't have that."
    
def save_game():
    ''' writes project file with status module: inventory, location, etc.)'''

def load_game():
    '''reads file data and loads variables from past game'''
