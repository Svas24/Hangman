# Write your code here
import random
import sys

won = 0
lost = 0
print("H A N G M A N")

while True:
    command = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:\n')
    if command == "exit":
        sys.exit(0)

    if command == "results":
        print(f"You won: {won} times.\nYou lost: {lost} times.")

    if command == "play":
        attempts = 8
        word = random.choice(("python", "java", "swift", "javascript"))
        user_inputs = set()  # user inputs
        display = list('-' * len(word))

        while attempts > 0 and display.count("-") > 0:
            inp = input(f"\n{''.join(display)}\nInput a letter: ")

            if len(inp) != 1:
                print("Please, input a single letter.")
                continue
            letter = inp[0]

            if not(letter.isalpha() and letter.islower()):
                print("Please, enter a lowercase letter from the English alphabet.")
                continue

            if letter in user_inputs:
                print("You've already guessed this letter.")
                continue
            else:
                user_inputs.add(letter)

            if letter in word:
                for i in range(len(word)):
                    if word[i] == letter:
                        display[i] = word[i]
            else:
                print("That letter doesn't appear in the word.")
                attempts -= 1

        if display.count('-') > 0:
            print("\nYou lost!")
            lost += 1
        else:
            print(f"You guessed the word {word}!\nYou survived!")
            won += 1