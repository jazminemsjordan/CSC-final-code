# %%
def initialize():
    global location
    location = "vestibule"
    global locked
    locked = {"supply_closet": True, "classroom_2": True, "classroom_3": True, "dean_office": True, "exit": True, "drawer": True}
    global item_pairs
    item_pairs = {"old key": "old door", "keycard": "keycard door", "rusty key": "rusty door", "shiny key": "shiny door", "gold key": "gold door", "drawer key": "librarian's desk"}
    global inventory
    inventory = []
    global turns
    turns = 0
    global win 
    win = False

# %%
def instructions():
    print("To play: enter a simple command: 'go' to move, look(l) to see the room you're in, examine(x) to investigate an object\n, help(?) to view commands, or inventory(i) to view inventory.\n Examples include 'go north' or 'look' or 'examine bookcase'.")


# %%
def end_menu():
    """ Shows end data and stats, variable counter for turns taken added every time a command is successful."""
    print("---------------------")
    print("Congratulations! You win!")
    print(f"Turns taken = {turns} turns.")
    exit()


# %%
def start_menu():
    """ Call instructions function and ask whether to begin a new game or reset."""
    print("Christmas at Ford Hall")
    print("-----------------------")
    print("Oh no! The doors locked for Christmas break while you were still inside the hall. Can you escape and make it home for the holidays?")
    initialize()
    start = input("Start game: Y/N?")
    if start == "Y" or start == "y":
        instructions()
    else:
        exit()

# %%
vestibule_flavor = "You are in the vestibule. The entrance is framed by sleek glass walls and natural stone flooring, with clean lines that hint at the building's contemporary design.\nObjects of interest: touchscreen directory, coat hooks, charging station, keycard door.\nTo the North is the Atrium. To the South is the exit."
vestibule_objects = ["keycard door", "touchscreen directory", "coat hooks", "charging station"]

# %%
keycard_door_flavor = "The exit to the building, barred by a large mechanical door."

# %%
touchscreen_directory_flavor = "The touchscreen directory glows faintly, displaying a map of the building. A sticky note tucked into the frame reads, 'Merry Christmas?!'"
coat_hooks_flavor = "A neat row of coat hooks lines the wall. Most of them are empty, but one hook holds a scarf with 'Christmas HO HO HO' embroidered on it."
charging_station_flavor = "The blinking red light appears to be a malfunction, and nothing else catches your attention."

# %%
atrium_flavor = "You are in the atrium. The expansive central space features soaring ceilings, an open staircase, and wide windows that flood the room with light. Collaborative seating areas dot the floor, inviting group discussions.\nObjects of interest: indoor plants, central staircase, old door.\nTo the North is Classroom 1. To the East is Classroom 2. To the West is the Stairwell. To the South is the Vestibule."
atrium_objects = ["old door", "indoor plants", "central staircase"]

# %%
old_door_flavor = "The faded sign besides the old door reads Classroom 2."

# %%
indoor_plants_flavor = "A collection of potted indoor plants adds a touch of green. Beneath one pot is a faint scratch, but there's nothing of importance."
central_staircase_flavor = "The central staircase spirals to the upper levels, its clean lines uninterrupted by anything unusual."

# %%
classroom_1_flavor = "You are in Classroom 1. A mix of modular tables and chairs fills the room, designed for interactive learning. A smartboard stretches across one wall, flanked by writable whiteboard surfaces.\nObjects of interest: smartboard, lab stools, supply drawers, rusty door.\nTo the South is the Atrium. To the East is the supply closet."
classroom_1_objects = ["smartboard", "lab stools", "supply drawers", "rusty door"]

# %%
rusty_door_flavor = "The rusty door to the supply closet is old and weathered."

# %%
smartboard_flavor = "The smartboard faintly glows, displaying 'No Input Detected.' A USB port is visible, but you find nothing significant."
lab_stools_flavor = "The lab stools are neatly arranged. Underneath one, theres an old piece of gum—gross, but nothing useful"
supply_drawers_flavor = "A row of drawers lines the room. They are all empty, except for an mix of old lab tools and a flash of metal. You found: rusty key."

# %%
classroom_2_flavor = "You are in Classroom 2. Rows of lab benches are equipped with sinks and microscopes, with overhead fume hoods lining the perimeter. The room is primed for hands-on experimentation.\nObjects of interest: lab benches, safety cabinet, wall-mounted monitor.\nTo the West is the Atrium."
classroom_2_objects = ["lab benches", "safety cabinet", "wall-mounted monitor"]

