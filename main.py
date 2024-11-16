# beginning the game
import command_module

def main():
    command_module.menu()
    while True:
        command_module.get_input()
        if command_module.win == True:
            replay = command_module.winner()
            if replay == True:
                continue
            else:
                break 




if __name__ == "__main__":
    main()