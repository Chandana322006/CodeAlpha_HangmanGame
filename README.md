# Hangman Game

A simple Python implementation of the classic Hangman word-guessing game.

## Overview

This is an interactive command-line Hangman game where players try to guess a hidden word by suggesting letters one at a time. You have 6 attempts to guess the word correctly.

## Features

- **Word Bank**: Game includes a pre-defined list of programming-related words
- **Input Validation**: Only accepts single alphabetic characters
- **Duplicate Detection**: Prevents re-guessing the same letter
- **Attempt Tracking**: Shows remaining attempts after each wrong guess
- **Win/Lose Conditions**: Clear victory message or reveals the word on loss

## How to Play

1. Run the program: `python hangman.py`
2. A random word will be selected and hidden with underscores
3. Guess letters one at a time when prompted
4. Each correct guess reveals all instances of that letter in the word
5. Each wrong guess reduces your attempts by 1
6. Win by guessing the word before running out of attempts
7. Lose if you run out of attempts before completing the word

## Game Rules

- You have **6 attempts** to guess the word
- Enter only **one letter** at a time (a-z)
- You **cannot guess the same letter twice**
- All input is converted to lowercase
- Invalid input (numbers, symbols, multiple characters) will be rejected

## Word List

The game includes the following programming-related words:
- python
- java
- kotlin
- javascript
- programming

## Requirements

- Python 3.x

## Example Gameplay

```
_ _ _ _ _ _
Guess a letter: e
Good guess! The letter 'e' is in the word.

_ e _ _ _ _
Guess a letter: a
Wrong guess! You have 5 attempts left.
```

## License

This project is part of CodeAlpha
