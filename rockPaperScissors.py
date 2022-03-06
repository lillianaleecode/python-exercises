"""Rock Paper Scissors   
Exercise 8 (and Solution)
Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock
"""
#now i need to try to loop it again .rest game.
# 3 rounds. only if win 3 times, wins the whole game. the game keeps looping while this is true.

def main():
    player1Score = 0
    player2Score = 0

    while True:
        player1 = input("Player 1: Rock, Paper, or Scissor?")
        player2 = input("Player 2: Rock, Paper, Scissor?")
        
        #cases:
        if player1Score == 2:
            print(player1Score)
            print(player2Score)
            playAgain = input("Player 1 won!, start new game? (Y/N)")
            if playAgain == "Y":
                player1Score == 0#checking purposes
                player2Score == 0#checking purposes
                print(player1Score)
                print(player2Score)
                main()
            else:
                print("Okay, have a nice day!")
                break

        elif player2Score == 2:
            print(player1Score)
            print(player2Score)
            playAgain = input("Player 2 won!, start new game? (Y/N)")
            if playAgain == "Y":
                player1Score == 0 #checking purposes
                player2Score == 0#checking purposes
                print(player1Score)
                print(player2Score)
                main()
            else:
                print("Okay, have a nice day!")
                break
        elif player2Score == player1Score and player1Score == 2:
            print(player1Score)
            print(player2Score)
            playAgain = input("Tie!, start new game? (Y/N)")
            if playAgain == "Y":
                player1Score == 0#checking purposes
                player2Score == 0#checking purposes
                print(player1Score)
                print(player2Score)
                main()
            else:
                print("Okay, have a nice day!")
                break
        else:

            if player1 == "Rock" and player2 == "Scissor":
                player1Score = player1Score + 1
                print("player 1 wins!")
                print(player1Score)
                print(player2Score)
            elif player1 == "Rock" and player2 == "Paper":
                player2Score += 1
                print("player 2 wins")
                print(player1Score)
                print(player2Score)
            elif player1 == "Scissor" and player2 == "Rock":
                player2Score += 1
                print("player 2 wins")
                print(player1Score)
                print(player2Score)
            elif player1 == "Scisor" and player2 == "Paper":
                player1Score += 1
                print("player1 wins" )
                print(player1Score)
                print(player2Score)
            elif player1 == "Paper" and player2 == "Rock":
                player1Score += 1
                print("player1 wins" )
                print(player1Score)
                print(player2Score)
            elif player1 == "Paper" and player2 == "Scissor":
                player2Score += 1
                print("player2 wins" )
                print(player1Score)
                print(player2Score)

        
        

main() #main will help to restart the game.