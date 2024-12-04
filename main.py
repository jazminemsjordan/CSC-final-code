# beginning the game
import command_module
import status_module

def main():
    command_module.start_menu()
    while True:
        command_module.get_input()
        status_module.turns += 1
        if status_module.win == True:
            command_module.end_menu()




if __name__ == "__main__":
    main()
