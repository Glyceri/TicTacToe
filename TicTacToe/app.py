import extra
Quit = False
Board = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]


while Quit == False:
    Board = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]
    print("Welcome to Tic Tac Toe")
    extra.PrintBoard()
    extra.NameCheck()
    
    Quit = extra.QuitCheck()



print("Bye bye")