import status_module 
# test comment

def check_commands(command):
    if command in status_module.command_list:
        if command == "go":
            direction = input("Where would you like to go?")
            return go(direction)
        if command == "look":
            return look()
        if command == "examine":
            object = input("What would you like to examine?")
            return examine(object):

    else:
        return "Failed: not a valid command."


def get_input():
    while True:
        command = input("Enter your command: ")
        result = check_commands(command)
        print(result)
        

def go(direction):
    global location
    if direction != "north" and direction != "east" and direction != "south" and direction != "west":
        return "Failed: not a valid direction."
    if location == "vestibule":
        if direction == "north":
            location = "atrium"
            return "Success!"
        if direction == "south":
            if status_module.locked["exit"] == True:
                return "Failed: the exit is locked."
            else: 
                return "win"
        else:
            return "Failed: you can't go that way."
    if location == "atrium":
        if direction == "north":
            location = "classroom_1"
            return "Success!"
        if direction == "east":
            if status_module.locked["classroom_2"] == True:
                return "Failed: this door is locked."
            else: 
                location = "classroom_2"
                return "Success!"
        if direction == "south":
            location = "vestibule"
            return "Success!"
        if direction == "west":
            location = "library"
            return "Success!"
    if location == "classroom_1":
        if direction == "east":
            if status_module.locked["supply_closet"] == True:
                return "Failed: this door is locked."
            else:
                location = "supply_closet"
                return "Sucess!"
        if direction == "south":
            location = "atrium"
            return "Success!"
        else: 
            return "Failed: you can't go that way."
    if location == "supply_closet":
        if direction == "west":
            location == "classroom_1"
            return "Success!"
        else:
            return "Failed: you can't go that way."
    if location == "classroom_2":
        if direction == "west":
            location == "atrium"
            return "Success!"
        else:
           return "Failed: you can't go that way."
    if location == "library":
        if direction == "north":
            if status_module.locked["classroom_3"] == True:
                return "Failed: door is locked."
            else:
                location = "classroom_3"
                return "Success!"
        if direction == "east":
            if status_module.locked["dean_office"] == True:
                return "Failed: door is locked."
            else:
                location = "dean_office"
                return "Success!"
        if direction == "south":
            location = "balcony":
            return "Success!"
        if direction == "west":
            location = "atrium"
            return "Success!"
    if location == "classroom_3":
        if direction == "south":
            location = "library"
            return "Success!"
        else:
            return "Failed: you can't go that way."
    if location == "dean_office":
        if direction == "west":
            location = "library"
            return "Success!"
        else:
            return "Failed: you can't go that way."
    if location == "balcony":
        if direction == "north":
            location = "library"
            return "Success!"
        else:
            return "Failed: you can't go that way."


def look():
    if location == "vestibule":
        return status_module.vestibule_flavor
    if location == "atrium":
        return status_module.atrium_flavor
    if location == "classroom_1":
        return status_module.classroom_1_flavor
    if location == "supply_closet":
        return status_module.supply_closet_flavor
    if location == "classroom_2":
        return status_module.classroom_2_flavor
    if location == "library":
        return status_module.library_flavor
    if location == "classroom_3":
        return status_module.classroom_3_flavor
    if location == "dean_office":
        return status_module.dean_office_flavor
    if location == "balcony":
        return status_module.balcony_flavor
    
def examine(subject):
    pass

# Choose item to use at targeted subject
def use(item, subject):
    if item in status_module.inventory:
        if location == "atrium" and subject in status_module.atrium_objects:
            if status_module.item_pairs[item] == subject:
                pass
            else: 
                return "Failed: those things don't go together."
        elif location == "vestibule" and subject in status_module.vestibule_objects:
            if status_module.item_pairs[item] == subject:
                pass
            else: 
                return "Failed: those things don't go together."
        elif location == "classroom_1" and subject in status_module.classroom_1_objects:
            if status_module.item_pairs[item] == subject:
                pass
            else: 
                return "Failed: those things don't go together."    
        elif location == "supply_closet" and subject in status_module.supply_closet_objects:
           if status_module.item_pairs[item] == subject:
                pass
           else: 
                return "Failed: those things don't go together." 
        elif location == "classroom_2" and subject in status_module.classroom_2_objects:
           if status_module.item_pairs[item] == subject:
                pass
           else: 
                return "Failed: those things don't go together." 
        elif location == "library" and subject in status_module.library_objects:
           if status_module.item_pairs[item] == subject:
                pass
           else: 
                return "Failed: those things don't go together." 
        elif location == "balcony" and subject in status_module.balcony_objects:
           if status_module.item_pairs[item] == subject:
                pass
           else: 
                return "Failed: those things don't go together." 
        elif location == "classroom_3" and subject in status_module.classroom_3_objects:
           if status_module.item_pairs[item] == subject:
                pass
           else: 
                return "Failed: those things don't go together." 
        elif location == "dean_office" and subject in status_module.dean_office_objects:
           if status_module.item_pairs[item] == subject:
                pass
           else: 
                return "Failed: those things don't go together." 
        else:
            return "Failed: you don't see that in this room."
    else:
        return "Failed: you don't have that with you."
