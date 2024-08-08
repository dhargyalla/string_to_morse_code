# A text-based Python program to convert Strings into Morse Code.

# get the string
message = input("type the message to convert into morse code: \n").upper()

morse_code = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    " ": "  "
}
secret_code = ""

for letter in message:
    for code in morse_code:
        if letter == code:
            secret_code += morse_code[letter]
            secret_code += " "
            break
            
print("The corresponding morse code is:\n" + secret_code)







