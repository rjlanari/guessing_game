"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random
import sys


def start_game():
    count = 0
    answer = int(random.randrange(1 , 10))
    print("Welcome to the guessing game!")
    while True:
        guess_number = input("Please enter a number from 1 to 10  ")
    
        try:
            guess_number = int(guess_number)
            count += 1     
        except ValueError:
            print("Oh no, that's not a valid number, please try again!  ")
        else:
            if guess_number < 1 or guess_number > 10:
                print("The number you chose is outside the range!")
            elif guess_number > answer:
                print("It's lower!  ")         
            elif guess_number < answer:
                print("It's higher!  ")            
        finally:
            if guess_number == answer:
                    print ("Got it! You took {} attempts to figure it out!".format(count))
                    sys.exit ("See you another time!")
        
    
       

    
    """Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
    
    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.



# Kick off the program by calling the start_game function.
start_game()