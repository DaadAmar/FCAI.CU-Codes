# File: The 100 game
# program: A two player game in python where the goal
#         is to reach 100. Each player chooses from 0-10.
#         The first player to reach 100 wins.
# Author: Daad Amar Osman
# Date created : Feb 19,2024
# version : 3


def main():
    # Welcome Message for the players
    print("\n                               The 100 Game ")
    print('''     
          A two players game that starts from 0 and the goal is to 
          reach the sum of 100, each player alternatively adds a number 
          from 1 to 10 to the sum.The player who reaches 100 first wins.
    ''')
    # The starting number and the target number
    Sum = 0
    Goal = 100

    # The Game 
    while Sum < Goal:
        #Player 1 entry and validation
        play =int(input("Player 1: Enter a number from 1 - 10: "))
        while play < 1 or play > 10:
            play = int(input("Player 1: Enter a number from 1 - 10: "))
            
        # Check if the sum is above the required Goal
        temp = Sum + play    
        while  temp > Goal :
            print(f"The sum must not exceed {Goal} \n")
            play = int (input("Player 1: Enter a number from 1 - 10: "))
            temp = Sum + play
        Sum += play
        print(f"The Total is now {Sum}\n")
        
        # Check for Winner
        if Sum >= Goal:
            print("Player 1 Is the Winner 🏆\nGame Over \n")
            break
        
        #Player 2 entry and validation
        play =int(input("Player 2: Enter a number from 1 - 10: "))
        while play < 1 or play > 10:
            play = int(input("Player 2: Enter a number from 1 - 10: "))
            
        # Check if the sum is above the required Goal
        temp = Sum + play    
        while  temp > Goal :
            print(f"The sum must not exceed {Goal} \n")
            play = int (input("Player 2: Enter a number from 1 - 10: "))
            temp = Sum + play
        Sum += play
        print(f"The Total is now {Sum}\n")
        
        # Check for Winner
        if Sum >= Goal:
            print("Player 2 Is the Winner 🏆\nGame Over \n")
            break
        
#set the intial status to yes        
game = 'yes'

#repeat playing the game until told otherwise
while game == 'yes':
    main()
    game = input("Do you want to play The 100 Game again ?(yes/no)  ")
    

       

