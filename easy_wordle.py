#Reese Saladin

import random
from wordle import check_word
import display_utility
from words import words

def filter_word_list(words, clues):
    """Takes input List containing tuples of the guess taken and their corresponding clues returned, which is a List. Returns a new word List
    containing only words that could be the secret word based on given clues"""
    good_words = []
    word_validity = False
    if len(clues) == 0:
        good_words = words[:]
        return good_words
    for word in words: #Checks word using logic given from Project 1 File
        count = 0
        for i in range(len(clues)):
            for index in range(5):
                if check_word(word.upper(), clues[i][0])[index] == clues[i][1][index]:
                    count +=1
                if count == len(clues)*5:
                    word_validity = True
                else:
                    word_validity = False
        if word_validity == True:
            good_words.append(word.lower())
    return good_words


def easy_game(secret):
    """Plays a game of easy wordle with the user. Takes string input of the secret word. User guesses a word and in response
    is printed the number of words possible with given clues, and 5 possible words (If less than 5 possible, prints all possible)"""
    clues = []
    rounds_left = 6
    words_list = words
    while rounds_left>0:
        validity = True
        guess = input("> ").upper()
        if guess.lower() not in words:
            validity = False
        while validity == False:
            print("Not a word. Try again")
            guess = input("> ").upper()
            if guess.lower() not in words:
                continue
            else:
                validity = True
        hints = check_word(secret,guess)
        clues.append((guess, hints))
        for round in range(len(clues)):
            for index in range(5):
                if clues[round][1][index] == "green":
                    display_utility.green(clues[round][0][index])
                elif clues[round][1][index] == "yellow":
                    display_utility.yellow(clues[round][0][index])
                elif clues[round][1][index] == "grey":
                    display_utility.grey(clues[round][0][index])
                if index==4 and guess == secret:
                    print()
            if guess != secret:
                print()
        words_list = filter_word_list(words_list, clues)
        random.shuffle(words_list)
        print(f"{len(words_list)} words possible:")
        if len(words_list) >= 5:
            for i in range(5):
                print(words_list[i])
        else:
            for word in words_list:
                print(word)
        rounds_left -= 1
        if guess == secret:
            rounds_left = 0
    print(f"Answer: {secret}")

if __name__ == "__main__":
    """Starts an easy_wordle game with a random secret word from "words" list"""
    easy_game((random.choice(words)).upper()) #Found "choice" method from https://docs.python.org/3/library/random.html#functions-for-sequences