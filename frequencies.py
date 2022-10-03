"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

from pip import main


def frequencies(items):
    frequencies = {}
    # Your code goes here
    for item in items:
        if type(item) == int:
            item = str(item)
            
        if item in frequencies:
            frequencies[item] = frequencies.get(item) + 1
        else:
            frequencies[str(item)] = 1

    return frequencies
