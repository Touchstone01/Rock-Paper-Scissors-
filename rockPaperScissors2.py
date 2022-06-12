import random  # importing the random module

# Program to design the rock paper scissors

# R === Rock
# P === Paper
# S === Scissors

# This Function is to continue the game or nat after the player has win or lose


def continueTheGame():
    choice = input("Do you want to continue (y/n)? ").lower()
    if choice == 'y':
        rockPaperScissors()

# This Function is to get the player input
def userChoice():
    print("A Rock, Paper, Scissors Game")
    choice = input(
        "R - Rock\nS - Scissors\nP - Paper \nEnter Your Choice  (R,P,S): ").upper()
    return choice


# This Function is to get What R, P and S means and display it back to the player
def defineInputs(input):
    if (input == 'R'):
        response = "Rock"
    elif (input == 'S'):
        response = 'Scissors'
    elif (input == 'P'):
        response = 'paper'
    return response

# This is the Main Function that powers the game flow and in it contains all the conditions for the choices made by the user

def rockPaperScissors():
    possibleInputs = ['R', 'P', 'S']
    userInput = userChoice()

    while userInput not in possibleInputs:
        print("Wrong Input")
        continueTheGame()
        break
    else:
        computerInput = random.choice(possibleInputs)
        print(
            f"Player({defineInputs(userInput)}) \nComputer({defineInputs(computerInput)})")
        if userInput == computerInput:
            print(
                f"Both players selected {defineInputs(userInput)}. It's a tie!")
            continueTheGame()
        elif userInput == "R":
            if computerInput == "S":
                print(
                    f"{defineInputs(userInput)} smashes {defineInputs(computerInput)}! You win!")
                continueTheGame()
            else:
                print(
                    f"{defineInputs(computerInput)} covers {defineInputs(userInput)}! You lose.")
                continueTheGame()
        elif userInput == "P":
            if computerInput == "R":
                print(
                    f"{defineInputs(userInput)} covers {defineInputs(computerInput)}! You win!")
                continueTheGame()
            else:
                print(
                    f"{defineInputs(computerInput)} cuts {defineInputs(userInput)}! You lose.")
                continueTheGame()
        elif userInput == "S":
            if computerInput == "P":
                print(
                    f"{defineInputs(userInput)} cuts {defineInputs(computerInput)}! You win!")
                continueTheGame()
            else:
                print(
                    f"{defineInputs(computerInput)} smashes {defineInputs(userInput)}! You lose.")
                continueTheGame()


rockPaperScissors()
