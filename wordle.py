#Reese Saladin

import random
import display_utility
from words import words

def check_word(secret, guess):
    """Takes String inputs of the secret word and word guessed, and outputs a list of length 5 containing Strings 
    "green", "yellow", or "grey", corresponding to each letter's validity in secret, based on the rules of wordle"""
    color_output = [None] * 5
    secret_separate = list(secret)
    guess_separate = list(guess)
    for x in range(5): #Assigns green to letters that are in both words, and in the same index
        for i in range(5):
            if guess_separate[x] == secret_separate[i] and x==i:
                color_output[x] = "green"
    for x in range(5): #Assigns yellow letters by adding necessary yellow clues left to right
        if color_output[x] != "green":
            num_in_secret = secret_separate.count(guess_separate[x])
            num_in_guess = guess_separate.count(guess_separate[x])
            count = num_in_secret
            if num_in_secret<num_in_guess:
                for i in range(5): #Takes total count of letter appearance, subtracts letters already made green or yellow
                    if guess_separate[x] == guess_separate[i] and guess_separate[i] == secret_separate[i]:
                        count -= 1
                    for num in range(5):
                        if guess_separate[x] == guess_separate[num] and color_output[num] == "yellow" and num < i:
                            count -= 1
            if count>0: #Gives yellows while necessary
                    color_output[x] = "yellow"
            if count<=0: #Gives grey to letter multiples that have enough clues
                color_output[x] = "grey"
    for num in range(5): #Assigns any letter not in secret to grey
        if color_output[num] == None:
            color_output[num] == "grey"
    return color_output

def known_word(clues):
    """Takes input List containing tuples of the guess taken and their corresponding clues returned in a List. Returns a String output
    with 5 characters, with letters where letters are known to be, and a _ where letters are not kown to be"""
    known_list = ["_"] * 5
    for round_result in clues:
        for i in range(5):
            if round_result[1][i] == "green":
                known_list[i] = round_result[0][i]
    return ''.join(known_list)

def no_letters(clues):
    """Takes input List containing tuples of the guess taken and their corresponding clues returned in a List. Returns an alphabetically ordered 
    String of letters that are only grey, and therefore will not be in the secret word"""
    green_yellow_letters = []
    grey_letters_list = []
    for round_result in clues: #Adds all letters that are not in secret to a list
        guess = list(round_result[0])
        clue = round_result[1]
        for i in range(5):
            if clue[i] == "green" or clue[i] == "yellow":
                green_yellow_letters.append(guess[i])
            else:
                grey_letters_list.append(guess[i])
    for letter in grey_letters_list:
        if letter in green_yellow_letters:
            grey_letters_list.remove(letter)
    grey_letters_set = set(grey_letters_list) #Casts list to set to remove repeats
    grey_letters_list_unrepeated = list(grey_letters_set)
    grey_letters_list_unrepeated.sort()
    grey_letters = ''.join(grey_letters_list_unrepeated)
    return grey_letters

def yes_letters(clues):
    """Takes input List containing tuples of the guess taken and their corresponding clues returned in a List. Returns an alphabetically ordered
    String of letters that are green or yellow, and therefore will be in the secret word"""
    green_yellow_letters_list = []
    for round_result in clues:
        guess = list(round_result[0])
        clue = round_result[1]
        for i in range(5):
            if clue[i] == "green" or clue[i] == "yellow":
                green_yellow_letters_list.append(guess[i])
    green_yellow_letters_set = set(green_yellow_letters_list) #Casts list to set to remove repeats
    green_yellow_letters_list_unrepeated = list(green_yellow_letters_set)
    green_yellow_letters_list_unrepeated.sort()
    green_yellow_letters = ''.join(green_yellow_letters_list_unrepeated)
    return green_yellow_letters


def game(secret):
    """Takes an input String that serves as the secret word, and Returns nothing. Plays a game of Wordle with the user
    entering a guess and getting clues, known_word, yes_letters, and no_letters printed in response. Maximum of 6 guesses allowed"""
    clues = []
    rounds_left = 6
    while rounds_left>0:
        print(f"Known:  {known_word(clues)}")
        print(f"Green/Yellow Letters: {yes_letters(clues)}")
        print(f"Grey Letters: {no_letters(clues)}")
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
                if index==4 and guess == secret and round != len(clues)-1:
                    print()
            if guess != secret:
                print()
        rounds_left -= 1
        if guess == secret:
            rounds_left = 0
    print(f"\nAnswer: {secret}")

if __name__ == "__main__":
    """Starts a Wordle game with a random secret word from "words" list"""
    game((random.choice(words)).upper()) #Found "choice" method from https://docs.python.org/3/library/random.html#functions-for-sequences

