#!/usr/bin/env python3

def return_evens(num_list):
    return [n for n in num_list if n % 2 ==0]
print(return_evens([2,3,4,5,6]))

def make_exclamation(sentence_list):
    return [n + "!" for n in sentence_list]
print(make_exclamation(["Hello", "I'm doing great", "Python is fun"]))
# Using a list comprehension, write a function make_exclamation() that takes a 
# list of sentence strings and returns a list of sentence strings with exclamation
# marks at the end.

# make_exclamation(["Hello", "I'm doing great", "Python is fun"])
# # ["Hello!", "I'm doing great!", "Python is fun!"]