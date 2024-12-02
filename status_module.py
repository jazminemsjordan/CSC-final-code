def initialize():
    global location
    location = "vestibule"
    global locked
    locked = {"supply_closet": True, "classroom_2": True, "classroom_3": True, "dean_office": True}
    global item_pairs
    item_pairs = {"old key": "old door", "keycard": "keycard door", "rusty key": "rusty door", "shiny key": "shiny door", "gold key": "gold door", "small key": "small drawer"}
    global inventory
    inventory = []
    global turn
    turn = 0
    global win 
    win = False

def end_menu():
    """ Shows end data and stats, variable counter for turns taken added every time a command is successful."""

def start_menu():
    """ Call instructions function and ask whether to begin a new game or reset."""

vestibule_flavor = "text"
vestibule_objects = []

atrium_flavor = "text"
atrium_objects = []

classroom_1_flavor = ""
classroom_1_objects = []

classroom_2_flavor = ""
classroom_2_objects = []

classroom_3_flavor = ""
classroom_3_objects = []

supply_closet_flavor = ""
supply_closet_objects = []

library_flavor = "You are in the library. Floor to ceiling bookshelves line the walls, with a few cozy looking chairs and couches in the center. Objects of interest: librarian's desk, study table, mahogany bookcase. To the north is Classroom 3. To the east is the Dean's Office. To the South is the balcony. To the West is the stairwell down to the atrium."
library_objects = ["librarian's desk", "study table", "mahogany bookcase"]

dean_office_flavor = ""
dean_office_objects = []

balcony_flavor = ""
balcony_objects = []

command_list = ["go", "look", "examine", "use"]

