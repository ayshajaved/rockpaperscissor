#in this file, i am converting the simple game into an object oriented program.
import random
class Rps:                                                                           #declaring the class
    def __init__(self):                                                              #declaring the constructor
        self.game = {1 : "rock",
        2 : "paper",
        3 : "scissor"}
        self.condition = True
        self.your_score = 0
        self.comp_score = 0

    def display_welcome(self):                                                        #function for displaying the welcome message
        print("\t\t\t**************************************")
        print("\t\t\t\"WELCOME TO THE ROCK PAPER SCISSOR GAME\"")
        print("\t\t\t**************************************")
        print("(1) for rock\n(2) for paper\n(3) for scissor\n(0) to quit:")

   
        
    def initiate_game(self):                                                          #method to initiate the rock, paper and scissor game
        self.display_welcome()
        while self.condition:                                                         #loop to play until the plaer wants
            player1= int(input("Your turn: "))
            if(player1 == 1):
                print("You choose", self.game[1])
            elif(player1 == 2):
                print("You choose" ,self.game[2])
            elif(player1 == 3):
                print("You choose", self.game[3])
            else:
                print("Quiting!")                                                     #quiting if the plaer enters "0"
                print(f"YOUR SCORE IS {self.your_score} AND COMPUTER'S SCORE IS {self.comp_score}")
                if (self.your_score > self.comp_score):                               #displaying the final score of the player and the computer
                    print("You are the winner!")
                elif self.your_score == self.comp_score :
                    print("TIE!")
                else :
                    print("Compter is the winner!")
                self.condition = False
                break
            print("computer's turn: ", end = "")                                      #computer's playing by generating random value
            player2 =random.randint(1, 3)
            print(player2) 
            if(player2 == 1):
                print(f"computer choose :{self.game[1]}")                             #displaying the computer's choice along with the dictionary's value according to the key
            elif(player2 == 2):
                print(f"computer choose :{self.game[2]}")
            else:
                print(f"computer choose :{self.game[3]}")
            
            if player1 == player2:                                                    #checking that whether the player wins or the computer for the current game
                print("\nIt's a tie!")
            else:
                if(player1 == 1 and player2 ==3 or player1 ==2 and player2 ==1 or player1 ==3 and player2 ==2):
                    print("\nYou win!")
                    self.your_score+=1
                else:
                    print("\nYou lose, computer wins!")
                    self.comp_score +=1       
            print("")
        
            

play = Rps()                                                                          #declaring the object of the class Rps
play.initiate_game()                                                                  #calling the method of the class