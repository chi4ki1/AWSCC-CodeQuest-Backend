player1= input("Player 1: ")
player2= input("Player 2: ")

if (player1 == "paper" and player2 == "scissors") or (player1 == "scissors" and player2 =="rock") or (player2 =="paper" and player1 == "rock"):
    print("Player 2 Wins!")
elif (player2 == "paper" and player1 == "scissors") or (player2 == "scissors" and player1 =="rock") or (player1 =="paper" and player2 == "rock"):
    print("Player 1 Wins!")
elif (player1 == "paper" and player2 =="paper") or (player1 == "scissors" and player2 == "scissors") or (player1 == "rock" and player2 == "rock"):
    print("It's a TIE!")