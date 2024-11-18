# beginning the game
import command_module

def main():
    command_module.menu()
    while True:
        command_module.get_input()
        if status_module.win == True:
            command_module.end_menu()




if __name__ == "__main__":
    main()
