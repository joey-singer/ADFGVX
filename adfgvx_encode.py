import math
import sys

#Functions:
def prune(message):
    # Prune spaces, convert all to uppercase, TO ADD: Error handling for non-alphanumeric characters
    message = message.upper()
    message = message.replace(" ","")
    return message

def letter_assign(x):
    # Big if-else tree to assign a letter based on adfgvx
    if x == 0:
        return "A"
    elif x == 1:
        return "D"
    elif x == 2:
        return "F"
    elif x == 3:
        return "G"
    elif x == 4:
        return "V"
    elif x == 5:
        return "X"
    else:
        print("Error encountered. Exiting")
        sys.exit()

def assemble_cypher(message, encode_list):
    # For each letter: assign a tuple of row, col to each letter's location in the polybus square
    message_encoded_num = []
    message_encoded_letters = []

    for letter in message:
        for i, row_list in enumerate(encode_list):
            if letter in row_list:
                j = row_list.index(letter)
                local_pair = (i,j)
                message_encoded_num.append(local_pair)
                break
            else:
                continue

    for letter in message_encoded_num:
        # Use the tuple values to assign the ADFGVX to each letter, then combine into a string and assemble that into a list
        a = letter_assign(letter[0])
        b = letter_assign(letter[1])
        message_encoded_letters.append(a+b)
    return message_encoded_letters

def list2str(list):
    return "".join(list)

def transpose_from_word(message, tword):
    # Convert abc letter based list from the message into ADFGVX letter based list
    message_list = list(list2str(message))
    len_tword = len(tword) # get length of word for sorting indices
    tword = list(tword.upper()) # convert transposition word to a list of characters

    transpose_dict = {}
    for i, char in enumerate(tword): # sort each item into a tuple with the letter and its index
        key = (char,i)
        transpose_dict[key]=[]
    for i, letter in enumerate(message_list):
        if i != 0:
            dic_idx_i = (i % len_tword)
            assoc_key = (tword[dic_idx_i],dic_idx_i)
            transpose_dict[assoc_key].append(letter)
        else:
            dic_idx_i = 0
            assoc_key = (tword[dic_idx_i],dic_idx_i)
            transpose_dict[assoc_key].append(letter)
    sorted_transpose_dict = dict(sorted(transpose_dict.items()))
    reconstituted_message = list(sorted_transpose_dict.values())
    for i, inner_list in enumerate(reconstituted_message):
        reconstituted_message[i] = list2str(inner_list)
    return reconstituted_message


# main code:

msg = prune(input("Enter Message: "))
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
encoded = assemble_cypher(msg, poly_square)
print("Encoded Message:")
for i in encoded:
    print(i, end = " ")
print()
transposed_encode = transpose_from_word(encoded, transpositon)
print("Encoded & Transposed Message:")
for i in transposed_encode:
    print(i, end = " ")
print()