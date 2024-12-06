def initialize():
    global location
    location = "vestibule"
    global locked
    locked = {"supply_closet": True, "classroom_2": True, "classroom_3": True, "dean_office": True, "exit": True, "drawer": True}
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
if locked["exit"] == True:
    keycard_door_flavor = "The exit to the building is locked."
elif locked["exit"] == False:
    keycard_door_flavor = "The exit to the building is unlocked."
else: 
    keycard_door_flavor = "error"
touchscreen_directory_flavor = ""
coat_hooks_flavor = ""
charging_station_flavor = ""

atrium_flavor = "You are in the atrium. The expansive central space features soaring ceilings, an open staircase, and wide windows that flood the room with light. Collaborative seating areas dot the floor, inviting group discussions.\nObjects of interest: indoor plants, central staircase, rusty door, old door.\nTo the North is Classroom 1. To the East is Classroom 2. To the West is the Stairwell. To the South is the Vestibule."
atrium_objects = ["old door", "indoor plants", "central staircase"]
if locked["classroom_2"] == True:
    old_door_flavor = "The old door is locked. The faded sign reads Classroom 2."
elif locked["classroom_2"] == False:
    old_door_flavor = "The old door is unlocked. The faded sign reads Classroom 2."
else:
    old_door_flavor = "error"
indoor_plants_flavor = ""
central_staircase_flavor = ""

classroom_1_flavor = "You are in Classroom 1. A mix of modular tables and chairs fills the room, designed for interactive learning. A smartboard stretches across one wall, flanked by writable whiteboard surfaces.\nObjects of interest: smartboard, lab stools, supply drawers.\nTo the South is the Atrium. To the East is the supply closet."
classroom_1_objects = ["smartboard", "lab stools", "supply drawer", "rusty door"]
if locked["supply closet"] == True:
    rusty_door_flavor = "The rusted door to the supply closet is locked."
elif locked["supply closet"] == False:
    rusty_door_flavor = "The rusted door to the supply closet is unlocked."
else:
    rusty_door_flavor = "error"
smartboard_flavor = ""
lab_stools_flavor = ""
supply_drawers_flavor = ""

classroom_2_flavor = "You are in Classroom 2. Rows of lab benches are equipped with sinks and microscopes, with overhead fume hoods lining the perimeter. The room is primed for hands-on experimentation.\nObjects of interest: lab benches, safety cabinet, wall-mounted monitor.\nTo the West is the Atrium."
classroom_2_objects = ["lab benches", "safety cabinet", "wall-mounted monitor"]
lab_benches_flavor = ""
safety_cabinet_flavor = ""
wall_mounted_monitor_flavor = ""

classroom_3_flavor = "You are in Classroom 3. The room features workstations with power outlets, 3D printers, and toolkits neatly arranged along the walls.\nObjects of interest: 3D printer, soldering station, robotics kits.\nTo the South is the Library."
classroom_3_objects = ["3D printer", "power outlets", "robotics kits"]
printer_flavor = ""
power_outlets_flavor = ""
robotics_kits_flavor = ""

supply_closet_flavor = "You are in the Supply Closet. Compact and efficient, the room houses rows of labeled bins holding everything from lab coats to specialized tools.\nObjects of interest: equipment shelves, PPE cabinet.\nTo the east is Classroom 3."
supply_closet_objects = ["equipment shelves", "PPE cabinet"]
equipment_shelves_flavor = ""
ppe_cabinet_flavor = ""

library_flavor = "You are in the library. Floor to ceiling bookshelves line the walls, with a few cozy looking chairs and couches in the center.\nObjects of interest: librarian desk, study table, mahogany bookcase.\nTo the north is Classroom 3. To the east is the Dean's Office. To the South is the balcony. To the West is the stairwell down to the atrium."
library_objects = ["librarian desk", "study table", "mahogany bookcase", "shiny door", "gold door"]
mahogany_bookcase_flavor = "There's a bright book that seems out of place. You open the violet book to find it hollowed out."
if locked["drawer"] == True:
    librarian_desk_flavor = "The desk is well-used, covered in books and scribbles on the wood. You notice a small lock on one of the drawers."
elif locked["classroom_2"] == False:
    librarian_desk_flavor = "The desk is well-used, covered in books and scribbles on the wood. You notice a small lock on one of the drawers. It's open."
else:
    librarian_desk_flavor = "error"
study_table_flavor = "The study table is covered in a thin layer of dust. Apparently nobody has studied here for a while. You see nothing important."
if locked["classroom_2"] == True:
    shiny_door_flavor = "The shiny door to the newest classroom is locked."
elif locked["classroom_2"] == False:
    shiny_door_flavor = "The shiny door to the newest classroom is unlocked."
else:
    shiny_door_flavor = "error"
if locked["dean_office"] == True:
    gold_door_flavor = "The ornate gold door to the Dean's Office is locked."
elif locked["classroom_2"] == False:
    gold_door_flavor = "The ornate gold door the the Dean's Office is unlocked."
else:
    gold_door_flavor = "error"

dean_office_flavor = "You are in the Dean's Office. The room balances modernity and warmth, with contemporary furniture and framed photographs of recent projects and alumni achievements.\nObjects of interest: ergonomic desk, bookshelf with scientific journals, Smith College crest plaque.\nTo the West is the Library."
dean_office_objects = ["ergonomic desk", "bookshelf with scientific journals", "Smith College crest plaque"]
ergonomic_desk_flavor = ""
bookshelf_flavor = ""
crest_plague_flavor = ""

balcony_flavor = "You are on the Balcony. Glass railings provide an uninterrupted view of the campus greenery below, with a few seating options tucked in for a quiet moment between classes.\nObjects of interest: glass railing, potted plants.\nTo the north is the Library."
balcony_objects = ["glass railing", "potted plants"]
glass_railing_flavor = ""
potted_plants_flavor = ""

command_list = ["go", "look", "examine", "use"]

