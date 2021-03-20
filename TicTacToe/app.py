from Game import Game
Quit = False
WinnerFound = False

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
    gameRules.boardSize = size + 1
    gameRules.Board = [" "] * ((size + 1) * (size + 1))
    SetNode(0, "+")
    for i in range(1, gameRules.boardSize):
        SetNode(i, chr(96+i).upper())
    for i in range(1, gameRules.boardSize):
        SetNode((gameRules.boardSize) * i, str(i))
    return

def PrintBoard():
    counter = 0
    board_text = ""
    for i in range(len(gameRules.Board)):

        counter += 1
        board_text += "[" + gameRules.Board[i] + "]"

        if counter >= gameRules.boardSize:
            counter = 0
            print(board_text)
            board_text = ""

def SetNode(selector, setToo):
    gameRules.Board[selector] = setToo
        
def GetNode(selector):
    return gameRules.Board[selector]


def PlayRound():
    PrintBoard()
    PrintRound()
    GatherInput()

    if gameRules.Turn == 0:
        gameRules.Turn = 1
    elif gameRules.Turn == 1:
        gameRules.Turn = 0
    
    if CheckIfDraw():
        return False
    return NoWinnerFound()

def CheckIfDraw():
    IsDraw = True
    for i in range(len(gameRules.Board)):
        if gameRules.Board[i] == " ":
            IsDraw = False
    if IsDraw:
        print("It's a Draw")
    return IsDraw

def NoWinnerFound():
    CorrectSymbols = ["X","O"]
    for i in CorrectSymbols:
        if LeftRight(i) or BotTop(i) or Diagonal(i):
            WinnerText(i)
            return False

    return True

def WinnerText(num):
    PrintBoard()
    if num == "X":
        print(gameRules.name1,"is the winner!")
    else:
        print(gameRules.name2,"is the winner!")

def LeftRight(symb):
    for i in range(gameRules.boardSize - 1):

        i += 1
        i *= gameRules.boardSize
        i += 1

        Win = True
        for f in range(i, i + (gameRules.boardSize - 1)):
            if gameRules.Board[f] != symb:
                Win = False
        if Win:
            return True

    return False


def BotTop(symb):
    for i in range(gameRules.boardSize + 1, gameRules.boardSize + 1 + gameRules.boardSize - 1):
        Win = True
        for f in range(gameRules.boardSize-1):
            if gameRules.Board[i + (gameRules.boardSize * f)] != symb:
                Win = False
        if Win:
            return True

    return False

def Diagonal(symb):
    
    i = gameRules.boardSize + 1

    Win = True
    for f in range(gameRules.boardSize - 1):
        if gameRules.Board[i + (gameRules.boardSize * f) + f] != symb:
            Win = False
    if Win:
        return True

    i = (gameRules.boardSize * 2) - 1

    Win = True
    for f in range(gameRules.boardSize - 1):
        if gameRules.Board[i + (gameRules.boardSize * f) - f] != symb:
            Win = False
    if Win:
        return True

    return False

def PrintRound():
    if gameRules.Turn == 0:
        print("It's", gameRules.name1, "'s turn. Please make a move.")
    elif gameRules.Turn == 1:
        print("It's", gameRules.name2, "'s turn. Please make a move.")


def GatherInput():
    try:
        InputPlayer = input()
        list_input = list(InputPlayer)

        if list_input[0].isalpha:
            Num = ord(list_input[0].lower()) - 96
            del list_input[0]

        listToStr = ' '.join([str(elem) for elem in list_input])
        Num2 = int(listToStr) 

        ActualNum = Num + (Num2 * gameRules.boardSize)
        if ActualNum >= (gameRules.boardSize * gameRules.boardSize):
            return WrongInput()
        elif Num >= gameRules.boardSize:
            return WrongInput()
        elif Num2 >= gameRules.boardSize:
            return WrongInput()
        else:
            if GetNode(ActualNum) == " ":
                if gameRules.Turn == 0:
                    SetNode(ActualNum, "X")
                elif gameRules.Turn == 1:
                    SetNode(ActualNum, "O")
            else:
                return WrongInput()
    
    except Exception as e:
        return WrongInput()
    
def WrongInput():
    print("Invalid input, try again.")
    return GatherInput()

while Quit == False:
    print("Welcome to Tic Tac Toe")
    gameRules = Game()
    SetupBoard(3)
    NameCheck()

    while(PlayRound()):
        none = None


    Quit = QuitCheck()
    


print("Bye bye")