#!/usr/bin/env python3

def return_evens(sequence):
    return [x for x in sequence if x % 2 == 0]

# Test the function
print(return_evens([0, 1, 3, 5, 7, 8, 9]))


def make_exclamation(sentence_list):
    return [sentence + "!" for sentence in sentence_list]

# Test the function
print(make_exclamation(["Hello", "I'm doing great", "Python is fun"]))