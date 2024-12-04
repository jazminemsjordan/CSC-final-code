def initialize():
    global location
    location = "vestibule"
    global locked
    locked = {"supply_closet": True, "classroom_2": True, "classroom_3": True, "dean_office": True}
    global item_pairs
    item_pairs = {"old key": "old door", "keycard": "keycard door", "rusty key": "rusty door", "shiny key": "shiny door", "gold key": "gold door", "drawer key": "librarian's desk"}
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

vestibule_flavor = "You are in the vestibule. The entrance is framed by sleek glass walls and natural stone flooring, with clean lines that hint at the building's contemporary design.\nObjects of interest: touchscreen directory, coat hooks, charging station, keycard door.\nTo the North is the Atrium."
vestibule_objects = ["keycard door", "touchscreen directory", "coat hooks", "charging station"]
keycard_door_flavor = "The exit to the building is locked."
touchscreen_directory flavor = ""
coat_hooks_flavor = ""
charging_station_flavor = ""

atrium_flavor = "You are in the atrium. The expansive central space features soaring ceilings, an open staircase, and wide windows that flood the room with light. Collaborative seating areas dot the floor, inviting group discussions.\nObjects of interest: indoor plants, central staircase, rusty door, old door.\nTo the North is Classroom 1. To the East is Classroom 2. To the West is the Stairwell. To the South is the Vestibule."
atrium_objects = ["old door", "rusty door", "indoor plants", "central staircase"]
old_door_flavor = "The old door is locked. The faded sign reads "Classroom 1."
rusty_door_flavor = "The rusted door to the supply closet is locked."

classroom_1_flavor = "You are in Classroom 1. A mix of modular tables and chairs fills the room, designed for interactive learning. A smartboard stretches across one wall, flanked by writable whiteboard surfaces.\nObjects of interest: smartboard, lab stools, supply drawers.\nTo the South is the Atrium. To the East is the supply closet."
classroom_1_objects = ["smartboard", "lab stools", "supply drawers"]

classroom_2_flavor = "You are in Classroom 2. Rows of lab benches are equipped with sinks and microscopes, with overhead fume hoods lining the perimeter. The room is primed for hands-on experimentation.\nObjects of interest: lab benches, safety cabinet, wall-mounted monitor.\nTo the West is the Atrium."
classroom_2_objects = ["lab benches", "safety cabinet", "wall-mounted monitor"]

classroom_3_flavor = "You are in Classroom 3. The room features workstations with power outlets, 3D printers, and toolkits neatly arranged along the walls.\nObjects of interest: 3D printer, soldering station, robotics kits.\nTo the South is the Library."
classroom_3_objects = ["3D printer", "power outlets", "robotics kits"]

supply_closet_flavor = "You are in the Supply Closet. Compact and efficient, the room houses rows of labeled bins holding everything from lab coats to specialized tools.\nObjects of interest: equipment shelves, PPE cabinet.\nTo the east is Classroom 3."
supply_closet_objects = ["equipment shelves", "PPE cabinet"]

library_flavor = "You are in the library. Floor to ceiling bookshelves line the walls, with a few cozy looking chairs and couches in the center.\nObjects of interest: librarian desk, study table, mahogany bookcase.\nTo the north is Classroom 3. To the east is the Dean's Office. To the South is the balcony. To the West is the stairwell down to the atrium."
library_objects = ["librarian desk", "study table", "mahogany bookcase", "shiny door", "gold door"]
def mahogany_bookcase_puzzle():
    print("The bookcase is tall and intimidating, with a variety of colorful books. Which would you like to check?")
    book = input("Which color book do you select?")
    if book == "violet":
        inventory.append("drawer key")
        return("You open the violet book to find it hollowed out. There's a key inside! You got: drawer key.")
    else:
        return("You open the " + book + " book, but see nothing of note.")
librarian_desk_flavor = "The desk is well-used, covered in books and scribbles on the wood. You notice a small lock on one of the drawers."
study_table_flavor = "The study table is covered in a thin layer of dust. Apparently nobody has studied here for a while. You see nothing important."


dean_office_flavor = "You are in the Dean's Office. The room balances modernity and warmth, with contemporary furniture and framed photographs of recent projects and alumni achievements.\nObjects of interest: ergonomic desk, bookshelf with scientific journals, Smith College crest plaque.\nTo the West is the Library."
dean_office_objects = ["ergonomic desk", "bookshelf with scientific journals", "Smith College crest plaque"]

balcony_flavor = "You are on the Balcony. Glass railings provide an uninterrupted view of the campus greenery below, with a few seating options tucked in for a quiet moment between classes.\nObjects of interest: glass railing, potted plants.\nTo the north is the Library."
balcony_objects = ["glass railing", "potted plants"]

command_list = ["go", "look", "examine", "use"]

