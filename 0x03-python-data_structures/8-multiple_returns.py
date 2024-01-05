#!/usr/bin/python3
def multiple_returns(sentence):
    longeur = len(sentence)
    premier = sentence[0] if longeur > 0 else "None"
    total = longeur, premier
    return(total)
