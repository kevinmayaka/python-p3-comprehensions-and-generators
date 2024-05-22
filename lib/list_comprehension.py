#!/usr/bin/env python3

def return_evens(num_list):
    evens_list = [x for x in num_list if x % 2 == 0]
    return evens_list


def make_exclamation(sentence_list):
    strings_with_exclamation = [string + "!" for string in sentence_list]
    return strings_with_exclamation
