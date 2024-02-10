#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random


# In[3]:


def choose_word():
    words = ["python", "hangman", "programming", "challenge", "computer"]
    return random.choice(words)


# In[4]:


def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display


# In[5]:


def hangman():
    word_to_guess = choose_word()
    guessed_letters = []
    attempts_left = 6

    print("Welcome to Hangman!")

    while attempts_left > 0:
        current_display = display_word(word_to_guess, guessed_letters)
        print(f"Word: {current_display}")
        print(f"Attempts left: {attempts_left}")

        guess = input("Enter a letter: ").lower()

        if guess.isalpha() and len(guess) == 1:
            if guess in guessed_letters:
                print("You've already guessed that letter. Try again.")
            elif guess in word_to_guess:
                guessed_letters.append(guess)
                print("Good guess!")
            else:
                attempts_left -= 1
                print("Incorrect guess. Try again.")
        else:
            print("Invalid input. Please enter a single letter.")

        if set(guessed_letters) == set(word_to_guess):
            print("Congratulations! You guessed the word:", word_to_guess)
            break

    if attempts_left == 0:
        print("Sorry, you ran out of attempts. The word was:", word_to_guess)


# In[ ]:


hangman()


# In[ ]:




