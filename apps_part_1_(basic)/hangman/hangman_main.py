
from hangman_word_list import word_list
from hangman_stages import stages
from hangman_logo import logo
import random

print(logo)
game_is_finished = False
lives = len(stages) - 1
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
print(f'The solution is {chosen_word}.')  # Testing code
display = []

for _ in range(word_length):
    display += "_"

while not game_is_finished:
    guess = input("Guess a letter: ").lower()

    # Use the clear() function imported from replit to clear the output between guesses.
    # clear()

    # this searches within a list
    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(f"{' '.join(display)}")

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            game_is_finished = True
            print("You lose.")

    if not "_" in display:  # TODO investigate this warning
        game_is_finished = True
        print("You win.")

    print(stages[lives])
