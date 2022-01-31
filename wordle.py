#AmirElkess

import random
from pprint import pprint

words = open('words.txt')
n = 5

def prepare( n ):
    global words
    words = [word.rstrip().lower() for word in words if len(word) == (n+1)]

def randomize():
    # returns random word
    while True:
        word = random.choice(words)
        if word.isalpha():
            return word

def print_tutorial():
    print("================")
    print("In order to find the possible words, you have to answer 3 questions about your guess in each iteration as follows:")
    print("if you guessed the word 'traps' for example, you have to answer according to the game's tiles' color change")
    print("1) correct letters:                     ..a.. <= means only 'a' was guessed correctly (green box) in its spot, and the other letters should be replaced with dots")
    print("2) correct letters in incorrect places: ...p. <= means letter 'p' is part of the word but not in this spot(orange box), other letters replaced with dots")
    print("3) incorrect letters: trs <= type all letters without space")
    print("================")


def search(query, contains, not_contains, incl_strs, n):
    matches = []
    for word in words:
        ln = 0
        for i in range(len(query)):
            if word[i] == query[i] or query[i] == '.':
                ln += 1

        append_word = False
        if ln == n:
            append_word = True

        for letter in contains:
            if letter not in word:
                append_word = False

        for letter in not_contains:
            if letter in word:
                append_word = False

        # incl_str indicate strings of correct letters in incorrect places
        # ex: w.... => word contains 'w' but not in index 0 of the word

        # _incl_str = .a...
        #    word   = plays # will be accepted as 'a's don't align

        for _incl_str in incl_strs:
            for i in range(n):
                if _incl_str[i] == word[i]:
                    append_word = False

        if append_word:
            matches.append(word)
    

    return matches


if __name__ == '__main__':
    print("Welcome to Wordle solver")
    n = int(input("how many letters (if unsure type 5): "))
    prepare(n)

    while True:
        print(f"Random word: {randomize()}")
        retry = input("Try another word? y/N ")
        if retry.lower() == 'n' or retry.strip() == '':
            break


    include = set() #letters that are part of the word but guessed in incorrect place
    incl_strs = []
    not_incl = set() #letters that are not part of the word
    
    print_tutorial()
    
    for i in range(n):
        correct = input("1) Input correct letters in correct places:   ")
        
        include_str = input("2) Input correct letters in incorrect places: ")
        incl_strs.append(include_str)
        for letter in include_str:
            if letter != '.':
                include.add(letter)
        
        not_incl_temp = input("3) Input incorrect letters: ")
        for letter in not_incl_temp:
            not_incl.add(letter)

        print("Possible words: ")
        pprint(search(correct, include, not_incl, incl_strs, n))
        print("================")
    

# to do:
# check user inputs for inconsistencies
