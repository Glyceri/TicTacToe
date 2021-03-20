from Game import Game
Quit = False

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

def NameCheck():
    print("Player One please enter your name:")
    gameRules.name1 = str(input())
    print("Welcome:", gameRules.name1)
    print("Player Two please enter your name:")
    gameRules.name2 = str(input())
    print("Welcome:", gameRules.name2)
    return

def SetupBoard(size):
    gameRules.boardSize = size
    gameRules.Board = [" "] * ((size + 1) * (size + 1))
    SetNode(0, "X")
    return

def PrintBoard():
    counter = 0
    board_text = ""
    for i in range(len(gameRules.Board)):

        counter += 1
        board_text += "[" + gameRules.Board[i] + "]"

        if counter > gameRules.boardSize:
            counter = 0
            print(board_text)
            board_text = ""

def SetNode(selector, setToo):
    gameRules.Board[selector] = setToo
        


while Quit == False:
    print("Welcome to Tic Tac Toe")
    gameRules = Game()
    SetupBoard(3)
    PrintBoard()
    NameCheck()
    


    Quit = QuitCheck()



print("Bye bye")