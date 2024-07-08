#This is the simple gae of rock, paper, scissor game.
import random                                                                   #importing the library to give a random number to the computer to play
game = {1 : "rock",                                                             #dictionary to initialize the rock paper scissor
2 : "paper",
3 : "scissor"}
print("\t\t\t**************************************")                           #displaying welcome message
print("\t\t\t\"WELCOME TO THE ROCK PAPER SCISSOR GAME\"")
print("\t\t\t**************************************")
condition = True
your_score = 0
comp_score = 0
print("(1) for rock\n(2) for paper\n(3) for scissor\n(0) to quit:")
while condition:                                                                #condition for playing game as long as player wants
    player1= int(input("Your turn: "))
    if(player1 == 1):
        print("You choose", game[1])
    elif(player1 == 2):
        print("You choose" ,game[2])
    elif(player1 == 3):
        print("You choose", game[3])
    else:
        print("Quiting!")
        print(f"YOUR SCORE IS {your_score} AND COMPUTER'S SCORE IS {comp_score}")#displaying the final result
        if (your_score > comp_score):
            print("You are the winner!")
        elif your_score == comp_score :
            print("TIE!")
        else :
            print("Compter is the winner!")
        condition = False
        break
    print("computer's turn: ", end = "")                                        #computer's playing; generating the random number to play
    player2 =random.randint(1, 3)
    print(player2) 
    if(player2 == 1):
        print(f"computer choose :{game[1]}")
    elif(player2 == 2):
        print(f"computer choose :{game[2]}")
    elif(player2 == 3):
        print(f"computer choose :{game[3]}")

    if player1 == player2:                                                    #displaying the message that whether the player wins or the computer for the current game  
        print("\nIt's a tie!")
    else:
        if(player1 == 1 and player2 ==3 or player1 ==2 and player2 ==1 or player1 ==3 and player2 ==2):
            print("\nYou win!")
            your_score+=1
        else:
            print("\nYou lose, computer wins!")
            comp_score +=1       
    print("")

