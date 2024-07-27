import random

def wordForHangman():
    wordsList = ['string', 'variable', 'function', 'library', 'method', 'integer', 'coding', 'bioinformatics', 'phyton']
    return random.choice(wordsList)

def hangmanSketch(tries):
    stages = [
        """
           ------
           |    |
           |    
           |    
           |   
           -
        """,
         """
           ------
           |    |
           |    O
           |    
           |   
           -
        """,
         """
           ------
           |    |
           |    O
           |    |
           |   
           -
        """,
        """
           ------
           |    |
           |    O
           |   /|
           |   
           -
        """,
         """
           ------
           |    |
           |    O
           |   /|\\
           |   
           -
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / 
           -
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           -
        """
    ]
    return stages[tries]

def hangman():
    print("Let's play Hangman!")
    word = wordForHangman()
    wordLines = "_" * len(word)
    print(wordLines)

    guessed = False

    wordsGuessed = list()
    tries = 0
    print(hangmanSketch(tries))

    while not guessed and tries < 6:
        playerGuess = input("Enter  your guess(preferably a letter):")
        if len(playerGuess) == 1 and playerGuess.isalpha():
            if playerGuess not in word:
                print("Your guess is wrong.")
                tries += 1
                wordsGuessed.append(playerGuess)
                print(wordLines)
                print(hangmanSketch(tries))
            elif playerGuess in wordsGuessed:
                print("You have already guessed that.")
                print(wordLines)
                print(hangmanSketch(tries))
            elif playerGuess in word:
                print("Your guess", playerGuess, "is right!")
                wordsGuessed.append(playerGuess)
                wordShowcase = list(wordLines)
                wordsCorrect = [i for i, letter in enumerate(word) if letter == playerGuess]
                for wordCorrect in wordsCorrect:
                    wordShowcase[wordCorrect] = playerGuess
                wordLines = "".join(wordShowcase) 
                if wordLines == word:
                    guessed = True  
                print(wordLines)
                print(hangmanSketch(tries))  
        elif len(playerGuess) == len(word) and playerGuess.isalpha():
            if playerGuess == word:
                guessed = True
            else:
                print("The guess is wrong.")
                tries += 1
                wordsGuessed.append(playerGuess)
                print(wordLines)
                print(hangmanSketch(tries))    
        else:
            print("Invalid. Try Again.")
            print(wordLines) 

    if guessed == True:
        print("Congrats!!!")
    else:
        print("Sorry, you lost. The word is ", word,".") 

hangman()

    
