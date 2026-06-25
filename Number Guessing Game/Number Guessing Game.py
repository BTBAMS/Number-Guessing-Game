#Number Guessing Game
import random
                   #Beginner coding version
'''
print("Welcome to the Number Guessing Game")
print("I'm thinking of a number between 1 and 100")

name= input("What is your name? ")
print(f"Hello {name}, Let's play")

#Computer selects a random Number between 1 and 100 
secret_number=random.randint(1, 100)

#print(f"DEBUG: secret number is {secret_number})")  #Temporary line just to test that the program is working
attempts = 0  #This is used to count the player's guess
while True:  #Keeps looping until the player wins
    guess= int(input("Enter your guess: "))
    attempts += 1  #Adds 1 attempt each time the player guesses
    
    if guess < secret_number:
        print("Your guess is too low! Try again.\n")
    elif guess > secret_number:
        print("Your guess is too high! Try again. \n")
    else:
        print(f"Correct!! You got it in {attempts} attempts.")
        break #Exits loop when the player wins.
'''


                #Advanced Coding version
def get_rating(attempts):   #Returns a rating based on how many guesses the player had
    if attempts <=5:
        return 'Amazing! you are a mind reader'
    elif attempts <=8:
        return 'Great Job'
    elif attempts <=12:
        return "Not bad! Keep Practicing"
    else:
        return"Keep going you'll get better."
    
def play_game(name):
    secret_number = random.randint(1, 100)
    attempts = 0
    print("I'm thinking of a number between 1 and 100")
    
    while True:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:  #handles error when you enter letters, symbols etc.
            print("Please enter a valid number")
            continue
        
        attempts +=1
        if guess <1 or guess>100:
            print("Please guess a number between 1 and 100")
            attempts -=1  #Does not count invalid guesses
        elif guess < secret_number:
            print("Guess is too low! Try again.\n")
        elif guess > secret_number:
            print("Guess is too high! Try again. \n")
        else:
            print(f"Correct!! The secret number was {secret_number}.")
            print(f"You got the secret number in {attempts} attempts.")
            print(get_rating(attempts))
            break  #Exit loop when the pkayer wins.

def main():   #Main function that controls the overall flow of the game
    print("Number Guessing Game")
    
    name = input("What is your name? ")
    print(f"Hello {name} Let's Play.")
    
    while True:
        play_game(name)
        
        again = input("Would you like to play again? (yes/no): ").lower()
        if again != "yes":
            print(f"Thanks for playing the game {name}. See you next time")
            break

main()
    
    