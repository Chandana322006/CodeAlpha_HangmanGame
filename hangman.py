import random
words = ["python", "java", "kotlin", "javascript", "programming"]
word = random.choice(words)
hidden_word = ["_"] * len(word)
attempts = 6
guessed_letters = []
while attempts > 0 and "_" in hidden_word:
    print("\n" + " ".join(hidden_word))
    guess = input("Guess a letter: ").lower()
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue
    guessed_letters.append(guess)
    if guess in word:
        for index, letter in enumerate(word):
            if letter == guess:
                hidden_word[index] = guess
        print(f"Good guess! The letter '{guess}' is in the word.")
    else:
        attempts -= 1
        print(f"Wrong guess! You have {attempts} attempts left.")
if "_" not in hidden_word:
    print("\n" + " ".join(hidden_word))
    print("Congratulations! You guessed the word.")
else:
    print(f"\nGame over! The word was: {word}")