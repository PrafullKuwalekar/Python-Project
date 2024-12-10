import random
import time

# Initial steps to invite in the game
print("\nWelcome to Hangman game\n")
name = input("Enter your name: ")
print(f"Hello {name}! Best of Luck!")
time.sleep(2)
print("The game is about to start!\nLet's play Hangman")
time.sleep(2)

def main():
    global count, display, word, already_guessed, play_game
    words_to_guess = ["january", "border", "image", "film", "promise", "kids", "lungs", "doll", "rhyme"]
    word = random.choice(words_to_guess)
    count = 0
    display = '_' * len(word)
    already_guessed = []
    play_game = ""

def play_loop():
    play_game = input("\nDo you want to play again? (y = yes, n = no): ").lower()
    if play_game == "y":
        main()
        hangman()
    elif play_game == "n":
        print("Thanks for playing! We expect you back again!")
        exit()
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
        play_loop()

def hangman():
    global count, display, word, already_guessed
    limit = 5

    while count < limit:
        guess = input(f"\nThis is the Hangman Word: {display}\nEnter your guess: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("\nInvalid Input, please enter a single letter.\n")
            continue

        if guess in already_guessed:
            print("\nYou already guessed that letter. Try another one.\n")
            continue

        if guess in word:
            already_guessed.append(guess)
            display = ''.join([char if char in already_guessed else '_' for char in word])
            print(f"\nGood guess: {display}\n")

            if display == word:
                print("Congrats! You have guessed the word correctly!")
                play_loop()
                break
        else:
            count += 1
            already_guessed.append(guess)
            print(f"\nWrong guess. {limit - count} guesses remaining.\n")
            print_hangman(count)

    if count == limit:
        print("\nWrong guess. You are hanged!!!\n")
        print(f"The word was: {word}")
        play_loop()

def print_hangman(count):
    stages = [
        """
           _____
          |     
          |     
          |     
          |     
          |     
          |     
        __|__
        """,
        """
           _____
          |     |
          |     |
          |     
          |     
          |     
          |     
        __|__
        """,
        """
           _____
          |     |
          |     |
          |     |
          |     
          |     
          |     
        __|__
        """,
        """
           _____
          |     |
          |     |
          |     |
          |     O
          |     
          |     
        __|__
        """,
        """
           _____
          |     |
          |     |
          |     |
          |     O
          |    /|\\
          |    / \\
        __|__
        """
    ]
    print(stages[count - 1])

# Start the game
main()
hangman()
