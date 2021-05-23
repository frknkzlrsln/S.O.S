
import  random

# Abouth Rules
explanation1 = "Welcome to game of S.O.S"
explanation2 = "* Rule 1 : Values of Row or Column can not less than 3 or more than 26"
explanation3 = "* Rule 2 : Do not enter any characters except 'S' or 'O' "
explanation4 = "* Rule 3 : The person who made 'S.O.S' in vertical, horizontal or diagonal directions gets 1 point in the game."
explanation5 = "* Rule 4 : The player who made the S.O.S will continue the game without transferring his turn."
explanation6 = "* Rule 5 : The game continues until either 'S' or 'O' has been entered in all squares. The person who the most points at the end of the game wins the game."

print("\n", explanation1.rjust(90), "\n" * 2)
print(explanation2)
print(explanation3)
print(explanation4)
print(explanation5)
print(explanation6)
print("\n")


while True:

    print("\n")
    line =(input("Please ,Enter the number of ROW : \t"))
    column = (input("Please ,Enter the number of COLUMN : \t"))
    print("\n")

    if not line.isnumeric() or not column.isnumeric():
        print("Enter only numbers for row and column !")
        print("\n")
        continue

    else:
        line = int(line)
        column = int(column)

    if line <= 2 or column <= 2 or line > 26 or column > 26:
        print(
            "One of the Row or Column values ​​entered is incorrect  !! (Values of Row or Column can not less than 3 or more than 26!) \n ")
        continue


    else:

        squareNumber = 0
        s_Character_Positions = list([])
        o_Character_Positions = list([])
        board = []
        indexesOfBoard = set({})

        table = "SCORE TABLE"
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        alphabetList = list((alphabet).upper())

        player1Score = 0
        player2Score = 0
        player1 = input("Enter the name of Player 1 : \t").upper()
        player2 = input("Enter the name of Player 2 : \t").upper()
        firstPlayer = random.choice([player1, player2])
        playerTurn = firstPlayer


        # creating game board
        def BOARDFRAME():
            for i in range(line):
                tempList = []
                for x in range(column):
                    tempList.append("-")
                    indexesOfBoard.add((i, x))

                board.append(tempList)


        # naming rows and columns on the game board
        def BOARD():
            print("*" * 50, "\n")

            for i in range(line):
                if i == 0:
                    print(("{:>9}" * len(alphabetList[slice(column)])).format(*alphabetList[slice(column)]))
                print("\n")
                for y in range(column):

                    print(f"{board[i][y]:>9}", end="")
                    if y == column - 1:
                        print(f"{alphabetList[i]:>8}", end="")
                print("\n")

            print("*" * 50, "\n")


        def OUTOFBOARD(val):
            if val not in indexesOfBoard:
                return True
            else:
                return False


        def SCORETABLE(val=squareNumber):
            print("\n")
            print(f"| {table:^25} |".rjust(40), ("-" * 29).rjust(40), sep="\n")
            print(f"{player1}: {player1Score} {player2:>15}: {player2Score}".rjust(39))
            print("\n")
            if squareNumber != line * column:
                print(f"Active Player : {playerTurn.upper():}".rjust(34))
            print("\n")


        print("\n")
        BOARDFRAME()
        BOARD()

    while squareNumber < line * column:

        SCORETABLE()

        locationLine = input("Select the Row location of the value you want to enter: \t").upper()
        locationColumn = input("Select the Column location of the value you want to enter: \t").upper()
        print("\n" * 2)

        if locationLine not in alphabetList or locationColumn not in alphabetList:
            print(f"One of the '{locationLine}' or '{locationColumn}' values ​​was entered incorrectly.")
            print("Try Again ..", "\n" * 2)
            BOARD()
            continue

        else:

            indexLine = alphabetList.index(locationLine)
            indexColumn = alphabetList.index(locationColumn)

            if indexLine > line - 1 or indexColumn > column - 1:
                print("Wrong location chosen ..Try Again.")
                print("\n" * 2)
                BOARD()
                continue

            elif board[indexLine][indexColumn] != "-":
                print("This location filled with another value. Please,choose diffirent location .")
                print("\n" * 2)
                BOARD()
                continue


            else:

                squareNumber += 1
                soLoop = True

                while soLoop:

                    soInput = input("Please , Enter the one of  'S' or 'O' : \t").upper()
                    print("\n" * 2)

                    if soInput != "S" and soInput != "O":
                        print("Wrong value entered. Please , enter only one of the 'S' or 'O'")
                        print("\n" * 2)
                    else:
                        soLoop = False

                if soInput == "S":
                    s_Character_Positions.append((indexLine, indexColumn))
                else:
                    o_Character_Positions.append((indexLine, indexColumn))

                board[indexLine][indexColumn] = soInput

                # essential locations to check S.O.S
                # this locations for 'O' and 'S' control
                currentLocation = (indexLine, indexColumn)
                top = (indexLine - 1, indexColumn)
                bottom = (indexLine + 1, indexColumn)
                right = (indexLine, indexColumn + 1)
                left = (indexLine, indexColumn - 1)
                righttop = (indexLine - 1, indexColumn + 1)
                leftbottom = (indexLine + 1, indexColumn - 1)
                lefttop = (indexLine - 1, indexColumn - 1)
                rightbottom = (indexLine + 1, indexColumn + 1)

                # essential locations to check S.O.S
                # this locations for 'S' control
                dtop = (indexLine - 2, indexColumn)
                dbottom = (indexLine + 2, indexColumn)
                dright = (indexLine, indexColumn + 2)
                dleft = (indexLine, indexColumn - 2)
                drighttop = (indexLine - 2, indexColumn + 2)
                dleftbottom = (indexLine + 2, indexColumn - 2)
                dlefttop = (indexLine - 2, indexColumn - 2)
                drightbottom = (indexLine + 2, indexColumn + 2)


                # checking S.O.S
                def SOS(score=0):

                    if soInput == "O":

                        if not OUTOFBOARD(top) and not OUTOFBOARD(bottom):
                            if top in s_Character_Positions and bottom in s_Character_Positions:
                                score += 1

                        if not OUTOFBOARD(right) and not OUTOFBOARD(left):
                            if right in s_Character_Positions and left in s_Character_Positions:
                                score += 1

                        if not OUTOFBOARD(righttop) and not OUTOFBOARD(leftbottom):
                            if righttop in s_Character_Positions and leftbottom in s_Character_Positions:
                                score += 1

                        if not OUTOFBOARD(lefttop) and not OUTOFBOARD(rightbottom):
                            if lefttop in s_Character_Positions and rightbottom in s_Character_Positions:
                                score += 1



                    else:

                        if not OUTOFBOARD(top) and not OUTOFBOARD(dtop):
                            if top in o_Character_Positions and dtop in s_Character_Positions:
                                score += 1

                        if not OUTOFBOARD(righttop) and not OUTOFBOARD(drighttop):
                            if righttop in o_Character_Positions and drighttop in s_Character_Positions:
                                score += 1

                        if not OUTOFBOARD(right) and not OUTOFBOARD(dright):
                            if right in o_Character_Positions and dright in s_Character_Positions:
                                score += 1

                        if not OUTOFBOARD(rightbottom) and not OUTOFBOARD(drightbottom):
                            if rightbottom in o_Character_Positions and drightbottom in s_Character_Positions:
                                score += 1

                        if not OUTOFBOARD(bottom) and not OUTOFBOARD(dbottom):
                            if bottom in o_Character_Positions and dbottom in s_Character_Positions:
                                score += 1

                        if not OUTOFBOARD(leftbottom) and not OUTOFBOARD(dleftbottom):
                            if leftbottom in o_Character_Positions and dleftbottom in s_Character_Positions:
                                score += 1

                        if not OUTOFBOARD(left) and not OUTOFBOARD(dleft):
                            if left in o_Character_Positions and dleft in s_Character_Positions:
                                score += 1

                        if not OUTOFBOARD(lefttop) and not OUTOFBOARD(dlefttop):
                            if lefttop in o_Character_Positions and dlefttop in s_Character_Positions:
                                score += 1

                    return score


                BOARD()

        if playerTurn == player1 and SOS() == 0:
            playerTurn = player2

        elif playerTurn == player2 and SOS() == 0:
            playerTurn = player1

        elif playerTurn == player1 and SOS() != 0:
            player1Score += SOS()
            print(f"Congratulations! You made {SOS()} different S.O.S.".rjust(46))
        elif playerTurn == player2 and SOS() != 0:
            player2Score += SOS()
            print(f"Congratulations! You made {SOS()} different S.O.S.".rjust(46))

    SCORETABLE()

    print("\n")
    if player1Score > player2Score:
        print(f"Congratulations! {player1} . You Won!! ".rjust(46))
    elif player2Score > player1Score:
        print(f"Congratulations! {player2} . You Won !! ".rjust(46))
    else:
        print("DRAW...".rjust(30))
    print("\n")

    quit = input("Press 'Q' to exit, any key to continue: \t").upper()
    print("\n" * 2)
    if quit == "q".upper():
        print("Exiting...")
        break
