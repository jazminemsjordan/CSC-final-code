import status_module 

def check_commands(command):
    """Compares player input to a list of possible gameplay commands.
    If command is valid, runs function command; else, it returns “invalid input” string and prompts the user to enter something else"""
    pass



def get_input():
    pass
        

def go(direction):
    """ Player input a string of direction to move (north, south, west, east).
    If the input is valid (available direction - path is available, not locked), move the player in the input direction; 
    else, returns “unavailable direction” string and prompts user to enter a different direction.
    """
    pass
    # Checking player's location and give available direction for each location
    # If direction is valid, update location


def look():
    """ Provide a description of the player's current location (based on the location variable from go(direction)), including exits, interactable objects
    """
    pass
    
def examine(subject):
    """ Player input a string of a subject to examine. 
    If the input is valid (subject is available in location), let player interact with each object (open, close, display item available, etc).
    """
    pass

def use(item, subject):
    """ Player input a string of the name of item want to use and a string of the name of the targetted subject.
    If the input is valid (item available in inventory and the target is an interactable object at location), modify game state based on item effect 
    (eg. unlock door → new available direction for move).
    Remove item from inventory after use and show the available items in the inventory.
    """
    pass
    # Check if item is available in inventory
        # Check if the target in an interactable object at location

    
def save_game():
    """ Writes project file with status module: inventory, location, etc.)"""
    pass

def load_game():
    """ Reads file data and loads variables from past game """
    pass
