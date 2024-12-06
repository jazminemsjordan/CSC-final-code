import status_module 
# test comment

def check_commands(command):
    """Compares player input to a list of possible gameplay commands.
    If command is valid, runs function command; else, it returns “invalid input” string and prompts the user to enter something else"""
    if command in status_module.command_list:
        if command == "go":
            direction = input("Where would you like to go?")
            return go(direction)
        if command == "look":
            return look()
        if command == "examine":
            object = input("What would you like to examine?")
            return examine(object)
        if command == "use":
            item = input("What would you like to use?")
            subject = input("On what will you use it on?")
            return use(item, subject)
        if command == "inventory":
            return status_module.inventory 

    else:
        return "Failed: not a valid command."

def get_input():
    while True:
        command = input("Enter your command: ")
        result = check_commands(command)
        print(result)
        

def go(direction):
    """ Player input a string of direction to move (north, south, west, east).
    If the input is valid (available direction - path is available, not locked), move the player in the input direction; 
    else, returns “unavailable direction” string and prompts user to enter a different direction.
    """
    if direction != "north" and direction != "east" and direction != "south" and direction != "west":
        return direction
    if status_module.location == "vestibule":
        if direction == "north":
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
        if direction == "north":
            status_module.location = "classroom_1"
            return "Success!"
        if direction == "east":
            if status_module.locked["classroom_2"] == True:
                return "Failed: this door is locked."
            else: 
                status_module.location = "classroom_2"
                return "Success!"
        if direction == "south":
            status_module.location = "vestibule"
            return "Success!"
        if direction == "west":
            status_module.location = "library"
            return "Success!"
    if status_module.location == "classroom_1":
        if direction == "east":
            if status_module.locked["supply_closet"] == True:
                return "Failed: this door is locked."
            else:
                status_module.location = "supply_closet"
                return "Sucess!"
        if direction == "south":
            status_module.location = "atrium"
            return "Success!"
        else: 
            return "Failed: you can't go that way."
    if status_module.location == "supply_closet":
        if direction == "west":
            status_module.location == "classroom_1"
            return "Success!"
        else:
            return "Failed: you can't go that way."
    if status_module.location == "classroom_2":
        if direction == "west":
            status_module.location == "atrium"
            return "Success!"
        else:
           return "Failed: you can't go that way."
    if status_module.location == "library":
        if direction == "north":
            if status_module.locked["classroom_3"] == True:
                return "Failed: door is locked."
            else:
                status_module.location = "classroom_3"
                return "Success!"
        if direction == "east":
            if status_module.locked["dean_office"] == True:
                return "Failed: door is locked."
            else:
                status_module.location = "dean_office"
                return "Success!"
        if direction == "south":
            status_module.location = "balcony"
            return "Success!"
        if direction == "west":
            status_module.location = "atrium"
            return "Success!"
    if status_module.location == "classroom_3":
        if direction == "south":
            status_module.location = "library"
            return "Success!"
        else:
            return "Failed: you can't go that way."
    if status_module.location == "dean_office":
        if direction == "west":
            status_module.location = "library"
            return "Success!"
        else:
            return "Failed: you can't go that way."
    if status_module.location == "balcony":
        if direction == "north":
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
    
