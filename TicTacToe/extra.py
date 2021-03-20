

def QuitCheck():
    print("Want to play another round. Type 'y' or 'n'")
    ShouldQuit = str(input())
    if ShouldQuit == 'n':
        return True
    elif ShouldQuit == 'y':
        return False
    else:
        print("Please input a 'y' or 'n'")
        return QuitCheck()


name1 = ""
name2 = ""

def NameCheck():
    print("Player One please enter your name:")
    name1 = str(input())
    print("Welcome:", name1)
    print("Player Two please enter your name:")
    name2 = str(input())
    print("Welcome:", name2)


def PrintBoard():
    from app import Board
    for i in range(len(Board)):
        for j in len(Board[i]):
            print(j)