import random
import word_list
import ascii_art

# Welcome to my hangman game.
# You will need to download the word_list file and ascii_art file from the repo

game_on = True

while True:
    #Define the variables that will be used in the code
    stages = ascii_art.stages
    chosen_word = random.choice(word_list.word_list)
    word_length = len(chosen_word)
    display = []
    life = 6
    letters = []
    
    # This will represent our blank spaces
    for letter in chosen_word:
        display.append("_")
    
    # Print the welcome stage
    print(ascii_art.logo)
    print(stages[life])
    print(f"{' '.join(display)}")

    while game_on:

        # Ask the user to guess a letter and assign their answer to a variable called guess.
        guess = input("Guess a letter: ").lower()
        print("\n" * 80)
        
        # This will let the user know they are guessing repeats
        if guess in letters:
            print(f"You have already guessed {guess}, try again!")

        # If the letter is wrong the user will lose a life
        # The guessed letter will also be added to a list
        if guess not in chosen_word:
            life = life - 1
            letters.append(guess)
            print(f"You chose {guess}, this letter is not in the word!\nYou lose a life!")

        # If the letter is correct it will be displayed for the user
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter
                print(f"You chose {guess}, this letter is in the word!\nGood job keep going!")
        
        # Here we give the display a quick tidy by joining the lists
        print(stages[life])
        print(f"{' '.join(display)}")
        print(f"{' '.join(letters)}")
        
        # This is our win condition
        if not "_" in display:
            print("YOU WIN!")
            game_on = False
        
        # This is our win condition
        if life == 0:
            print(f'GAME OVER!\nThe word was "{chosen_word}"')
            game_on = False
    
    # Give the user a chance to replay the game from the begining
    replay = input("Would you like to play again: Y or N?").lower()
    if replay == "y":
        print("\n" * 80)
        game_on = True
        continue
    else:
        print("Thanks for playing!")
        break
