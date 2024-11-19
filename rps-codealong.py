# welcoming player and giving instructions
print("Welcome Players 1 and 2\n When ask for your choice please enter 'r', 'p' ,'s'")

#getting players input 
playerOneInput = input("player one select: r, p or s")
playerTwoInput = input("player two select: r, p or s")

#print("player one input: " + playerOneInput + "\n" 
 #     + "player two input: " + playerTwoInput)

 #compare player input to determine result. Either1 one wins , player2 wins, or its a tie
if playerOneInput == "s":
    if playerTwoInput == "s":
        print("Its a tie!")
    if playerTwoInput == "r":
        print("player two wins!")
    if playerTwoInput == "p":
        print("player 1 wins!")

if playerOneInput == "r":
    if playerTwoInput == "r":
        print("Its a tie!")
    if playerTwoInput == "s":
        print("player 1 wins!")
    if playerTwoInput == "p":
        print("Player two wins!")

if playerOneInput == "p":
    if playerTwoInput == "p":
        print("Its a tie!")
    if playerTwoInput == "s":
        print("player 2 wins!")
    if playerTwoInput == "r":
        print("player 1 wins!")
    