# %%
lab_benches_flavor = "The lab benches are cluttered with abandoned experiments—beakers, pipettes, and half-written notes. There's a tiny key by one of the beakers. You got: drawer key."
safety_cabinet_flavor = "The safety cabinet is locked and contains standard safety gear—nothing useful."
wall_mounted_monitor_flavor = "The wall-mounted monitor is dark, with a fingerprint smudge on the screen. It appears non-functional."

# %%
classroom_3_flavor = "You are in Classroom 3. The room features workstations with power outlets, 3D printers, and toolkits neatly arranged along the walls.\nObjects of interest: 3D printer, power outlets, robotics kits.\nTo the South is the Library."
classroom_3_objects = ["3D printer", "power outlets", "robotics kits"]

# %%
printer_flavor = "The 3D printer hums quietly. On the platform sits a newly printed object—a gold key is put next to the unfinished project. You found: gold key."
power_outlets_flavor = "Rows of power outlets blink green. One outlet blinks red but reveals nothing unusual."
robotics_kits_flavor = "The robotics kits are neatly arranged in plastic bins. None of them hold anything important."

# %%
supply_closet_flavor = "You are in the Supply Closet. Compact and efficient, the room houses rows of labeled bins holding everything from lab coats to specialized tools.\nObjects of interest: equipment shelves, PPE cabinet.\nTo the west is Classroom 1."
supply_closet_objects = ["equipment shelves", "PPE cabinet"]

# %%
equipment_shelves_flavor = "The equipment shelves are packed with supplies—spools of wire, boxes of screws, and a small toolkit that seems unusually dusty. Beside it is a key. You found: old key."
ppe_cabinet_flavor = "The PPE cabinet is filled with goggles and gloves but no hidden items."

# %%
library_flavor = "You are in the library. Floor to ceiling bookshelves line the walls, with a few cozy looking chairs and couches in the center.\nObjects of interest: librarian's desk, study table, mahogany bookcase, shiny door, gold door.\nTo the north is Classroom 3. To the east is the Dean's Office. To the South is the balcony. To the West is the stairwell down to the atrium."
library_objects = ["librarian's desk", "study table", "mahogany bookcase", "shiny door", "gold door"]

# %%
mahogany_bookcase_flavor = "There's a variety of colorful books on all different topics, but none seem useful right now."

# %%
librarian_desk_flavor = "The desk is well-used, covered in books and scribbles on the wood. You notice a small lock on one of the drawers."

# %%
study_table_flavor = "The study table is covered in a thin layer of dust. Apparently nobody has studied here for a while. You see nothing important."

# %%
shiny_door_flavor = "The shiny door to the newest classroom, with a shiny lock."

# %%
gold_door_flavor = "The ornate door to the Dean's Office has a golden lock."

# %%
dean_office_flavor = "You are in the Dean's Office. The room balances modernity and warmth, with contemporary furniture and framed photographs of recent projects and alumni achievements.\nObjects of interest: ergonomic desk, bookshelf with scientific journals, Smith College crest plaque.\nTo the West is the Library."
dean_office_objects = ["ergonomic desk", "bookshelf with scientific journals", "Smith College crest plaque"]

# %%
ergonomic_desk_flavor = "The ergonomic desk is organized and spotless. There's nothing hidden here."
bookshelf_flavor = "The bookshelf contains scientific journals. One journal is wedged at an odd angle but holds no items."
crest_plaque_flavor = "The Smith College crest plaque hangs above the desk, pristine but ordinary. Inside the frame lies an official looking plastic card, also bearing the Smith logo. You got: keycard."

# %%
balcony_flavor = "You are on the Balcony. Glass railings provide an uninterrupted view of the campus greenery below, with a few seating options tucked in for a quiet moment between classes.\nObjects of interest: glass railing, potted plants.\nTo the north is the Library."
balcony_objects = ["glass railing", "potted plants"]

# %%
glass_railing_flavor = "The glass railing offers a beautiful view but has no apparent hiding spots for anything significant."
potted_plants_flavor = "The potted plants are vibrant, but closer inspection reveals no hidden items."

# %%
command_list = ["go", "look", "examine", "use", "inventory", "help"]

