#!/usr/bin/env python3

def return_evens(num_list):
    even_integers = [num for num in num_list if num % 2 == 0]
    return even_integers
    pass

def make_exclamation(sentence_list):
    add_exclamation = [str + '!' for str in sentence_list]
    return add_exclamation
    pass