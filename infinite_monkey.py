"""
author: Pencov Peter
date: 04.04.2024
version: Python 3.12.2

Infinite monkey program:
This program is designed to take a string as "required_sentence" 
and tries to match the string perfectly by randomly choosing one character at a time
from a-z and space. If the string is matched perfectly, the number of tries it took will be displayed.
Program can be interrupted manually via ctrl + c in console window

"""

import random
import string
import time



alphabet = list(string.ascii_lowercase)
alphabet.append(" ")

req_sentence = str(input("enter required sentence (a-z and space allowed): ")).lower()

def check_input(input_sentence):
    """checks user input
    all characters in req_sentence must be in alphabet"""
    result = True
    for i in input_sentence:
        if i not in alphabet:
            result = False
    return result
        
def random_sentence():
    """returns a random string (a-z and space)
    with the same number of characters as the required sentence"""
    result = ""
    for letter in req_sentence:
        result += random.choice(alphabet)
        
    return result

def compare_sentence(sentence):
    """compares given sentence(string) with required sentence character by character
    returns match percentage"""
    pos = 0
    matches = 0
    for letter in req_sentence:
        if letter == sentence[pos]:
            matches += 1
        pos += 1
    return  round(matches * 100 / len(req_sentence), 2)

def repeated_try():
    """Repeatedly calls random_sentence and compare_sentence until:
    both sentences match perfectly.
    Time betwen itterations can be changed by modifying time.sleep() argument
    While loop can be canceled manually by ctrl + c in console window
    """
            
    number_of_tries = 0
    sentence = random_sentence()
    current_match = compare_sentence(sentence)
    highest_match = -1
    best_string = ""
    
    while req_sentence != sentence:
        
        time.sleep(1)
        
        if current_match > highest_match:
            highest_match = current_match
            best_string = sentence
        
        print(f"required sentence is: {req_sentence}\nmonkey sentence is: {sentence}\nmatch percentege: {current_match} \
\n\n\tbest string so far: {best_string}, with percentile: {highest_match}%")
        
        sentence = random_sentence()
        current_match = compare_sentence(sentence)
        number_of_tries += 1
        
        continue
    print(f"wow, sentances match perfectly!\n total number of tries: {number_of_tries}")
        
def main():
    if not check_input(req_sentence):
        raise ValueError("invalid string. can only contain characters: a-z and space")
    repeated_try()
    
if __name__ == "__main__":
    main()