def examine(subject):
    """ Player input a string of a subject to examine. 
    If the input is valid (subject is available in location), let player interact with each object (open, close, display item available, etc).
    """
    if status_module.location == "atrium" and subject in status_module.atrium_objects:
        if subject == "old door":
            return status_module.old_door_flavor
        if subject == "indoor plants":
            return status_module.indoor_plants_flavor
        if subject == "central staircase":
            return status_module.central_staircase_flavor
    elif status_module.location == "vestibule" and subject in status_module.vestibule_objects:
        if subject == "keycard door":
            return status_module.keycard_door_flavor
        if subject == "touchscreen directory":
            return status_module.touchscreen_directory_flavor
        if subject == "coat hooks":
            return status_module.coat_hooks_flavor
    elif status_module.location == "classroom_1" and subject in status_module.classroom_1_objects: 
        if subject == "smartboard":
            return status_module.smartboard_flavor
        if subject == "lab stools":
            return status_module.lab_stools_flavor
        if subject == "supply drawers":
            return status_module.supply_drawers_flavor  
    elif status_module.location == "supply_closet" and subject in status_module.supply_closet_objects:
        if subject == "equipment shelves":
            return status_module.equipment_shelves_flavor
        if subject == "PPE cabinet":
            return status_module.ppe_cabinet_flavor
    elif status_module.location == "classroom_2" and subject in status_module.classroom_2_objects:
        if subject == "lab benches":
            return status_module.lab_benches_flavor
        if subject == "safety cabinet":
            return status_module.safety_cabinet_flavor
        if subject == "wall-mounted monitor":
            return status_module.wall_mounted_monitor_flavor
    elif status_module.location == "library" and subject in status_module.library_objects:
        if subject == "mahogany bookcase":
            status_module.inventory.append("drawer key")
            return status_module.mahogany_bookcase_flavor
        if subject == "librarian's desk":
            return status_module.librarian_desk_flavor
        if subject == "study table":
            return status_module.study_table_flavor
        if subject == "gold door":
            return status_module.gold_door_flavor
        if subject == "shiny door":
            return status_module.shiny_door_flavor
    elif status_module.location == "balcony" and subject in status_module.balcony_objects:
        if subject == "glass railing":
            return status_module.glass_railing_flavor
        if subject == "potted plants":
            return status_module.potted_plants_flavor
    elif status_module.location == "classroom_3" and subject in status_module.classroom_3_objects:
        if subject == "3D printers":
            return status_module.printer_flavor
        if subject == "power outlets":
            return status_module.power_outlets_flavor
        if subject == "robotic kits":
            return status_module.robotics_kits_flavor
    elif status_module.location == "dean_office" and subject in status_module.dean_office_objects:
        if subject == "ergonomic desk":
            return status_module.ergonomic_desk_flavor
        if subject == "bookshelf with scientific journals":
            return status_module.bookshelf_flavor
        if subject == "Smith College crest plaque":
            return status_module.crest_plaque_flavor
    else:
        return "You can't find that object right now."


def use(item, subject):
    """ Player input a string of the name of item want to use and a string of the name of the targetted subject.
    If the input is valid (item available in inventory and the target is an interactable object at location), modify game state based on item effect 
    (eg. unlock door → new available direction for move).
    Remove item from inventory after use and show the available items in the inventory.
    """
    # Check if item is available in inventory
    if item in status_module.inventory:
        # Check if the target in an interactable object at location
        if status_module.location == "atrium" and item == "old key" and subject == "old door":
            status_module.locked["old door"] == False
            status_module.inventory.remove("old key") 
            return "You unlocked the door to classroom 2!"
        elif status_module.location == "classroom_1" and item == "rusty key" and subject == "rusty door":
            status_module.locked["rusty door"] == False
            status_module.inventory.remove("rusty key")
            return "You unlocked the door to the supply closet!"
        elif status_module.location == "library" and item == "drawer key" and subject == "librarian desk":
            status_module.locked["librarian desk"] == False
            status_module.inventory.remove("drawer key")
            return "You unlocked the door to the librarian's desk!"
        elif status_module.location == "library" and item == "gold key" and subject == "gold door":
            status_module.locked["gold door"] == False
            status_module.inventory.remove("gold key")
            return "You unlocked the door to the dean's office!"
        elif status_module.location == "library" and item == "shiny key" and subject == "shiny door":
            status_module.locked["shiny door"] == False
            status_module.inventory.remove("shiny key")
            return "You unlocked the door to the dean's office!"
        elif status_module.location == "vestibule" and item == "keycard" and subject == "keycard door":
            status_module.locked["keycard door"] == False
            status_module.inventory.remove("keycard")
            return "You unlocked the exit door! Now you can out of here!"
def save_game():
    ''' writes project file with status module: inventory, location, etc.)'''

def load_game():
    '''reads file data and loads variables from past game'''
