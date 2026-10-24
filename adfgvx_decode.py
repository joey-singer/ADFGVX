import math
import sys

def prune(message):
    # Prune spaces, convert all to uppercase, TO ADD: Error handling for non-alphanumeric characters
    message = message.upper()
    message = message.replace(" ","")
    return message

def list2str(list):
    return "".join(list)

# Top level code msg = prune(input("Enter Message: "))
transpositon = input("Enter ADFGVX Transposition Word: ")

""" Using fixed Polybius square for now, same as the one provided on Wikipedia:
|   | A | D | F | G | V | X |
| A | N | A | 1 | C | 3 | H |
| D | 8	| T	| B	| 2	| O | M |
| F | E	| 5	| W	| R | P	| D |
| G | 4	| F	| 6	| G	| 7 | I |
| V | 9	| J	| 0	| K | L	| Q |
| X | S	| U	| V	| X	| Y	| Z | """

poly_square = [ # Currently from wikipedia, will find a way to randomize soon
    ["N", "A", "1", "C", "3", "H"],
    ["8", "T", "B", "2", "O", "M"],
    ["E", "5", "W", "R", "P", "D"],
    ["4", "F", "6", "G", "7", "I"],
    ["9", "J", "0", "K", "L", "Q"],
    ["S", "U", "V", "X", "Y", "Z"]
] 