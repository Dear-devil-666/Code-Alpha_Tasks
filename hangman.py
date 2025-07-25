import random
# List of possible words
word_list = ["python", "hangman", "developer", "language","code"]
hangman_stages = [
    '''
       +---+
       |   |
           |
           |
           |
           |
    =========
    ''',  # 6 lives left

    '''
       +---+
       |   |
       O   |
           |
           |
           |
    =========
    ''',  # 5 lives left

    '''
       +---+
       |   |
       O   |
       |   |
           |
           |
    =========
    ''',  # 4 lives left

    '''
       +---+
       |   |
       O   |
      /|   |
           |
           |
    =========
    ''',  # 3 lives left

    '''
       +---+
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    ''',  # 2 lives left

    '''
       +---+
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    ''',  # 1 life left

    '''
       +---+
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    '''   # 0 lives left - Game over
]

# randomly select word
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
guessed_letters = []


display = ['_' for _ in chosen_word]
lives = 6

print("🎮 Welcome to Hangman!")

# game loop
while lives > 0 and '_' in display:
    print(hangman_stages[6 - lives])
    print("\nWord: " + " ".join(display))
    guess = input("Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single alphabetic character.")
        continue

    if guess in guessed_letters:
        print(f"⚠️ You've already guessed '{guess}'. Try another letter.")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        for i in range(word_length):
            if chosen_word[i] == guess:
                display[i] = guess
        print(f"✅ Good job! '{guess}' is in the word.")
    else:
        lives -= 1
        print(f"❌ Wrong guess! You lost a life. Lives remaining: {lives}")

# after game over
if '_' not in display:
    print("\n🎉 Congratulations! You guessed the word:", chosen_word)
else:
    print("\n 💀Game Over! The word was:", chosen_word)