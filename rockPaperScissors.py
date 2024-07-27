import random
choices = ['rock', 'paper', 'scissors']
computerChoice = random.choice(choices)
userChoice = input('Enter your choice: ').lower()
print("Your choice:", userChoice)
print("Bot choice:", computerChoice)
if userChoice == computerChoice:
    print("It's a tie. Better luck next time!")
elif userChoice == 'rock':
    if computerChoice == 'paper':
        print("Paper covers rock, better luck next time!")
    else:
        print("Rock crushes scissors, you won!")
elif userChoice == 'paper':
    if computerChoice =='rock':
        print("Paper covers rock, you won!")
    else:
        print("Scissors cuts paper, you lost. Better luck next time!")
elif userChoice == 'scissors':
    if computerChoice == 'paper':
        print("Scissors cut paper, you won!")
    else:
        print("Rock crushes scissors, you lost. Better luck next time!")                               