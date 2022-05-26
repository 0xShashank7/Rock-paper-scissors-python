import random

print("Welcome to the game Rock / Paper / Scissors")

user_guess = 0
computer_guess= 0

options = ["rock","paper","scissors"]

while True:
    
    user_input = input("Enter the game and select Rock / Paper / Scissors or Q to exit the game: ").lower()
    if user_input == "q":   
        break

    randomNo = random.randint(0,2)
    computer_pick = options[randomNo]
    print("Computer picked",computer_pick)


    if user_input=="rock" and computer_pick=="scissors":
        print("Yo win")
        user_guess+=1
    elif user_input=="paper" and computer_pick == "rock":
        print("yo win")
        user_guess+=1
    elif user_input=="scissors" and computer_pick=="paper":
        print("you win")
        user_guess+=1
    else:
        print("yo lose")
        computer_guess+=1

print("You won", user_guess, "times")
print("Computer won", computer_guess,"times")

