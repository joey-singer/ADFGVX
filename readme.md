# ADFGVX Cypher Encode/Decode

## What is this?
- This repo contains scripts to encode and decode text typed in the ADFGVX Cypher.
- DO NOT USE THIS FOR ENCRYPTING ANYTHING OF REAL IMPORTANCE, ADFGVX HAS NOT BEEN SECURE SINCE 1918!!!!!

### Why?
1) I wanted to get some extra practice with programming in python, as my current course load uses the concepts used in this a decent amount
2) I’m a history buff
3) Why not?

## What is ADFGVX?
- The ADFGVX Cypher was a cypher used in 1918 by the Imperial German Army (*Deutches Heer*) in World War I.
- It used a Polybius Square and Columnar Transpose to encode its messages.
- More info on the ADFGVX cypher is available on Wikipedia at: <a href=https://en.wikipedia.org/wiki/ADFGVX_cipher>https://en.wikipedia.org/wiki/ADFGVX_cipher</a>

## Coming Eventually
- Decode!
- Dynamic Polybius Square creation to secure/formulate cypher more accurately (without you needing to carry around a codebook)
  - The current Polybius Square used comes from the example provided on the Wikipedia article associated to this topic; it is not randomized (as would be more “secure” accurate to its historical use)
Polybius Square:

|   | A | D | F | G | V | X |
| - | - | - | - | - | - | - |
| A | N | A | 1 | C | 3 | H |
| D | 8 | T | B | 2 | O | M |
| F | E | 5 | W | R | P | D |
| G | 4 | F | 6 | G | 7 | I |
| V | 9 | J | 0 | K | L | Q |
| X | S | U | V | X | Y | Z |
