import random

"""
User will play Rock-Paper-Scissors game with the computer. Player and the computer will choose rock, paper, or scissors. 
If you win, you gain a point. 
One game includs three runs.
"""
#greeting
print("WELCOME - Rock-Paper-Scissors - GAME \n")

#define the list
rps = ["rock","paper","scissors"]

#initializing variables
i=0
win=0
draw=0
loose=0

#playing 3 rounds of game
while i<3:
    #Asking player2 for the next move
    player2 = input("\nWhat is your move: ")
    player2=player2.lower()
    
    #player1 is the computer and choosing rock-paper-scissors
    player1=random.choice(rps)
    print("Player1 move: ", player1)
    
    if(player2 in rps):    
        #comparing player1 and player2 to see who really wins
        if player2 == "rock" and player1 =="scissors":
            win += 1
            print ("YOU WIN")
        elif player2=="paper" and player1 =="rock":
            print("YOU WIN")
            win += 1
        elif player2=="scissors" and player1 == "paper":
            print ("YOU WIN")
            win += 1
        elif player1==player2:
            print("Draw")
            draw += 1
        else:  
            print("YOU LOOSE")
            loose += 1

        #going to next round
        i = i+1
    
    else:
        print("Wrong Input. Please choose one of the following: rock, paper, scissors")     
        
#score board
print("\nWin:", win, "  Loose:", loose, "  Draw:", draw, "\n")   


